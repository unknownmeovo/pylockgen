import os

def is_breached(password: str, custom_db: str = None, use_default: bool = True) -> bool:
    """
    Check if a password is in the breached database.

    Args:
        password (str): Password to check.
        custom_db (str, optional): Path to a custom database file (one password per line).
        use_default (bool, optional): Whether to use the default weak_passwords.txt. Default = True.

    Returns:
        bool: True if password is found in a database, False otherwise.
    """

    # Default weak password list file
    default_file = os.path.join(os.path.dirname(__file__), "weak_passwords.txt")

    # Collect all breached passwords
    breached = set()

    # Load default file if enabled
    if use_default and os.path.exists(default_file):
        with open(default_file, "r", encoding="utf-8") as f:
            breached.update(line.strip() for line in f)

    # Load custom database if provided
    if custom_db and os.path.exists(custom_db):
        with open(custom_db, "r", encoding="utf-8") as f:
            breached.update(line.strip() for line in f)

    return password in breached
