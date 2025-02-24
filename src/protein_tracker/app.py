import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'POST':
        return add_protein(event)
    elif http_method == 'GET':
        return get_protein(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method')
        }

def add_protein(event):
    try:
        body = json.loads(event['body'])
        user_id = event['requestContext']['authorizer']['claims']['sub']
        protein_amount = body['protein']
        date_logged = datetime.now().strftime('%Y-%m-%d')

        table.put_item(
            Item={
                'userId': user_id,
                'dateLogged': date_logged,
                'proteinAmount': protein_amount
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Protein entry added successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

def get_protein(event):
    try:
        user_id = event['requestContext']['authorizer']['claims']['sub']
        date_logged = event['queryStringParameters'].get('date', datetime.now().strftime('%Y-%m-%d'))

        response = table.get_item(
            Key={
                'userId': user_id,
                'dateLogged': date_logged
            }
        )

        item = response.get('Item', {})
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }