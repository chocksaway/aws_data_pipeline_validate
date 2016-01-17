import unittest

from MAIN import boto3_util, json_util


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print "SETUP!"

    def tearDown(self):
        print "TEAR DOWN!"

    def test_boto_config(self):
        boto3_util.get_s3_buckets()

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

    # def test_validate_pipeline_definition(self):
    #     parameters_dict = json_util.read_json_and_get_dict(
    #             '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
    #             'parameters'
    #     )
    #
    #     parameters = json_util.parameter_objects(parameters_dict)
    #
    #     values_dict = json_util.read_json_and_get_dict(
    #             '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
    #             'values'
    #     )
    #
    #     values = json_util.parameter_values(values_dict)
    #
    #     objects_dict = json_util.read_json_and_get_dict(
    #             '/Users/milesd/python/workspace/skeleton/MAIN/pipeline.json',
    #             'objects'
    #     )
    #
    #     objects = json_util.pipeline_objects(objects_dict)
    #
    #     response = boto3_util.validate_data_pipeline_definition(objects, parameters, values)
    #
    #     self.assertEquals(response['errored'], False)
    #     print response

    def test_create_and_validate_pipeline_definition(self):
        """
        Create pipeline

        Get the id

        Put definition

        Validate definition

        Delete pipeline

        :return:
        """
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

        pipeline_id, response = boto3_util.create_data_pipeline_and_put_pipeline_definition \
            (objects, parameters, values)

        self.assertEquals(response['errored'], False)

        response = boto3_util.validate_data_pipeline_definition(pipeline_id, objects, parameters, values)

        self.assertEquals(response['errored'], False)
        print response

        boto3_util.delete_data_pipeline(pipeline_id)

    def test_get_dynamodb_details(self):
        response = boto3_util.create_new_dynamo_table_from_existing_detail()
        http_response_created_success = response['ResponseMetadata']['HTTPStatusCode']
        self.assertEquals(http_response_created_success, 200)

    def test_get_most_recent_file_in_s3_bucket(self):
        response = boto3_util.get_most_recent_file_in_s3_bucket('milesdincoming')
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
