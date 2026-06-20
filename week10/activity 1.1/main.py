"""FastAPI application for the Second-Hand Trading Platform user account module."""

from fastapi import FastAPI, HTTPException, status

from database.database import create_users_table
from models.user import ForgotPassword, UserLogin, UserSignup
from services.auth_service import login_user, reset_user_password
from services.user_service import create_user, get_user_by_email

app = FastAPI(
    title="Second-Hand Trading Platform - User Account Module",
    description="Week 10 Activity 1.1 for user registration, login, profile, and forgot password.",
    version="1.0.0",
)


@app.on_event("startup")
def startup_event():
    """Create required database tables when the application starts."""
    create_users_table()


@app.get("/")
def home():
    """Return a welcome message for the home page."""
    return {
        "message": "Welcome to the Second-Hand Trading Platform User Account Module",
        "available_routes": ["/signup", "/login", "/profile/{email}", "/forgot-password"],
    }


@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserSignup):
    """Register a new user with full name, date of birth, email, and password."""
    success = create_user(
        full_name=user.full_name,
        date_of_birth=user.date_of_birth,
        email=user.email,
        password=user.password,
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists. Please use another email.",
        )

    return {"message": "User account created successfully"}


@app.post("/login")
def login(user: UserLogin):
    """Login using email and password."""
    success = login_user(email=user.email, password=user.password)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    return {"message": "Login successful"}


@app.get("/profile/{email}")
def view_profile(email: str):
    """View a user's profile information by email."""
    user = get_user_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    return {
        "full_name": user["full_name"],
        "date_of_birth": user["date_of_birth"],
        "email": user["email"],
    }


@app.post("/forgot-password")
def forgot_password(data: ForgotPassword):
    """Reset password using email and date of birth verification."""
    success = reset_user_password(
        email=data.email,
        date_of_birth=data.date_of_birth,
        new_password=data.new_password,
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or date of birth does not match.",
        )

    return {"message": "Password reset successful"}


@app.get("/logout")
def logout():
    """Return logout confirmation message."""
    return {"message": "Logout successful"}
