import boto3
import random
import string


def get_s3_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def get_data_pipelines():
    client = boto3.client('datapipeline')

    response = client.list_pipelines()
    print response

def get_data_pipeline_definition():
    id = 'df-0450879G3LEAVCDEBPH'
    client = boto3.client('datapipeline')

    response = client.get_pipeline_definition(
            pipelineId=id
    )

    return response


def validate_data_pipeline_definition(id, pipeline_objects, parameter_objects, parameter_values):
    """
    :param pipeline_objects:
    :param parameter_objects:
    :param parameter_values:
    :return:

        pipelineId
        pipelineObjects
        parameterObjects
        parameterValues
    """

    client = boto3.client('datapipeline')

    response = client.validate_pipeline_definition(
            pipelineId=id,
            pipelineObjects=pipeline_objects,
            parameterObjects=parameter_objects,
            parameterValues=parameter_values
    )

    return response


def create_data_pipeline_and_put_pipeline_definition(objects, parameters, values):
    client = boto3.client('datapipeline')
    response = client.create_pipeline(
            name='another_pipeline',
            uniqueId='zzsswwqqqaa',
            description='new pipeline')

    pipeline_id = response['pipelineId']

    response = client.put_pipeline_definition(
            pipelineId=pipeline_id,
            pipelineObjects=objects,
            parameterObjects=parameters,
            parameterValues=values
    )

    return pipeline_id, response


def delete_data_pipeline(pipeline_id):
    client = boto3.client('datapipeline')
    client.delete_pipeline(
            pipelineId=pipeline_id
    )


def create_new_dynamo_table_from_existing_detail():
    """
    Get existing details from existing DynamoDB table
    Use the Provisioned Throughput and AttributeDefinitions
    """

    # Create a random db name
    new_table = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

    client = boto3.client('dynamodb')
    response = client.describe_table(
            TableName='table1'
    )

    new_table_details = response['Table']

    throughput = new_table_details['ProvisionedThroughput']
    throughput.pop('NumberOfDecreasesToday')

    response = client.create_table(
            AttributeDefinitions=new_table_details['AttributeDefinitions'],
            TableName=new_table,
            KeySchema=new_table_details['KeySchema'],
            ProvisionedThroughput=throughput)
    return response


def get_most_recent_file_in_s3_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    result = bucket.meta.client.list_objects(Bucket=bucket.name,
                                             Delimiter='/')
    for o in result.get('CommonPrefixes'):
        print(o.get('Prefix'))

    return result.get('CommonPrefixes')




