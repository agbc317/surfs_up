# Add Dependencies
from flask import Flask

# Create App
app = Flask(__name__)

# Create new app route /
@app.route('/')
def hello_world():
    return 'Hello world'
