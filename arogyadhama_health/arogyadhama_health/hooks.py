app_name = "arogyadhama_health"
app_title = "Arogyadhama Health"
app_publisher = "Abinash - SVE Group"
app_description = "Hospital Information Management System for Arogyadhama - S-VYASA University, Bengaluru"
app_email = "admin@arogyadhama.com"
app_license = "MIT"
app_version = "0.1.0"

# Required Apps
required_apps = ["frappe", "erpnext"]

# App Icon (shown in Desk)
app_icon = "octicon octicon-heart"
app_color = "#1B4332"

# Fixtures - data that gets exported/imported with the app
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "Arogyadhama Health"]]
    },
    {
        "doctype": "Property Setter",
        "filters": [["module", "=", "Arogyadhama Health"]]
    },
    {
        "doctype": "Role",
        "filters": [["name", "in", [
            "Naturopathy Intern",
            "Naturopathy Doctor",
            "Ayurveda Doctor",
            "Therapist",
            "Yoga Therapist Intern",
            "Treatment Specialist",
            "Facility Manager",
            "Arogyadhama Admin",
        ]]]
    }
]

# Website
website_route_rules = [
    {"from_route": "/book-appointment", "to_route": "book_appointment"},
    {"from_route": "/patient-portal", "to_route": "patient_portal"},
    {"from_route": "/aftercare", "to_route": "aftercare"},
]

# DocType Events
doc_events = {
    "Patient": {
        "after_insert": "arogyadhama_health.arogyadhama_health.events.patient.after_insert",
    },
    "Patient Encounter": {
        "on_submit": "arogyadhama_health.arogyadhama_health.events.encounter.on_submit",
    },
}

# Scheduled Tasks
# scheduler_events = {
#     "daily": [
#         "arogyadhama_health.arogyadhama_health.tasks.daily.send_therapy_reminders"
#     ],
# }

# Jinja template extensions
# jinja = {
#     "methods": [],
#     "filters": [],
# }

# Installation
after_install = "arogyadhama_health.arogyadhama_health.setup.install.after_install"

# App includes in desk
app_include_css = "/assets/arogyadhama_health/css/arogyadhama.css"
# app_include_js = "/assets/arogyadhama_health/js/arogyadhama.js"
