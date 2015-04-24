import pandas as pd
import nltk
import codecs


def prep_input(x):
    tokens = nltk.wordpunct_tokenize(x)
    text = nltk.Text(tokens)
    words = [w.lower() for w in text]
    return words

def predict(x, top_word, bigrams, trigrams):
    X_ = prep_input(x)
    if len(X_) > 1:
        X = X_[-2] + ' ' + X_[-1]
        tri = list(trigrams['Word1'] + ' ' + trigrams['Word2'])
        if X in tri:
            index = tri.index(X)
            y = trigrams['Word3'][index]
            return y
    X = X_[-1]
    bi = list(bigrams['Word1'])
    if X in bi:
        y = bigrams[bigrams['Word1'] == X]['Word2'].iloc[0]
        return y
    
    y = top_word
    return y

def read_file(filepath):
    with open(filepath) as f:
        output = f.readlines()
    output = [item.strip().split('\t') for item in output]
    columns = ['index'] + output[0]
    output = pd.DataFrame(output[1:], columns = columns)
    return output
    
if __name__ == '__main__':    

    the_bigrams = read_file('bigrams.txt')
    the_trigrams = read_file('trigrams.txt')

    
    def pred(x, word = 'the', b = the_bigrams, t = the_trigrams):
        '''Predicts words'''
        output = predict(x, word, b, t)
        return output

    print('Type "pred(your_string_here)" to get prediction of the next word')

    #predict('the', 'the', the_bigrams, the_trigrams)
    
