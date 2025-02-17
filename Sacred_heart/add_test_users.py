from sacred_heart import app
from models import User, db

with app.app_context():
    db.create_all()  # Ensure tables exist

    # Add test users (replace passwords as needed)
    users = [
        {"username": "dr_minyard", "password": "password123", "role": "doctor"},
        {"username": "dr_davis", "password": "securepass", "role": "doctor"},
        {"username": "dr_green", "password": "securepass", "role": "doctor"},
        {"username": "dr_miller", "password": "securepass", "role": "doctor"},
        {"username": "dr_clark", "password": "securepass", "role": "doctor"},
        {"username": "admin", "password": "adminpass", "role": "admin"}
    ]

    for user_data in users:
        user = User.query.filter_by(username=user_data["username"]).first()
        if not user:  # Only add if user doesn't exist
            user = User(username=user_data["username"], role=user_data["role"])
            user.set_password(user_data["password"])  # Hash password
            db.session.add(user)

    db.session.commit()
    print("Test users added.")
