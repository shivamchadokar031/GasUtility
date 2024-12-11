# Gas Utility Management System

## Overview
The Gas Utility Management System is a Django-based web application that allows users to:
- Login and manage their accounts.
- Submit and track service requests (e.g., installation, repair, inspection).
- View detailed statuses and updates on their requests.

This application is designed to streamline utility service management and provide a user-friendly interface for both customers and administrators.

---

## Features
1. **User Authentication**
   - Login and Logout functionality using Django's built-in authentication system.

2. **Dashboard**
   - Displays all service requests submitted by the logged-in user.
   - Links to create new service requests and view request details.

3. **Service Request Management**
   - Create service requests with details and optional file attachments.
   - Track the status of each request (e.g., Pending, Resolved).

4. **Admin Panel**
   - Manage users and service requests from Django's admin interface.

---

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.7)
- Django (>=4.0)

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/gas-utility-management.git
   cd gas-utility-management
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

### **1. User Login**
   - Navigate to the login page: [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/).
   - Use the credentials created via the Django admin panel or sign up if implemented.

### **2. Dashboard**
   - After logging in, users can view a list of their service requests.
   - Links to create new requests or view detailed information are available.

### **3. Submit a Service Request**
   - Navigate to "New Service Request" from the dashboard.
   - Fill in the required details (service type, description, file attachments).
   - Submit the request.

### **4. View Service Request Details**
   - Click on a request from the dashboard to view detailed information.
   - Includes request type, status, and any attached files.

### **5. Admin Panel**
   - Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
   - Manage users, service requests, and other data models.

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.


