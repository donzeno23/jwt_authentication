from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
import jwt
import secrets
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

SECRET_KEY='a9cbf7dda1c1406f1bf77851bd715d333757dd795549247c287c8777f96ff083e2d180cd2d104b47b855a7a32851bde12db420572f63340952b5979b3f55f2db'
# REFRESH_TOKEN_SECRET='f582ee122d103373151acbb8fc053bc6c39eb83cd1ec7eb3e178f36b71b4b153b464907abbc8afbbd4816185909a87c2faeec523a4444756cd55219b6e4bf998'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 800

test_user = {
    "username": "temitope",
    "password": "temipassword",
    "email": "donzeno23@yahoo.com"
}

app = FastAPI()

security = HTTPBasic()

origins = {
    "http://localhost",
    "http://localhost:3000",
}

app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

class LoginItem(BaseModel):
    username: str
    password: str

    @app.get("/")
    def read_root():
     return {"Hello": "World"}

class RegisterItem(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    # government_org: bool
    address_1: str
    # address_2: str
    # city: str
    # state: str
    zip: int


    @app.get("/")
    def read_root():
     return {"Hello": "World"}


@app.post("/login")
async def user_login(loginitem:LoginItem):

    data = jsonable_encoder(loginitem)

    print(f'received username={data["username"]}')
    print(f'received password={data["password"]}')

    if data['username']== test_user['username'] and data['password']== test_user['password']:

        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {"roles": "admin", "accessToken": encoded_jwt}

    else:
        # TODO: handle server response (401: Unauthorized)
        # return {"message":"login failed"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )       
    

@app.post("/register")
async def user_registration(registeritem:RegisterItem):

    data = jsonable_encoder(registeritem)

    if data['email']== test_user['email'] and data['password']== test_user['password']:

        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {"accessToken": encoded_jwt}

    else:
        # return {"message":"registration failed"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    

if __name__ == '__main__':
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")