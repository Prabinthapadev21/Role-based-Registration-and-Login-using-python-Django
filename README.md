# Role Based Login System (Django)

A simple **Role Based Registration and Login System** built using **Django**. This project allows users to register and log in with different roles such as **Admin**, **Employee**, and **Customer**, and redirects them to their respective dashboards.

This project is designed for **beginners** and follows clean and understandable Django practices.

---

## 🚀 Features

* User Registration
* User Login & Logout
* Role-based authentication
* Separate dashboards for:

  * Admin
  * Employee
  * Customer
* Django Forms for validation
* CSRF protection enabled
* Clean and simple UI

---

## 🛠️ Technologies Used

* Python 3
* Django
* HTML
* CSS
* SQLite (default Django database)

---

## 📁 Project Structure

```
Role_based_login_system/
│
├── account/
│   ├── migrations/
│   ├── templates/
│   │   ├── accounts/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── roles/
│   │       ├── admin.html
│   │       ├── employee.html
│   │       └── customer.html
│   │
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   └── base.html
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd Role_based_login_system
```

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. Open browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🔐 User Roles

During registration, users can choose one of the following roles:

* **Admin** → Access Admin Dashboard
* **Employee** → Access Employee Page
* **Customer** → Access Customer Page

Each role has its own HTML template and access logic.

---

## 📸 Screens Included

* Login Page
* Registration Page
* Admin Dashboard
* Employee Page
* Customer Page

---

## 🎯 Learning Outcomes

* Understanding Django authentication
* Using Django Forms
* Role-based access control
* Template inheritance
* Project structuring

---

## 📌 Future Improvements

* Password reset functionality
* Profile page
* Email verification
* Better UI using Bootstrap or Tailwind
* Permissions using Django Groups

---

## 👨‍💻 Author

**Prabin Thapa**
BCA Student | Django Learner

---

## 📄 License

This project is for **learning purposes**. You are free to use and modify it.

---

⭐ If you like this project, don't forget to star the repository!
