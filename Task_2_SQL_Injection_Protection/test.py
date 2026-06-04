from security import encrypt_data
from validator import detect_sql_injection
#Testing Encryption
print(
    encrypt_data("abcdef123")
)
#Testing Validator
print(
    detect_sql_injection(
        "admin' OR 1=1 --"
    )
)
from validator import detect_sql_injection

print(
    detect_sql_injection(
        "admin' OR 1=1 --"
    )
)

print(
    detect_sql_injection(
        "aman"
    )
)
