from snowballstemmer import TurkishStemmer
from trtokenizer.tr_tokenizer import SentenceTokenizer, WordTokenizer
import argparse

def main(args):
    stemmer = TurkishStemmer()
    word_tokenizer = WordTokenizer()
    sentence_tokenizer = SentenceTokenizer()

    word_frequencies = {}



    with open(args.file,'r',encoding='utf-8') as textfile:
        text = textfile.read()
        text = text.lower()

    def reducer(lst):
        reducedlst = []
        for tuple in lst:
            reducedlst+=tuple
        return reducedlst


    cumleler = sentence_tokenizer.tokenize(text)
    kelimeler = list(map(lambda cumle:word_tokenizer.tokenize(cumle),cumleler))
    kelimeler = reducer(kelimeler)
    kelimeler = list(map(lambda kelime: stemmer.stemWord(kelime),kelimeler))

    for kelime in kelimeler:
        if kelime not in word_frequencies:
            word_frequencies[kelime] = 1
        else:
            word_frequencies[kelime] += 1

    def sorter(dct):
        newdct = {}
        while len(dct) > 0:
            largest_item = None
            largest_value = 0
            for item in dct:
                if dct[item] > largest_value:
                    largest_item = item
                    largest_value = dct[item]
            newdct[largest_item] = largest_value
            del(dct[largest_item])
        return newdct

    def remove_junktokens(dct):
        prefix_list = [',','.','ve','olarak','için','bir','bu','ki','de','da','her','daha','hala']
        for prefix in prefix_list:
            if prefix in dct:
                del[dct[prefix]]
        
    word_frequencies = sorter(word_frequencies)
    remove_junktokens(word_frequencies)
    print(f"First {args.words} keywords are:")
    for word in list(word_frequencies)[:args.words]:
        print(word)
    exit()
    



parser = argparse.ArgumentParser(description="Get first n keywords from a summarized text")
parser.add_argument("--file", type=str, help="Path to the text file", required=True)
parser.add_argument("--words", type=int, help="Number of keywords that you want", required=True)
args = parser.parse_args()
main(args)
