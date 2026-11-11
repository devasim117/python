from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Temporary database
users_db = [
    {
        "name": "Asim",
        "id": 1,
        "email": "asim@gmail.com"
    }
]

# Request model
class User(BaseModel):
    name: str
    id: int
    email: str

# CREATE
@app.post("/user")
def create_user(data: User):
    user = data
    users_db.append(user.model_dump())
    return {"message" : "User created successfully", "user": data}

# USERS
@app.get("/users")
def get_users():
    return users_db
    
# Read single user
@app.get("/user/{id}")
def get_user(id: int):
    user = next((u for u in users_db if u.get("id") == id),None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found") 

    return user
    
# UPDATE
@app.put("/user/{id}")
def update_user(id: int, user: User):
    for index, existing_user in enumerate(users_db):
        if existing_user.get("id") == id:
            updated_data = user.model_dump()
            updated_data["id"] = id
            users_db[index] = updated_data
            return updated_data

    raise HTTPException(status_code=404, detail="User not found")

# Delete
@app.delete("/user/{id}")
def update_user(id: int):
    user = next((u for u in users_db if u.get("id") == id),None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.remove(user)
    return {"user deleted": user}