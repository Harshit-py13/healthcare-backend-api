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
```
---

🚀 Getting Started

🧱 Prerequisites

- Python 3.13.7

- PostgreSQL

- pip

- Git

⚙️ Installation
```text
# Clone the Repository
git clone https://github.com/Harshit-py13/healthcare-backend-api.git
cd healthcare-backend-api

# Create and Activate Virtual Environment
python -m venv env
env\Scripts\activate       # Windows
# source env/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```
---

🗝️ Configure Environment Variables

Create a .env file in the root directory and add your PostgreSQL credentials.

Use .env.example as reference.
```text
# .env.example
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser (Optional)
python manage.py createsuperuser

# Start the Server
python manage.py runserver

# Server will run at:
  http://127.0.0.1:8000/
```
---

🔐 Authentication (JWT)
Register

POST /api/auth/register/

```text
{
  "name": "Harshit Tiwari",
  "email": "harshit@gmail.com",
  "password": "Har@#4321"
}
```

Login

POST /api/auth/login/

```text
Request Body
{
  "email": "harshit@gmail.com",
  "password": "Har@#4321"
}
```

📌 Use Token in Headers for Protected APIs
 ```text  Authorization: Bearer <access_token> ```

---

📮 API Endpoints

| Method | Endpoint                             | Description                      | Auth |
| ------ | ------------------------------------ | -------------------------------- | ---- |
| POST   | `/api/auth/register/`                | Register new user                | ❌    |
| POST   | `/api/auth/login/`                   | Login and get JWT token          | ❌    |
| POST   | `/api/patients/`                     | Add a new patient                | ✅    |
| GET    | `/api/patients/`                     | List all patients                | ✅    |
| GET    | `/api/patients/<id>/`                | View patient details             | ✅    |
| PUT    | `/api/patients/<id>/`                | Update patient details           | ✅    |
| DELETE | `/api/patients/<id>/`                | Delete patient                   | ✅    |
| POST   | `/api/doctors/`                      | Add a doctor                     | ✅    |
| GET    | `/api/doctors/`                      | Get all doctors                  | ✅    |
| GET    | `/api/doctors/<id>/`                 | View doctor details              | ✅    |
| PUT    | `/api/doctors/<id>/`                 | Update doctor info               | ✅    |
| DELETE | `/api/doctors/<id>/`                 | Delete doctor                    | ✅    |
| POST   | `/api/mappings/`                     | Assign doctor to patient         | ✅    |
| GET    | `/api/mappings/`                     | View all mappings                | ✅    |
| GET    | `/api/mappings/<patient_id>/`        | View doctors assigned to patient | ✅    |
| DELETE | `/api/mappings/delete/<mapping_id>/` | Remove doctor-patient mapping    | ✅    |

---

🛡️ Admin Panel

📌 Django Admin:

 ```text http://127.0.0.1:8000/admin/ ```

Login using your superuser credentials.

---

🌍 Environment Variables

Your .env file should contain:
 ```text
 SECRET_KEY=your-secret-key
 DEBUG=True

 DB_NAME=healthcare_db
 DB_USER=postgres
 DB_PASSWORD=your_password
 DB_HOST=127.0.0.1
 DB_PORT=5432
 ```

---

✨ Future Enhancements

✅ Swagger / ReDoc API Documentation 

✅ Role-based Access (Admin / Doctor / User) 

✅ Pagination & Filtering

✅ Email Verification

✅ Docker Support

---

👨‍💻 Author

Harshit Tiwari
GitHub: Harshit-py13





