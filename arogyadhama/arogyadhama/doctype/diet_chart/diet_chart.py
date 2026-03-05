import frappe
from frappe.model.document import Document


class DietChart(Document):
    def validate(self):
        if not self.patient:
            frappe.throw("Patient is required")
        if not self.practitioner:
            frappe.throw("Prescribing practitioner is required")

    def before_submit(self):
        # Notify the patient's therapist about the new diet chart
        pass

    def on_submit(self):
        frappe.msgprint(f"Diet Chart for {self.patient_name} has been submitted.", alert=True)
