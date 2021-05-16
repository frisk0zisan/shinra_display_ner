import argparse
import pickle

from display import display_ner

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shinra scoring program')
    parser.add_argument('tokens', help='token list path')
    parser.add_argument('labels', help='label list path')

    args = parser.parse_args()

    with open(args.tokens, 'rb') as f:
        tokens = pickle.load(f)

    with open(args.labels, 'rb') as f:
        labels = pickle.load(f)
        
    display_ner(tokens, labels)


