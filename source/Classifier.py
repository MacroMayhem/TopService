from source.MessageCategory import MessageCategory
import operator
from source.Model import Model


class Classifier:
    def __init__(self):
        self._model = None

    def load_model(self):
        self._model = Model()

    def classify(self,text):
        """
        Classifies the given text message as CANCEL_ORDER, ORDER_STATUS, OTHERS
        :param text: Input text message to be classified
        :return: Category, Confidence
        """
        try:
            category = self._model.get_text_category([text])
            confidence = self._model.get_category_confidence([text])
            if confidence > 0.6:                  # Less confident texts are classified as OTHERS
                return MessageCategory(category), confidence
            else:
                return MessageCategory.OTHERS, 1-confidence
        except Exception as e:
            raise Exception('Classification Failed'+str(e))
