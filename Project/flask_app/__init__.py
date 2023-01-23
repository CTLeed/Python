from flask import Flask
from flask import session
app = Flask(__name__)
app.secret_key = "It's the one that says BAD M F'er on it"
DATABASE = "banking_db"
