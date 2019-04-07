from source.Classifier import Classifier
from flask import Flask
app = Flask(__name__)
from flask import request
import json
from source.MessageCategory import  MessageCategory
from source.ResponseCreator import ResponseCreator

__author__ = "Aditya Singh"
__version__ = "0.1.0"


@app.route("/classify",methods =['GET'])
def classify_request():

    try:
        # Load  classifier
        classifier = Classifier()
        classifier.load_model()
        query = request.get_json()

        print(query)

        # Classify
        category, confidence = classifier.classify(query['message'])

        # Prepare response
        message = None
        if category == MessageCategory.CANCEL_ORDER:
            message = ResponseCreator.get_cancel_response()
        if category == MessageCategory.ORDER_STATUS:
            message = ResponseCreator.get_status_response()
        response = {'suggested_message':message,'prediction_category': category.name
            ,'prediction_confidence':str(confidence)}
        return json.dumps(response)
    except Exception as e:
        return  json.dumps('Error in computing the allocation as: '+str(e))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
