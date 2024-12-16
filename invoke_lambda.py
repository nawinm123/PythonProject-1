import boto3
import json

# Initialize a boto3 client for Lambda in the correct region
lambda_client = boto3.client('lambda', region_name='us-east-2')  # Adjust the region if needed

# Define the Lambda function name and payload
function_name = 'myLambdaFunction'  # Replace with your function name
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Invoke the Lambda function
try:
    response = lambda_client.invoke(
        FunctionName=function_name,  # Lambda function name or ARN
        InvocationType='RequestResponse',  # Synchronous invocation
        Payload=json.dumps(payload)  # Payload as a JSON string
    )

    # Read and parse the response payload
    response_payload = json.loads(response['Payload'].read())
    print("Lambda Response:", response_payload)
except Exception as e:
    print(f"Error invoking Lambda function: {e}")
