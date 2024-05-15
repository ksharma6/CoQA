import torch

from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

class Transformer:
    def __init__(self, model, tokenized_data):
        self.model = model
        self.data = tokenized_data

class Tokenizer:
    def __init__(self, raw_data):
        self.data = raw_data

    def tokenize(self):
        tokenizer = BertTokenizer
        encoding = tokenizer.encode_plus