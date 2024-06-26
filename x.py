###Builidng URL dynamically

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome! Hello World!"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is " + str(score)

@app.route('/fail/<int:score>')
def failx(score):
    return "The person has failed and the score is " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = "fail" if marks < 50 else "success"
    return redirect(url_for(result, score=marks))

if __name__ == '__main__':
    app.run(debug=True)
