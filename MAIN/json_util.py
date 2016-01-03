import json
from pprint import pprint


def read_json_and_get_dict(json_filename, dict_name):
    with open(json_filename) as data_file:
        data = json.load(data_file)
    pprint(data)
    return data[dict_name]


def check_for_ref_key_in_dict(my_dict):
    """

    :type my_dict: object
    """
    REF = 'ref'
    if REF in my_dict:
        return 'refValue', my_dict[REF]
    else:
        return 'stringValue', my_dict



def parse_dict(each, key_value):
    attributes = []
    my_dict = {}
    for key, value in each.iteritems():

        value_pair, value = check_for_ref_key_in_dict(value)

        my_dict[key_value] = key
        my_dict[value_pair] = value
        attributes.append(my_dict)
        my_dict = {}

    return attributes



def parameter_objects(my_dict):
    """
    iterate through dict
    remove id
    "default": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",

    becomes:

    {
        "stringValue": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",
        "key": "default"
     },

    :param data:
    :return:
    """
    # iterate through dict
    # remove id
    #

    outer_attributes = {}
    parameter_objects = []
    for each in my_dict:
        id = each.pop('id', None)
        attributes = parse_dict(each, 'key')

        outer_attributes['id'] = id
        outer_attributes['attributes'] = attributes
        parameter_objects.append(outer_attributes)
        outer_attributes = {}

    return parameter_objects


def parameter_values(values_dict):
    """
    convert:
        "values": {
        "myShellCmd": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt",
        "myS3InputLoc": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",
        "myS3OutputLoc": "s3://milesdincoming/"
    }

    to:

        "parameterValues": [
        {
          "stringValue": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt",
          "id": "myShellCmd"
        },
        {
          "stringValue": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data",
          "id": "myS3InputLoc"
        },
        {
          "stringValue": "s3://milesdincoming/",
          "id": "myS3OutputLoc"
        }
      ],

    :param values_dict:
    :return:
    """

    attributes = parse_dict(values_dict, 'id')
    parameter_objects = attributes

    return parameter_objects


def pipeline_objects(my_dict):
    """
    convert dict:
        "objects": [
            {
              "directoryPath": "#{myS3OutputLoc}/#{format(@scheduledStartTime, 'YYYY-MM-dd-HH-mm-ss')}",
              "name": "S3OutputLocation",
              "id": "S3OutputLocation",
              "type": "S3DataNode"
            },

    to:

        {
      "fields": [
        {
          "stringValue": "#{myS3OutputLoc}/#{format(@scheduledStartTime, 'YYYY-MM-dd-HH-mm-ss')}",
          "key": "directoryPath"
        },
        {
          "stringValue": "S3DataNode",
          "key": "type"
        }
      ],
      "id": "S3OutputLocation",
      "name": "S3OutputLocation"
    },


    :param my_dict:
    :return:
    """

    outer_attributes = {}
    objects = []
    for each in my_dict:

        id = each.pop('id', None)
        name = each.pop('name')

        attributes = parse_dict(each, 'key')

        outer_attributes['id'] = id
        outer_attributes['name'] = name
        outer_attributes['fields'] = attributes
        objects.append(outer_attributes)
        outer_attributes = {}

    pipeline_objects = objects
    return pipeline_objects
