from fastapi import FastAPI, Request, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from login_and_sign_up import check,New_User,changePassword
from generate import generate_response

import dotenv
dotenv.load_dotenv()
import os
import datetime

# Create an instance of FastAPI
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Server": "Ready"}

class toogle(BaseModel):
    Appliance_name: str
called = False
@app.post("/apptoogle")
def apptoogle(toogle: toogle, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("apptoogle_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        global called
        if(called):
            return 
        else:
            print((toogle.Appliance_name))
            ret = generate_response(toogle.Appliance_name)
            print(ret)
            called = False
        return ret


class login_cred(BaseModel):
    userID: str
    Password: str

@app.post("/login")
def login(login_cred: login_cred, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("login_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print((login_cred.userID,login_cred.Password))
        ret = check(login_cred.userID,login_cred.Password)
        print(ret)
        return ret
    
class Register_User(BaseModel):
    Username: str
    Password: str
    Email: str
    Contact:str

@app.post("/singup")
def singup(Register_User: Register_User, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("singup_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        Date_Created = datetime.datetime.now().date()
        LastLoggedIN = datetime.datetime.now().date()
        print(Register_User.Username,Register_User.Password,Register_User.Email,Register_User.Contact,Date_Created,LastLoggedIN)
        ret = New_User(Register_User.Username,Register_User.Password,Register_User.Email,Register_User.Contact,Date_Created,LastLoggedIN)
        print(ret)
        return ret
    
