import pickle
from flask import Flask, request
#Model loading
# model_pickle=open("C:\Users\MAYUR\OneDrive\Desktop\repo_clone\practice-\artifacts\logistic_model.pkl","rb")
model_pickle = open("./artifacts/logistic_model.pkl", "rb")

clf= pickle.load(model_pickle)

app= Flask(__name__)

@app.route("/ping", methods=['GET'])
############################################################
# for testing localhost.
def ping():
    return {"message":"Hi there, I'm working!!"}
#############################################################
##define endpoint which will make prediction

@app.route("/prediction", methods=["POST"])
def prediction():
    """
    Return loan appliction status using ML Model
    """
    loan_req= request.get_json()
    print(loan_req)
    
    if loan_req["Education"]=="Graduate":
        Education = 1
    else:
        Education = 0
    if loan_req["Gender"] == "Male":
        Gender = 1
    else:
        Gender = 0
    Credit_History=loan_req['Credit_History']
    
    
    result=clf.predict([ [Credit_History, Education, Gender]])
    
    if result==1:
        pred= "Approve"
    else:
        pred="Rejected"
    return {"loan_approval_status_is":pred}
        
        
