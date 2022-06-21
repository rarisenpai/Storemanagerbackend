from werkzeug.security import generate_password_hash, check_password_hash

users = [
    {"admin": generate_password_hash("admin")},
    {"attendant": generate_password_hash("attendant")}
]

roles = [
    {"admin": "admin"},
    {"attendant": "attendant"}
]