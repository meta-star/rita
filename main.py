"""
Rita - a calculator with processing natural language.

:license MPL v2.0
:website https://project.starinc.xyz/rl
:copyright 2019 Star Inc.(https://starinc.xyz) All Rights Reserved.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, Concatenate
from tensorflow.keras.models import Model
from transformers import TFBertModel

bert_layer = TFBertModel.from_pretrained('bert-base-uncased')

vocab = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
         'eight': 8, 'nine': 9, 'plus': 10, 'minus': 11, 'times': 12, 'divided': 13, 'by': 14}

input_layer = Input(shape=(None,))
embedding_layer = Embedding(input_dim=len(vocab), output_dim=16)(input_layer)
lstm_layer = LSTM(16)(embedding_layer)
bert_input = bert_layer([input_layer])[1]
concat_layer = Concatenate()([lstm_layer, bert_input])
dropout_layer = Dropout(0.2)(concat_layer)
output_layer = Dense(4)(dropout_layer)
model = Model(inputs=input_layer, outputs=output_layer)
model.compile(optimizer='adam', loss='mse')

questions = ['what is one plus two?', 'what is three minus two?',
             'what is four times two?', 'what is six divided by two?']
answers = [[1, 10, 2, 0], [3, 11, 2, 0], [4, 12, 2, 0], [6, 13, 2, 0]]

X = [[vocab[word] for word in question.lower().split()]
     for question in questions]
X = pad_sequences(X, padding='post')

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=5)
model.fit(X, np.array(answers), epochs=100, callbacks=[early_stopping])

test_question = 'what is five plus three?'
test_input = np.array([vocab[word]
                      for word in test_question.lower().split()]).astype('int32').reshape(1, -1)
test_output = model.predict(test_input)
test_answer = ''
for i in range(4):
    if i == 2 and test_output[0][i] == 12:
        test_answer += 'times'
    elif i == 2 and test_output[0][i] == 13:
        test_answer += 'divided by'
    else:
        test_answer += list(vocab.keys()
                            )[list(vocab.values()).index(int(test_output[0][i]))] + ' '
print(test_answer.strip())
