import frappe

def after_install():
    create_roles()
    create_departments()
    frappe.db.commit()
    print("Arogyadhama Health: Setup complete!")

def create_roles():
    roles = [
        "Naturopathy Intern", "Naturopathy Doctor", "Ayurveda Doctor",
        "Therapist", "Yoga Therapist Intern", "Treatment Specialist",
        "Facility Manager", "Arogyadhama Admin",
    ]
    for role_name in roles:
        if not frappe.db.exists("Role", role_name):
            doc = frappe.new_doc("Role")
            doc.role_name = role_name
            doc.desk_access = 1
            doc.insert(ignore_permissions=True)

def create_departments():
    departments = ["Naturopathy", "Ayurveda", "Yoga Therapy", "Physiotherapy", "Modern Medicine"]
    for dept_name in departments:
        if not frappe.db.exists("Medical Department", dept_name):
            doc = frappe.new_doc("Medical Department")
            doc.department = dept_name
            doc.insert(ignore_permissions=True)
