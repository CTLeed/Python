from flask import Flask
from flask import session

DATABASE = "login_reg_db"

app = Flask(__name__)
app.secret_key = "It's the one that says BAD M F'er on it"
