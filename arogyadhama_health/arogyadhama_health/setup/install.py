import frappe


def after_install():
    """Run after app installation - create default data."""
    create_roles()
    create_sections()
    create_departments()
    frappe.db.commit()
    print("Arogyadhama Health: Setup complete!")


def create_roles():
    """Create Arogyadhama-specific roles."""
    roles = [
        {"role_name": "Naturopathy Intern", "desk_access": 1},
        {"role_name": "Naturopathy Doctor", "desk_access": 1},
        {"role_name": "Ayurveda Doctor", "desk_access": 1},
        {"role_name": "Therapist", "desk_access": 1},
        {"role_name": "Yoga Therapist Intern", "desk_access": 1},
        {"role_name": "Treatment Specialist", "desk_access": 1},
        {"role_name": "Facility Manager", "desk_access": 1},
        {"role_name": "Arogyadhama Admin", "desk_access": 1},
    ]
    for role in roles:
        if not frappe.db.exists("Role", role["role_name"]):
            doc = frappe.new_doc("Role")
            doc.role_name = role["role_name"]
            doc.desk_access = role["desk_access"]
            doc.insert(ignore_permissions=True)
            print(f"  Created role: {role['role_name']}")


def create_sections():
    """Create the 11 hospital sections (A through K) as Healthcare Service Units."""
    sections = [
        ("Section A", "Ward"),
        ("Section B", "Ward"),
        ("Section C", "Ward"),
        ("Section D", "Ward"),
        ("Section E", "Ward"),
        ("Section F", "Ward"),
        ("Section G", "Ward"),
        ("Section H", "Ward"),
        ("Section I", "Ward"),
        ("Section J", "Ward"),
        ("Section K", "Ward"),
    ]

    # First ensure the parent service unit type exists
    if not frappe.db.exists("Healthcare Service Unit Type", "Ward"):
        doc = frappe.new_doc("Healthcare Service Unit Type")
        doc.service_unit_type = "Ward"
        doc.allow_appointments = 0
        doc.inpatient_occupancy = 1
        doc.insert(ignore_permissions=True)
        print("  Created service unit type: Ward")

    # Create root unit if not exists
    root_name = "Arogyadhama"
    if not frappe.db.exists("Healthcare Service Unit", root_name):
        doc = frappe.new_doc("Healthcare Service Unit")
        doc.healthcare_service_unit_name = root_name
        doc.is_group = 1
        doc.company = frappe.defaults.get_defaults().get("company", "Arogyadhama")
        doc.insert(ignore_permissions=True)
        print(f"  Created root unit: {root_name}")

    # Create section units
    for section_name, unit_type in sections:
        if not frappe.db.exists("Healthcare Service Unit", section_name):
            doc = frappe.new_doc("Healthcare Service Unit")
            doc.healthcare_service_unit_name = section_name
            doc.parent_healthcare_service_unit = root_name
            doc.service_unit_type = unit_type
            doc.is_group = 1
            doc.company = frappe.defaults.get_defaults().get("company", "Arogyadhama")
            doc.insert(ignore_permissions=True)
            print(f"  Created section: {section_name}")


def create_departments():
    """Create Arogyadhama medical departments."""
    departments = [
        "Naturopathy",
        "Ayurveda",
        "Yoga Therapy",
        "Physiotherapy",
        "Modern Medicine",
    ]
    for dept_name in departments:
        if not frappe.db.exists("Medical Department", dept_name):
            doc = frappe.new_doc("Medical Department")
            doc.department = dept_name
            doc.insert(ignore_permissions=True)
            print(f"  Created department: {dept_name}")
