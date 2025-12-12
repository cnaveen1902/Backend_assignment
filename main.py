# -----------------------------------------
#   FastAPI Backend (GitHub Version)
#   Replace secrets before using
# -----------------------------------------

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import motor.motor_asyncio
from passlib.context import CryptContext

# ❗ IMPORTANT: Replace these with placeholders for GitHub
MONGO_URI = "YOUR_MONGO_URI_HERE"
JWT_SECRET = "YOUR_SECRET_KEY"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["master_db"]
orgs = db["organizations"]

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(title="Assignment Backend")

class OrgCreate(BaseModel):
    organization_name: str
    email: EmailStr
    password: str

@app.post("/org/create")
async def create_org(data: OrgCreate):
    # check if email exists
    if await orgs.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = pwd_ctx.hash(data.password)

    doc = {
        "organization_name": data.organization_name,
        "email": data.email,
        "password": hashed_pw
    }

    await orgs.insert_one(doc)
    return {"message": "Organization created"}
