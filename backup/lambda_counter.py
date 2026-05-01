import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-visits')

def lambda_handler(event, context):

    KEY = {'id': 'counter'}  # MUST match scan result

    response = table.update_item(
        Key=KEY,
        UpdateExpression='SET #c = if_not_exists(#c, :start) + :inc',
        ExpressionAttributeNames={
            '#c': 'count'
        },
        ExpressionAttributeValues={
            ':inc': 1,
            ':start': 0
        },
        ReturnValues='UPDATED_NEW'
    )

    visits = int(response['Attributes']['count'])

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"visits": visits})
    }
