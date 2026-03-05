# Arogyadhama Health

Custom Frappe app for **Arogyadhama Hospital Information Management System** — a 600-bed integrative medicine hospital at S-VYASA University, Bengaluru.

## Features

- **Diet Chart** — Naturopathy doctor prescribes 7-slot meal plans with dietary restrictions
- **Yoga Prescription** — Prescribed yoga practices with schedule, duration, and instructions
- **Treatment Schedule** — Specialized treatments (Acupuncture, Med Bath, Panchakarma, etc.) with session tracking
- **10 Custom Roles** — Patient, Facility Manager, Accountant, Intern, Naturopathy Doctor, Ayurveda Doctor, Therapist, Yoga Therapist Intern, Treatment Specialist, Admin
- **11 Hospital Sections** (A-K) — Auto-created as Healthcare Service Units
- **5 Medical Departments** — Naturopathy, Ayurveda, Yoga Therapy, Physiotherapy, Modern Medicine

## Requirements

- Frappe Framework >= 15.0.0
- ERPNext >= 15.0.0
- Marley Health (Healthcare module)

## Installation

```bash
bench get-app https://github.com/YOUR_USERNAME/arogyadhama_health
bench --site your-site install-app arogyadhama_health
```

## License

MIT
