"""Pydantic models for user account requests."""

from pydantic import BaseModel, EmailStr, Field


class UserSignup(BaseModel):
    """Request model for user registration."""

    full_name: str = Field(..., min_length=2, description="User's full name")
    date_of_birth: str = Field(..., description="User's date of birth")
    email: EmailStr
    password: str = Field(..., min_length=6, description="User password")


class UserLogin(BaseModel):
    """Request model for user login."""

    email: EmailStr
    password: str = Field(..., min_length=6)


class ForgotPassword(BaseModel):
    """Request model for resetting a forgotten password."""

    email: EmailStr
    date_of_birth: str
    new_password: str = Field(..., min_length=6)
