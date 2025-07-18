import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import dotenv
dotenv.load_dotenv()
import os
import json

SERVICE_ACCOUNT_INFO = json.loads(os.getenv("GDrive_SERVICE_ACCOUNT_INFO"))


cred = credentials.Certificate(SERVICE_ACCOUNT_INFO)

firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("databaseURL") 
})

# Initialize Firestore DB
db = firestore.client()

print("Connected to Firebase")