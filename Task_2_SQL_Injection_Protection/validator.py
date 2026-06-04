def detect_sql_injection(text):
    dangerous_patterns = [
        "' OR 1=1",
        "DROP TABLE",
        "DELETE FROM",
        "--",
        ";",
        "UNION SELECT"
    ]

    text = text.upper()

    for pattern in dangerous_patterns:

        if pattern.upper() in text:
            return True

    return False