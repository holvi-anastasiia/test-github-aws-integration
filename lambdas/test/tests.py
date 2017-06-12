import unittest

from app import app


HTTP_OK_RESPONSE = 200


class TestAppTest(unittest.TestCase):

    def request_lambda(self):
        # test comment for triggering build on commit
        event = {
            'requestContext': {
                'resourcePath': '/',
                'httpMethod': 'GET',
            },
            'pathParameters': {},
            'queryStringParameters': {},
            'headers': {},
            'body': {},
            'stageVariables': {}
        }
        return app(event, {})

    def test_response(self):
        response = self.request_lambda()
        self.assertEqual(
            response['statusCode'], HTTP_OK_RESPONSE)  
    
