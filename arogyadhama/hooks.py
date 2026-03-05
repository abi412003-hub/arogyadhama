app_name = "arogyadhama"
app_title = "Arogyadhama Health"
app_publisher = "Abinash - SVE Group"
app_description = "Hospital Information Management System for Arogyadhama"
app_email = "admin@arogyadhama.com"
app_license = "MIT"
app_version = "0.1.0"

required_apps = ["frappe", "erpnext"]

app_icon = "octicon octicon-heart"
app_color = "#1B4332"

fixtures = [
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

after_install = "arogyadhama.arogyadhama.setup.install.after_install"
