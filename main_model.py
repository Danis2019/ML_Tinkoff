import re
import numpy as np

def preprocessing(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()
    data = data.lower()
    data = data.replace('\n', ' ')
    data = data.replace(',', ' ')
    data = data.replace('/', ' ')
    data = data.replace('(', ' ')
    data = data.replace(')', ' ')
    data = data.replace('.', ' ')
    data = data.replace('?', ' ')
    data = data.replace('!', ' ')
    data = data.replace('[', ' ')
    data = data.replace(']', ' ')
    data = data.replace('—', ' ')
    data = data.split()
    return data

class NGrammModel:
    def fit(input_file):
        data = preprocessing(input_file)
        ngrams_dict = {}
        for word_numb in range(len(data) - 1):
            key = data[word_numb] + ' ' + data[word_numb + 1]
            try:
                ngrams_dict[f'{key}'] += 1
            except:
                ngrams_dict[f'{key}'] = 1

        for ngrams in ngrams_dict.keys():
            count = ngrams_dict[ngrams]
            predicted_word = ngrams.split()[-1]
            before_words = ngrams.split()[:-1]
            for ngrams_2 in ngrams_dict.keys():
                if predicted_word == ngrams_2.split()[-1] and before_words != ngrams_2.split()[:-1]:
                    count += ngrams_dict[ngrams_2]
            ngrams_dict[ngrams] = ngrams_dict[ngrams] / count

        return ngrams_dict

    def generate(input_file, ngrams_dict, count_words):
        data = preprocessing(input_file)
        predicted_text = ''
        for i in range(count_words):
            input_words = np.random.choice(data, 1)
            max_p = 0
            for ngrams in ngrams_dict.keys():
                if ngrams.split()[:-1] == input_words:
                    try:
                        if max_p < ngrams_dict[ngrams]:
                            predeicted_word = ngrams.split()[-1]
                            max_p = ngrams_dict[ngrams]
                    except:
                        predeicted_word = ngrams.split()[-1]
                        max_p = ngrams_dict[ngrams]
            data.append(predeicted_word)
            predicted_text += ' ' + predeicted_word
        print(f'predicted_text:{predicted_text}')
        return predicted_text

model = NGrammModel
model1 = NGrammModel.fit('train_text.txt')
text = NGrammModel.generate('test_text.txt', model1, 3)
