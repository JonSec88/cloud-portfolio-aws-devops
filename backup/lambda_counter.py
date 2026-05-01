import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-visits')

def lambda_handler(event, context):

    KEY = {'id': 'counter'}  # confirm this matches your item

    try:
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

    except Exception as e:
        print("ERROR:", str(e))
        visits = 0

    headers = event.get('headers') or {}
    accept = headers.get('accept', '')

    if 'text/html' not in accept:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"visits": visits})
        }

    html = f"""
    <html>
    <body style="background:#080c12;color:#00d4ff;text-align:center;margin-top:100px;font-family:sans-serif;">
    <h2>Visitor Counter API</h2>
    <h1>{visits}</h1>
    <p>Live</p>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": html
    }
