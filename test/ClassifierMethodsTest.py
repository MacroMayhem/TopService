import unittest
from source.Classifier import Classifier
from source.MessageCategory import MessageCategory


class ClassifierMethodsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.classifier = Classifier()
        cls.classifier.load_model()

    def test_classify_CANCEL(self):
        test = 'I want to cancel my order'
        expected_result = MessageCategory.CANCEL_ORDER
        result,_ = ClassifierMethodsTest.classifier.classify(test)
        self.assertEqual(result,expected_result)

    def test_classify_STATUS(self):
        test = 'order status please'
        expected_result = MessageCategory.ORDER_STATUS
        result,_ = ClassifierMethodsTest.classifier.classify(test)
        self.assertEqual(result,expected_result)


if __name__ == '__main__':
    unittest.main()
