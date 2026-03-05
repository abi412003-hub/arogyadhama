import frappe
from frappe.model.document import Document


class TreatmentSchedule(Document):
    def validate(self):
        self.update_completion()

    def update_completion(self):
        if self.total_sessions and self.total_sessions > 0:
            self.completion_percentage = (
                (self.completed_sessions or 0) / self.total_sessions
            ) * 100
        else:
            self.completion_percentage = 0

        # Auto-update status based on completion
        if self.completed_sessions and self.total_sessions:
            if self.completed_sessions >= self.total_sessions:
                self.status = "Completed"
            elif self.completed_sessions > 0:
                self.status = "In Progress"

    def on_submit(self):
        frappe.msgprint(
            f"Treatment Schedule ({self.treatment_type}) for {self.patient_name} "
            f"has been submitted. {self.total_sessions or 'N/A'} sessions planned.",
            alert=True
        )

    @frappe.whitelist()
    def mark_session_complete(self):
        """Called by Treatment Specialist to mark one session as done."""
        self.completed_sessions = (self.completed_sessions or 0) + 1
        self.update_completion()
        self.save(ignore_permissions=True)
        frappe.msgprint(
            f"Session {self.completed_sessions}/{self.total_sessions} completed.",
            alert=True
        )
