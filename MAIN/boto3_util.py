import boto3


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
