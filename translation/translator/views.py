from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import re
import nltk
import numpy as np
import pickle

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

class TranslationView(View):
    template_name = 'translator/translation.html'
    model = None
    x_tokenizer = None
    y_tokenizer = None
    maxlen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_model_and_tokenizers()

    def load_model_and_tokenizers(self):
        self.model = load_model(r'C:\Users\Lenovo\Desktop\Translation\translation\translator\eng_fr.h5')
        with open(r'C:\Users\Lenovo\Desktop\Translation\translation\translator\english_tokenizer.pkl', 'rb') as f:
            self.x_tokenizer = pickle.load(f)
        with open(r'C:\Users\Lenovo\Desktop\Translation\translation\translator\french_tokenizer.pkl', 'rb') as f:
            self.y_tokenizer = pickle.load(f)
        self.maxlen = self.get_maxlen()

    def remove_punc(self, x):
        x = x.lower()  # Convert text to lowercase
        return re.sub('[!#?,.:";]', '', x)

    def get_maxlen(self):
        return 23  # Set the proper maxlen value based on your dataset

    def post(self, request):
        english_text = request.POST.get('english_text', '')
        english_text = self.remove_punc(english_text)

        if not english_text:
            french_text = ''
        else:
            x = self.tokenize_input(english_text)
            prediction = self.predict(x)
            french_text = self.convert_prediction(prediction)

        context = {'french_text': french_text}
        return render(request, self.template_name, context)


    def tokenize_input(self, input_text):
        x_sequences = self.x_tokenizer.texts_to_sequences([input_text])
        x_padded = pad_sequences(x_sequences, maxlen=self.maxlen, padding='post')
        return x_padded

    def predict(self, x):
        predictions = self.model.predict(x)[0]
        return predictions

    def convert_prediction(self, prediction):
        top_indices = np.argmax(prediction, axis=-1)  # Get the index of the highest predicted word
        index_word_dict = {i: word for word, i in self.y_tokenizer.word_index.items()}
        words = []
        for idx in top_indices.tolist():
            word = index_word_dict.get(int(idx), '')
            if word:
                words.append(word)
        french_text = ' '.join(words)
        return french_text

    def get(self, request):
        return render(request, self.template_name, {'french_text': ''})

def home(request):
    return HttpResponse("Welcome to the translation app!")
