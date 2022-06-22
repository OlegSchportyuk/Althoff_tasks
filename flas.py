from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Привет, Pandil!'
app.run(port='8000')
