import boto3
import json
import mysql.connector
#its working file unless the file name doesent contain any space
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    data = json.loads(data)
    names = []
    ages = []
    
    # Connect to the database
    mydb = mysql.connector.connect(
    host="database-s3.cfrt0aspgodf.ap-northeast-1.rds.amazonaws.com",
    user=variables.user,
    password=variables.pass,
    database="test_one"
    )

    # Create a cursor
    mycursor = mydb.cursor()

    for row in data:
        sql = "INSERT INTO person (name, age) VALUES (%s, %s)"
        val=(row['name'],row['age'])
        mycursor.execute(sql, val)


    

    # Commit the changes to the database
    mydb.commit()

    # Close the cursor and database connection
    mycursor.close()
    mydb.close()
    print(names)
    print(ages)
