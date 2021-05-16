import spacy
from spacy.tokens import Doc
from spacy.vocab import Vocab
from spacy import displacy  

def display_ner(tokens, labels):
    vocab = Vocab()
    html=''
    for token, label in zip(tokens, labels):
        #doc.user_data["title"] = "This is title"
        doc = Doc(vocab, words=token, ents=label)
        html += displacy.render(doc, style="ent", page=True)
        html += '\n\n'

    with open('display_ner.html', 'w') as f:
        f.write(html)



