# TopService

## Contents

1. [Overview](#overview)
2. [Project structure](#project_structure)
3. [How to execute](#how_to_execute)

## Overview

The project contains a python implementation of a multi-class text classifier. It is a Multinomial Naive Bayes Classifier which categorizes a text as
'CANCEL_ORDER', 'ORDER_STATUS' and 'OTHERS'

## Project Structure

    .
    ├── data                   # Should contain tech_test_data.csv if re-training is required
    ├── source                 # Contains the iimplementation of Flask app can classification model
    ├── model                  # Directory containing the pre-trained model
    ├── Dockerfile             # Dockerfile containing the docker instructions to set up the environment. NOT TESTED YET
    ├── test                   # Contains the unit tests corresponding to few classes
    └── README.md
    
## How To Execute

**Disclaimer** The build has been tested on Windows Docker toolbox. Docker for Windows(Mac, Linux etc.) the IP address might need to be altered. 

### DOCKER

Build the docker image from the Dockerfile. Navigate to the root of the project directory. The project structure at root is showed above. 

`docker build -t topservice:latest .`

`docker run -p 5000:5000 topservice`


### QUERY

The application accepts JSON **GET** request.

EndPoint: `http://192.168.99.100:5000/classify` 

Sample Request: `   { "message": "Please cancel the order",
                    "timestamp": "2001-02-03T10:11:12" }`
                  
Sample Response: `   {"suggested_message": "Of course. Please share your order number and account number with me and I will cancel."
                   , "prediction_category": "CANCEL_ORDER", "prediction_confidence": "0.730218624738"}
                 `

