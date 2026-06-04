from fastapi import FastAPI
from database import SessionLocal, engine
from models import User, Base
from validator import detect_sql_injection
from security import encrypt_data

Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "SQL Injection Protection System"
    }
@app.post("/register")
def register_user(
    username: str,
    email: str,
    password: str
):
    try:

        print("STEP 1")

        db = SessionLocal()

        print("STEP 2")

        if detect_sql_injection(username):

            print("STEP 3")

            return {

                "status": "Blocked",

                "reason": "SQL Injection Detected"

            }

        print("STEP 4")

        encrypted_password = encrypt_data(password)

        print("STEP 5")

        user = User(

            username=username,

            email=email,

            encrypted_password=encrypted_password

        )

        print("STEP 6")

        db.add(user)

        print("STEP 7")

        db.commit()

        print("STEP 8")

        db.close()

        return {

            "status": "Success"

        }

    except Exception as e:

        print("ERROR:", e)

        return {

            "error": str(e)

        }
    # print("Function Started")
    # db = SessionLocal()
    # print("Database Connected")
    # # Layer 1 Security
    # if detect_sql_injection(username):
    #     db.close()
    #     return {
    #         "status": "Blocked",
    #         "reason": "SQL Injection Detected"
    #     }
    # # Check existing user
    # existing_user = db.query(User).filter(
    #     User.email == email
    # ).first()
    # if existing_user:
    #     db.close()
    #     return {
    #         "status": "Rejected",
    #         "reason": "Email Already Exists"
    #     }
    # # Layer 2 Security
    # encrypted_password = encrypt_data(
    #     password
    # )
    # user = User(
    #     username=username,
    #     email=email,
    #     encrypted_password=encrypted_password
    # )
    # db.add(user)
    # db.commit()
    # db.close()
    # return {
    #     "status": "Success",
    #     "message": "User Registered Securely"
    # }