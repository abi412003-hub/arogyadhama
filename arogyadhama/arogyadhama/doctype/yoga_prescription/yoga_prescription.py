import frappe
from frappe.model.document import Document


class YogaPrescription(Document):
    def validate(self):
        self.calculate_total_duration()

    def calculate_total_duration(self):
        total = 0
        if self.yoga_practices:
            for practice in self.yoga_practices:
                total += (practice.duration_minutes or 0)
        self.total_duration_minutes = total

    def on_submit(self):
        frappe.msgprint(
            f"Yoga Prescription for {self.patient_name} submitted. "
            f"Total: {self.total_duration_minutes} minutes, {len(self.yoga_practices)} practices.",
            alert=True
        )
