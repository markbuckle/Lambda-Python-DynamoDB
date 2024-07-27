import boto3
from pytest import Item
import os

def lambda_handler(event: any, context: any):
    user = event["user"]
    visit_count: int = 0
    
    # Create a DynaomDB client
    dynamodb = boto3.resource("dynamodb")
    # get the table environment from AWS
    table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)
    
    # Get the current visit count
    response = table.get_item(Key={"user": user})
    if "Item" in response:
        visit_count = response["Item"]["count"]
        
    # Increment the number of visits
    visit_count += 1
    
    # Put the new visit count into the table
    table.put_item(Item={"user": user, "count": visit_count})
    
    
    message = f"Hello {user}! You have visited this page {visit_count} times."
    return {"message": message}

# we dont really need this part for deployment, it's just for local testing
if __name__ == "__main__":
    table_name = os.environ["TABLE_NAME"] = "visit-count-table"
    event = {"user": "markb_local"}
    print(lambda_handler(event, None))