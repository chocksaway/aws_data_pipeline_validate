import unittest
import json

from MAIN import boto3_util, json_util


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "SETUP!"

    def tearDown(self):
        print "TEAR DOWN!"

    def test_boto_config(self):
        boto3_util.get_s3_buckets()

    def test_data_pipeline(self):
        json_resp = boto3_util.get_data_pipeline_definition()

        json_resp = json.dumps(json_resp, indent=4)
        print json_resp

        ##
        # ResponseMetadata
        # parameterObjects
        # parameterValues
        # pipelineObjects
        ##

    def test_parameter_values(self):
        parameters_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'values'
        )

        json_util.parameter_values(parameters_dict)

    def test_parameter_objects(self):
        values_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'parameters'
        )

        json_util.parameter_objects(values_dict)

    def test_objects(self):
        objects_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'objects'
        )

        json_util.pipeline_objects(objects_dict)

    def test_validate_pipeline_definition(self):
        parameters_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'parameters'
        )

        parameters = json_util.parameter_objects(parameters_dict)

        values_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'values'
        )

        values = json_util.parameter_values(values_dict)

        objects_dict = json_util.read_json_and_get_dict(
                '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
                'objects'
        )

        objects = json_util.pipeline_objects(objects_dict)

        response = boto3_util.validate_data_pipeline_definition(objects, parameters, values)

        self.assertEquals(response['errored'], False)
        print response


if __name__ == '__main__':
    unittest.main()
