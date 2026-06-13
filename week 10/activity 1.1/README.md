# Login & Signup System

## Project Description
This project is a user account management system that includes login, signup, logout, personal information management, password hashing, and forgot password functionality.

## Main Features

### Home Page
Users can access the system and view their personal information after logging in.

### Sign Up
Users can create an account by entering:
- Full Name
- Date of Birth
- Email
- Password

The password is hashed before being saved for security.

### Login
Users log in using their email and password. The system validates the email and compares the entered password with the stored hashed password.

### Forgot Password
Users can reset their password by verifying:
- Email
- Date of Birth

After verification, the user can create a new password, which is hashed before saving.

### Logout
Users can safely log out of the system.

## Project Structure
```txt
project-folder/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── user.py
│
├── services/
│   ├── auth_service.py
│   └── user_service.py
│
└── database/
    └── database.py