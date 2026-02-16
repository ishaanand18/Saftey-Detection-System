from flask import Flask, render_template, request, jsonify
import pickle 
import numpy as np
from chatbot import ChatBot

app=Flask(__name__)
chatbot = ChatBot()
model=pickle.load(open('model.pkl','rb'))
le_city=pickle.load(open('le_city.pkl','rb'))
le_gender=pickle.load(open('le_gender.pkl','rb'))

@app.route('/')
def home():
    return render_template("dashboard2.html")
# def index():
#     cities=le_city.classes_
#     genders=le_gender.classes_
#     return render_template('index1.html',cities=cities,genders=genders)

@app.route('/form')
def form():
    cities=le_city.classes_
    genders=le_gender.classes_
    return render_template('index.html',cities=cities,genders=genders)

@app.route('/predict',methods=['POST'])

def predict():
    city=request.form['city']
    # time_hour = int(request.form['time'])
    time_hour = int(request.form['time'].split(':')[0])
    age=int(request.form['age'])
    gender=request.form['gender']

    city_encoded=le_city.transform([city])[0]
    gender_encoded=le_gender.transform([gender])[0]

    input_data=np.array([[city_encoded,time_hour,age,gender_encoded]])
    prob=model.predict_proba(input_data)[0]

    return render_template('result.html',safe=round(prob[1]*100,2),unsafe=round(prob[0]*100,2),city=city,time_hour=time_hour,age=age,gender=gender)

@app.route('/test')
def test():
    return "Flask is Working"

@app.route('/chat', methods =['POST'])
def chat():
    user_msg = request.json.get('message')
    if not user_msg:
        return jsonify({'reply': "Sorry, I didn't get that."})
    
    reply = chatbot.get_response(user_msg)
    return jsonify({'reply': reply})

if __name__=='__main__':
    app.run(debug=True)

