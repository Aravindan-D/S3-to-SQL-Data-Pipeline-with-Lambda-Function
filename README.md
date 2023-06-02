# S3-to-SQL-Data-Pipeline-with-Lambda-Function



# S3 to SQL Data Pipeline

This repository contains the code for a data pipeline that triggers a Lambda function when a JSON file is posted on Amazon S3. The Lambda function then stores the data from the JSON file into an SQL database.

## Architecture Overview

The data pipeline follows the following steps:

1. JSON file is uploaded to an S3 bucket.
2. The S3 bucket triggers an event, which invokes a Lambda function.
3. The Lambda function retrieves the JSON file from S3.
4. The JSON data is parsed and transformed as needed.
5. The transformed data is stored in an SQL database.

## Prerequisites

Before setting up the data pipeline, make sure you have the following:

- An AWS account with access to the following services:
  - Amazon S3
  - AWS Lambda
  - Amazon RDS (for the SQL database)
