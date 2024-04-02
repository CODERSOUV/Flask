###Integrating HTML using Flask
###HTTP VERBS - GET and POST
###Builidng URL dynamically

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is " + str(score)

###Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = "fail" if marks < 50 else "success"
    return redirect(url_for(result, score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    avg_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        avg_score=(science+maths+c+data_science)/4
        if avg_score<50:
            return redirect(url_for('success',score=avg_score))
        else:
            return redirect(url_for('success',score=avg_score))

if __name__ == '__main__':
    app.run(debug=True)
