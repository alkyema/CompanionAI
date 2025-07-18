from fastapi import FastAPI, Request, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

# from Appliance import Appliance_Reading,Appliance_writing
# from Sensor_Data import fetch_latest_data,get_all_data,get_temperature_stats
# from Wheather_Data_Retrive import weather_Daily,weather_Weekly,getaverage_weather_Temperature
from login_and_sign_up import check,New_User,changePassword
# from Mail_Sending import GenerateMail,verifyOTP
# from PassGenerator import Token_check,New_Token
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
    allow_origins=["*"],  # Replace with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Server": "Ready"}


@app.get("/Applicances_data")
# def Applicances_data(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("Applicances_data_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return Appliance_Reading()


# @app.get("/tempAverage")
# def tempAverage(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("tempAverage_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return get_temperature_stats()


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


# @app.get("/wheather_daily")
# def wheather_daily(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("wheather_daily_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return weather_Daily()


# @app.get("/wheather_weekly")
# def wheather_weekly(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("wheather_weekly_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return weather_Weekly()


# @app.get("/Average_Temp_Day")
# def Average_Temp_Day(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("Average_Temp_Day_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return getaverage_weather_Temperature()


# @app.get("/all_sensor_report")
# def sensor_report(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("sensor_report_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return get_all_data()


# @app.get("/fetch_sensor_data")
# def sensor_data(token: str = Depends(oauth2_scheme)):
#     if token != os.getenv("sensor_data_Token"):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     else:
#         return fetch_latest_data()


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
    
    
class genOTP(BaseModel):
    Email: str

@app.post("/generateOTP")
def generateOTP(genOTP: genOTP, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("generateOTP_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(genOTP.Email)
        ret = GenerateMail(genOTP.Email)
        print(ret)
        return ret
    
    
class verOTP(BaseModel):
    verOTP: str

@app.post("/OTPverify")
def OTPverify(verOTP: verOTP, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("verifyOTP_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(verOTP.verOTP)
        ret = verifyOTP(verOTP.verOTP)
        print(ret)
        return ret
    
    
class Tokenclass(BaseModel):
    UserID: str

@app.post("/generateToken")
def generateToken(Tokenclass: Tokenclass, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("generateToken_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(Tokenclass.UserID)
        ret = New_Token(Tokenclass.UserID)
        print(ret)
        return ret


class Tokencheck(BaseModel):
    Token: str

@app.post("/checkToken")
def checkToken(Tokencheck: Tokencheck, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("verifyToken_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(Tokencheck.Token)
        ret = Token_check(Tokencheck.Token)
        print(ret)
        return ret
    
class genOTP(BaseModel):
    Email: str

@app.post("/forgotPasswordMail")
def forgotPasswordMail(genOTP: genOTP, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("forgotpassword_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(genOTP.Email)
        ret = forgotPassword(genOTP.Email)
        print(ret)
        return ret
    
class new_pass(BaseModel):
    Email: str
    Password: str

@app.post("/PasswordChange")
def PasswordChange(new_pass: new_pass, request: Request,token: str = Depends(oauth2_scheme)):
    if token != os.getenv("changedpassword_Token"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print((new_pass.Email,new_pass.Password))
        ret = changePassword(new_pass.Email,new_pass.Password)
        return ret
    