# AI-Powered Second-Hand Trading Platform

## Activity 1.1 - User Account Management

This activity develops the user account management module for the AI-Powered Second-Hand Trading Platform. The module was developed from the class diagram and includes registration, login, personal information, forgot password, password hashing, and logout functionality.

## Project Description

The full project is a simple web-based second-hand trading platform that helps users buy and sell used items in a more organised way. It improves common informal trading problems such as poor searchability, unstructured listings, and limited item discovery.

The final platform will allow users to publish listings, browse items, submit purchase requests, and receive item recommendations. Administrators will manage users, listings, and platform activity.

## Current Module Features

### Home Page

The home route welcomes users and lists the available API routes.

### Sign Up

Users can create an account by entering:

- Full Name
- Date of Birth
- Email Address
- Password

The password is hashed before being stored.

### Login

Users can log in with their email and password. The system verifies the stored hashed password.

### User Profile

Users can view personal information such as:

- Full Name
- Date of Birth
- Email Address

### Forgot Password

Users can reset their password by verifying:

- Email Address
- Date of Birth

The new password is also hashed before being saved.

### Logout

The logout route confirms that the user has logged out.

## Functional Breakdown Based on Diagram

### 1. Home Module

Responsible for displaying the welcome message and available navigation routes.

### 2. Sign Up Module

Responsible for collecting user details, validating required fields, creating the account, and storing a hashed password.

### 3. Login Module

Responsible for checking the user email and verifying the password with the stored hash.

### 4. Forgot Password Module

Responsible for verifying the user by email and date of birth before allowing password reset.

### 5. Password Security Module

Responsible for hashing new passwords and verifying existing passwords using BCrypt.

### 6. User Profile Module

Responsible for displaying the saved user information without exposing the password.

## Project Structure

```text
activity 1.1/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── function_design.png
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   └── user_service.py
│
└── utils/
    ├── __init__.py
    └── password_utils.py
```

## How to Run

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Pylint Code Quality Check

Install Pylint if needed:

```bash
python -m pip install pylint
```

Run Pylint:

```bash
python -m pylint main.py database models services utils
```

## Future Development

The complete second-hand trading platform will include:

- Buyer module
- Seller listing module
- Admin management module
- AI item matching
- Personalized recommendations
- LLM-based search ranking
- Live deployment using free hosting or cloud services
