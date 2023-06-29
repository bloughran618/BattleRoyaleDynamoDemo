import json

import boto3
import subprocess

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('battle-royale')

items = []

with open('items.json', 'r') as f:
    for row in f:
        items.append(json.loads(row))

with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)

print(f"The item count of the table: {table.item_count}, updated every 6 hrs")
# note that scans are discouraged because they access every item in the db
print("The real item count, doing a full table scan:")
subprocess.run(["aws", "dynamodb", "scan", "--table-name", "battle-royale", "--select", "COUNT"])

