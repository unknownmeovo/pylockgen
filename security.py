import os
def is_breached(password: str, user_db: str = None) -> bool:
    """
    Check if the password exists in the default or user-provided breach database.
    
    Args:
        password (str): The password to check.
        user_db (str): Optional path to a user-provided text file with weak passwords.
    Returns:
        bool: True if the password is found, False otherwise.
    """
    default_file = os.path.join(os.path.dirname(__file__), "weak_passwords.txt")

    # Check default database
    try:
        with open(default_file, "r", encoding="utf-8") as f:
            if password in {line.strip() for line in f}:
                return True
    except FileNotFoundError:
        pass

    # Check user-provided database
    if user_db:
        try:
            with open(user_db, "r", encoding="utf-8") as f:
                if password in {line.strip() for line in f}:
                    return True
        except FileNotFoundError:
            pass

    return False

def check_breach(password: str, user_db: str = None) -> str:
    return (
        "❌ Found in breached password list"
        if is_breached(password, user_db)
        else "✅ Not found in breached password list"
    )

