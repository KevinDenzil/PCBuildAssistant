from flask import Flask,redirect,url_for,render_template,request,jsonify,Response
from chat import get_response
from PCBuilderWithBudget import *
from PCPartsFinderWithBudget import *
import json

bknd=Flask(__name__,template_folder='templates')
@bknd.get("/")
def home():
    return render_template("index.html")
@bknd.post("/predict")
def predict():
    text=request.get_json().get("message")
    func=request.get_json().get("func")
    arg=request.get_json().get("arg")
    
    print(func)
    response = ""
    if(func == "getStartingPrice"):
        response = getStartingPrice(arg, text)
    elif(func == "getEndingPrice"):
        response = getEndingPrice(arg, text)
    elif(func=="calculatePrice"):
        response = calculatePrice(arg, text)
    elif(func == "calculatePCPrice"):
        response = calculatePCPrice(arg, text)
    else:
        response = get_response(text)
    print(response, "response")
    res = json.loads(response)
    message={"answer": res["response"], "func": res["func"], "arg": res["arg"]}
    return jsonify(message)

    




if __name__=="__main__":
    bknd.run(debug=True)
