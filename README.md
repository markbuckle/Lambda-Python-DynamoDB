# python-lambda-with-database

AWS Lambda functions are a great way to deploy your Python code or API (e.g. Flask, FastAPI) - at a cheap cost and not having to worry about servers. But since Lambda functions are ephemeral (they disappear after they finish running), how do we persist data? In this tutorial, we'll use AWS DynamoDB as a database for us to store information used by our Lambda functions.

## Getting Started in AWS Lambda
Create a new function in the [Lambda Function Console](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/discover) 

Go to the **Code** tab, configure a new **Test event** and then hit **Test**

Go back into configure test event and change the JSON accordingly:
```json
{
  "user": "{whateverusername_aws}"
}
```
Edit the Lambda function code to your desire, for example:
```py
import json

def lambda_handler(event, context):
    user = event["user"]
    return {
        'message': f"Hello {user}"
    }
```
Press **Deploy** (to save) and then run **Test**

Move your code over to your IDE (i.e. VS Code) and start updating the rest there. 

## DynamoDB

Amazon has 9-10 database types, but only two of them are serverless; DynamoDB and Aurora. Aurora is a sequel DB which we do not need right now.

Go to the AWS console and search '[DynamoDB](https://us-east-1.console.aws.amazon.com/dynamodbv2/home?region=us-east-1#)'

Click 'Create Table' to get started

Enter a table name and a partition key (i.e 'user')

Go to customize settings and change the read and write capacity from Provisioned to On-Demand. Skip everying else and hit 'Create Table'.

## AWS CLI

Next we want to be able to interact with our DynamoDB table in our VS code. To do that we need to make sure AWS CLI is installed.

Download the latest AWS CLI [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Once downloaded (or if you already had it installed), run:
```pwsh
aws sts get-caller-identity
```
to make sure your AWS CLI is configured properly. 

## AWS SDK
The AWS SDK is called boto3. Run:
```pwsh
pip install boto3
```
and then in your code include:
```py
import boto3
```
Once that is installed we can access the DynamoDB table.











