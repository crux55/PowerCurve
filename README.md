# Flask API with PowerCurve and AWS SQS Integration

This Flask application provides API endpoints that interact with the Experian PowerCurve API and AWS SQS.

## Endpoints

- `/customer/<customer_id>`: Retrieves customer data from the PowerCurve API and puts the response on an AWS SQS queue.
- `/credit_score/<customer_id>`: Retrieves credit score data for a customer from the PowerCurve API and puts the response on an AWS SQS queue.
- `/customer_report/<customer_id>`: Retrieves a customer report from the PowerCurve API and puts the response on an AWS SQS queue.

## Configuration

The application reads configuration from a `config.ini` file. This file should have the following structure:

```ini
[PowerCurve]
api_url = https://powercurve.experian.com/api/customer-data/
api_token = your_token

[AWS]
region = your_region
access_key = your_access_key
secret_key = your_secret_key
queue_url = your_queue_url