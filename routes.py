from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from .models import OrgCreate
from .database import orgs_collection

router = APIRouter()
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/org/create")
async def create_org(data: OrgCreate):

    existing = await orgs_collection.find_one({"email": data.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    doc = {
        "organization_name": data.organization_name,
        "email": data.email,
        "password": pwd_ctx.hash(data.password)
    }

    await orgs_collection.insert_one(doc)

    return {"message": "Organization created successfully"}
