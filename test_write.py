import pickle
tokens = [['シャネル','は','フランス','の','企業','で','ある'], ['1909','年','パリ','17','区','マルゼルブ','大通り','（fr）','160','番地','に','女性','用','の','帽子','店','を','開業','する']]
labels = [['B-正式名称','O','B-本拠地国','O','O','O','O'], ['B-設立年','I-設立年','B-創業地','I-創業地','I-創業地','I-創業地','I-創業地','I-創業地','I-創業地','I-創業地','O','B-創業時の事業','I-創業時の事業','I-創業時の事業','I-創業時の事業','I-創業時の事業','O','O','O']]

## write
with open('test_tokens.txt', 'wb') as f:
    pickle.dump(tokens, f)

with open('test_labels.txt', 'wb') as f:
    pickle.dump(labels, f)

## read
with open('test_tokens.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)
    print(type(d))

with open('test_labels.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)
    print(type(d))
