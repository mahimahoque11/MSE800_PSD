"""User service functions for account creation and profile management."""

import sqlite3
from typing import Optional

from database.database import get_connection
from utils.password_utils import hash_password


def create_user(full_name: str, date_of_birth: str, email: str, password: str) -> bool:
    """Create a new user account and return True if successful."""
    hashed_password = hash_password(password)

    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO users (full_name, date_of_birth, email, password)
                VALUES (?, ?, ?, ?)
                """,
                (full_name, date_of_birth, email, hashed_password),
            )
            connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def get_user_by_email(email: str) -> Optional[sqlite3.Row]:
    """Return a user record by email, or None if not found."""
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()


def update_password(email: str, new_password: str) -> bool:
    """Update a user's password after hashing it."""
    hashed_password = hash_password(new_password)

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE users SET password = ? WHERE email = ?",
            (hashed_password, email),
        )
        connection.commit()
        return cursor.rowcount > 0
