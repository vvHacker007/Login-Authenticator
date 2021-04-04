from flask import Flask,render_template,session,redirect
from functools import wraps
import pymongo as pm
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
# Database
client = pm.MongoClient(os.getenv('MONGO_CLIENT'))
db = client.Login_signup

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')