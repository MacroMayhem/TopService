import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from joblib import dump, load


class Model:
    def __init__(self):
        self.clf = None
        self.tf_idf = None
        self.count_vector = None
        try:
            # Load if pre-trained model exists
            self.load()
        except Exception:
            # Train the model and save
            self.train()
            self.save()

    def get_text_category(self,text):
        return self.clf.predict(self.tf_idf.transform(self.count_vector.transform(text)))[0]

    def get_category_confidence(self,text):
        return max(self.clf.predict_proba(self.tf_idf.transform(self.count_vector.transform(text)))[0])

    def train(self):
        try:
            data_df = pd.read_csv('../data/tech_test_data.csv')
            X_train, X_test, y_train, y_test = train_test_split(data_df['message'], data_df['case_type'], random_state=0)
            self.count_vector = CountVectorizer()
            X_train_counts = self.count_vector.fit_transform(X_train)
            self.tf_idf = TfidfTransformer()
            X_train_tfidf = self.tf_idf.fit_transform(X_train_counts)
            self.clf = MultinomialNB().fit(X_train_tfidf, y_train)
        except Exception:
            print('Model could not be trained')

    def save(self):
        try:
            dump(self.clf, '../model/clf.joblib')
            dump(self.tf_idf, '../model/tf_idf.joblib')
            dump(self.count_vector, '../model/count_vector.joblib')
        except Exception:
            print('The model could not be saved to the disk')

    def load(self):
        try:
            self.tf_idf = load('../model/tf_idf.joblib')
            self.count_vector = load('../model/count_vector.joblib')
            self.clf = load('../model/clf.joblib')
        except FileNotFoundError:
            raise FileNotFoundError('pre-trained model not found')

