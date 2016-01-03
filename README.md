# aws_data_pipeline_validate
Validate an AWS data-pipeline definition.  

Useful in a disaster recovery situation, where you need to recreate your data-pipelines.

Parse the data pipeline JSon (which will be under version control).

Look at tests/simple_test.py:test_validate_pipeline_definition, to understand how the "pipelineObjects, parameterObjects, and parameterValues" JSon are "parsed".

You can use this JSon to call: 

**DataPipeline.Client.put_pipeline_definition**, 

and 

**DataPipeline.Client.validate_pipeline_definition**

### API reference (http://boto3.readthedocs.org/en/latest/reference/services/datapipeline.html#DataPipeline.Client.validate_pipeline_definition)


    response = client.validate_pipeline_definition(
    pipelineId='string',
    pipelineObjects=[
        {
            'id': 'string',
            'name': 'string',
            'fields': [
                {
                    'key': 'string',
                    'stringValue': 'string',
                    'refValue': 'string'
                },
            ]
        },
    ],
    parameterObjects=[
        {
            'id': 'string',
            'attributes': [
                {
                    'key': 'string',
                    'stringValue': 'string'
                },
            ]
        },
    ],
    parameterValues=[
        {
            'id': 'string',
            'stringValue': 'string'
        },
    ]
    )

### Checking the validation response

    {u'validationErrors': [], u'errored': False, u'validationWarnings': 
    [{u'id': u'Default', u'warnings': [u"'pipelineLogUri'is missing. It is recommended to set this value on Default object for better troubleshooting."]}], 
    'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'be705380-b1b4-11e5-ae68-3961d897082f'}}

The response has a **HTTPStatusCode': 200, and errored': False**

