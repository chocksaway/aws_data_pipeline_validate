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


def validate_data_pipeline_definition(pipeline_objects, parameter_objects, parameter_values):
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

    id = 'df-0450879G3LEAVCDEBPH'
    client = boto3.client('datapipeline')

    response = client.validate_pipeline_definition(
            pipelineId=id,
            pipelineObjects=pipeline_objects,
            parameterObjects=parameter_objects,
            parameterValues=parameter_values
    )

    return response

