from flask import *
import pyrebase
config={
    "apiKey": "AIzaSyDTNTLgsL4EYfJpXyqC8WhagKEy_dxIXjo",
    "authDomain": "beproj-f43fe.firebaseapp.com",
    "projectId": "beproj-f43fe",
    "storageBucket": "beproj-f43fe.appspot.com",
    "messagingSenderId": "689655457757",
    "appId": "1:689655457757:web:231bc14dc42cce379db834",
    "measurementId": "G-PR69M3LNGF",
    "databaseURL":""
}
firebase=pyrebase.initialize_app(config)
app= Flask(__name__)
auth=firebase.auth()
db=firebase.database()
from application import routes
