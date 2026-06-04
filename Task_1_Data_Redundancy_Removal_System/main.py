from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Customer, Base
from validator import check_name_similarity
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home Route
@app.get("/")
def home():
    return {
        "message": "Data Redundancy Removal System"
    }
#Add Customer
@app.post("/customer")
def add_customer(
    name: str,
    email: str,
    phone: str
):
    db = SessionLocal()
    # Exact duplicate check
    existing_customer = db.query(Customer).filter(
        Customer.email == email,
        Customer.phone == phone
    ).first()
    if existing_customer:
        return {
            "status": "Rejected",
            "reason": "Duplicate Record Found"
        }
    all_customers = db.query(Customer).all()
    for customer in all_customers:
        similarity = check_name_similarity(
            customer.name,
            name
        )
        if similarity > 90:
            return {
                "status": "Possible Duplicate",
                "existing_name": customer.name,
                "similarity_score": similarity
            }
    # Insert new customer
    customer = Customer(
        name=name,
        email=email,
        phone=phone
    )
    db.add(customer)
    db.commit()
    db.close()
    return {
        "status": "Success",
        "message": "Customer Added"
    }
# View Customers
@app.get("/customers")
def get_customers():

    db = SessionLocal()

    customers = db.query(Customer).all()

    result = []

    for customer in customers:

        result.append({
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone
        })

    return result