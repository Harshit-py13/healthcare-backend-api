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

🚀 Getting Started
🧱 Prerequisites

Python 3.13.7
PostgreSQL
Git

⚙️ Installation

1️⃣ Clone the repository
git clone https://github.com/Harshit-py13/healthcare-backend-api.git
cd healthcare-backend-api

2️⃣ Create and activate a virtual environment
python -m venv env
Windows:
env\Scripts\activate

Mac/Linux:
source env/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🛡️ Environment Variables Setup

Create a .env file in the root directory and add your PostgreSQL + Django settings.

Example:

SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432

You can use .env.example as a reference.

🗄️ Database Migration

Run migrations:
python manage.py makemigrations
python manage.py migrate

▶️ Run the Server
python manage.py runserver

Server will run at:
http://127.0.0.1:8000/

🔐 Authentication (JWT)
Register User

POST
/api/auth/register/

Login User

POST
/api/auth/login/

After login, copy the access token and include it in headers:
Authorization: Bearer <your_access_token>

📮 API Endpoints
| Method | Endpoint                      | Description                                    | Auth Required |
| ------ | ----------------------------- | ---------------------------------------------- | ------------- |
| POST   | `/api/auth/register/`         | Register a new user                            | ❌             |
| POST   | `/api/auth/login/`            | Login and get JWT token                        | ❌             |
| POST   | `/api/patients/`              | Add a new patient                              | ✅             |
| GET    | `/api/patients/`              | Get all patients created by authenticated user | ✅             |
| GET    | `/api/patients/<id>/`         | Get details of a patient                       | ✅             |
| PUT    | `/api/patients/<id>/`         | Update patient details                         | ✅             |
| DELETE | `/api/patients/<id>/`         | Delete patient record                          | ✅             |
| POST   | `/api/doctors/`               | Add a new doctor                               | ✅             |
| GET    | `/api/doctors/`               | Retrieve all doctors                           | ❌             |
| GET    | `/api/doctors/<id>/`          | Get doctor details                             | ❌             |
| PUT    | `/api/doctors/<id>/`          | Update doctor details                          | ✅             |
| DELETE | `/api/doctors/<id>/`          | Delete doctor record                           | ✅             |
| POST   | `/api/mappings/`              | Assign a doctor to a patient                   | ✅             |
| GET    | `/api/mappings/`              | Retrieve all patient-doctor mappings           | ✅             |
| GET    | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient              | ✅             |
| DELETE | `/api/mappings/<id>/`         | Remove a doctor from patient                   | ✅             |


🧪 Testing APIs

You can test all APIs using:
Thunder Client (VS Code Extension)
Postman

🧑‍💻 Author

Harshit Tiwari
GitHub: @Harshit-py13

Made with 🐍 Django & ❤️ for Healthcare Security.
