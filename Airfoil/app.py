from flask import Flask, jsonify, request, url_for,render_template
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data=[list(data.values())]
    prediction = model.predict(new_data)[0]
    return jsonify(prediction)

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final=[np.array(data)]
    print(data)
    output=model.predict(final)[0]
    print(output)
    return render_template('home.html',prediction_text="The predicted value is {}".format(output))

if __name__ == '__main__':
    app.run(debug=True)