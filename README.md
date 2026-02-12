# 🏥 Healthcare Backend API

A secure and scalable backend system for managing patients, doctors, and their assignments — built using Django, Django REST Framework, and PostgreSQL, with robust JWT Authentication.

---

## 📦 Features

- ✅ User Registration & Login (JWT-based authentication)
- ✅ Stateless Authentication using `djangorestframework-simplejwt`
- ✅ Full CRUD for Patients
- ✅ Full CRUD for Doctors
- ✅ Patient-Doctor Mapping (Assign doctors to patients)
- ✅ PostgreSQL database integration
- ✅ Environment-based configuration using `.env` and `python-decouple`

---

## 📁 Project Structure

```text
HealthCare/
├── accounts/            # User Auth & JWT logic
├── doctors/             # Doctor management
├── patients/            # Patient management
├── mappings/            # Doctor-Patient relationship logic
├── health/              # Core Project settings (settings.py, urls.py)
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
├── manage.py            # Django CLI
└── README.md            # Project documentation
...
---

🚀 Getting Started
🧱 Prerequisites
Python 3.13.7
PostgreSQL
pip
Git

⚙️ Installation
# Clone the Repository
git clone https://github.com/Harshit-py13/healthcare-backend-api.git
cd healthcare-backend-api

# Create and Activate Virtual Environment
python -m venv env
env\Scripts\activate       # Windows
# source env/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

