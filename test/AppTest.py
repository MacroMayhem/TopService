import unittest
from source.main import  app
import json
from unittest import mock
from source.MessageCategory import  MessageCategory
from source.ResponseCreator import ResponseCreator


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def do_nothing(self):
        pass

    @mock.patch('source.main.Classifier')
    def test_cancel_order_response(self, classifier):
        classifier_instance = classifier.return_value
        classifier_instance.classify.return_value = MessageCategory.CANCEL_ORDER, 1.0
        classifier_instance.load_model = self.do_nothing
        response = self.app.get('/classify',data=json.dumps(dict(message='Cancel my order'))
                                ,content_type='application/json', follow_redirects=True)
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['suggested_message'],ResponseCreator.get_cancel_response())
        self.assertEqual(response_data['prediction_confidence'],str(1.0))
        self.assertEqual(response_data['prediction_category'],MessageCategory.CANCEL_ORDER.name)

    @mock.patch('source.main.Classifier')
    def test_others_response(self, classifier):
        classifier_instance = classifier.return_value
        classifier_instance.classify.return_value = MessageCategory.OTHERS, 1.0
        classifier_instance.load_model = self.do_nothing
        response = self.app.get('/classify', data=json.dumps(dict(message='Random String'))
                                , content_type='application/json', follow_redirects=True)
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['suggested_message'], None)
        self.assertEqual(response_data['prediction_confidence'], str(1.0))
        self.assertEqual(response_data['prediction_category'], MessageCategory.OTHERS.name)


if __name__ == '__main__':
    unittest.main()
