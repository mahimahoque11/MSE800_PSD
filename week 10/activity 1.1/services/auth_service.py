"""Authentication service functions for login and password reset."""

from services.user_service import get_user_by_email, update_password
from utils.password_utils import verify_password


def login_user(email: str, password: str) -> bool:
    """Validate a user's login credentials."""
    user = get_user_by_email(email)

    if user is None:
        return False

    return verify_password(password, user["password"])


def reset_user_password(email: str, date_of_birth: str, new_password: str) -> bool:
    """Reset password after verifying email and date of birth."""
    user = get_user_by_email(email)

    if user is None or user["date_of_birth"] != date_of_birth:
        return False

    return update_password(email, new_password)
