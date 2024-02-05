import boto3
import configparser
import requests
from flask import Flask, jsonify

# Load configuration from config.properties
config = configparser.ConfigParser()
config.read('config.properties')
app = Flask(__name__)

@app.route('/customer/<customer_id>')
def customer(customer_id):
    # Get PowerCurve API URL and parameters from config
    url = f"{config['PowerCurve']['api_url']}{customer_id}"
    headers = {"Authorization": f"Bearer {config['PowerCurve']['api_token']}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Create SQS client with credentials from config
        sqs = boto3.client('sqs', region_name=config['AWS']['region'], aws_access_key_id=config['AWS']['access_key'], aws_secret_access_key=config['AWS']['secret_key'])

        # Get SQS queue URL from config
        queue_url = config['AWS']['queue_url']

        # Put message on the queue
        sqs.send_message(QueueUrl=queue_url, MessageBody=str(response.json()))

        return jsonify(response.json()), 200
    else:
        return jsonify({"message": "Error connecting to PowerCurve API"}), response.status_code
    
@app.route('/credit_score/<customer_id>')
def credit_score(customer_id):
    # Get PowerCurve API URL and parameters from config
    url = f"{config['PowerCurve']['api_url']}/credit_score/{customer_id}"
    headers = {"Authorization": f"Bearer {config['PowerCurve']['api_token']}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Create SQS client with credentials from config
        sqs = boto3.client('sqs', region_name=config['AWS']['region'], aws_access_key_id=config['AWS']['access_key'], aws_secret_access_key=config['AWS']['secret_key'])

        # Get SQS queue URL from config
        queue_url = config['AWS']['queue_url']

        # Put message on the queue
        sqs.send_message(QueueUrl=queue_url, MessageBody=str(response.json()))

        return jsonify(response.json()), 200
    else:
        return jsonify({"message": "Error connecting to PowerCurve API"}), response.status_code
    
@app.route('/customer_report/<customer_id>')
def customer_report(customer_id):
    # Get PowerCurve API URL and parameters from config
    url = f"{config['PowerCurve']['api_url']}/customer_report/{customer_id}"
    headers = {"Authorization": f"Bearer {config['PowerCurve']['api_token']}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Create SQS client with credentials from config
        sqs = boto3.client('sqs', region_name=config['AWS']['region'], aws_access_key_id=config['AWS']['access_key'], aws_secret_access_key=config['AWS']['secret_key'])

        # Get SQS queue URL from config
        queue_url = config['AWS']['queue_url']

        # Put message on the queue
        sqs.send_message(QueueUrl=queue_url, MessageBody=str(response.json()))

        return jsonify(response.json()), 200
    else:
        return jsonify({"message": "Error connecting to PowerCurve API"}), response.status_code