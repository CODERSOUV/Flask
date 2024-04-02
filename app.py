from flask import Flask
### WSGI Application
app = Flask(__name__)
### Route to the root of the web application
@app.route('/')
def welcome():
    return "<h2>Welcome! Hello World!</h2>"
@app.route('/hello')
def hello():
    return "<h2>Hello, World!</h2>"
if __name__ == '__main__':
    app.run(debug=True)