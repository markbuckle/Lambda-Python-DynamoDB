# python-lambda-with-database

AWS Lambda functions are a great way to deploy your Python code or API (e.g. Flask, FastAPI) - at a cheap cost and not having to worry about servers. But since Lambda functions are ephemeral (they disappear after they finish running), how do we persist data? In this tutorial, we'll use AWS DynamoDB as a database for us to store information used by our Lambda functions.

Create a new function in the [Lambda Function Console](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/discover) 

Go to the **Code** tab, configure a new **Test event** and then hit **Test**

Go back into configure test event and change the JSON accordingly:
```json
{
  "user": "{whateverusername_aws}",
}
```
