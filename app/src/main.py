import spacy
import os
import itertools

from typing import List
from collections import Counter
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

nlp = spacy.load("de_core_news_lg")


def preprocess(data: List[dict]) -> List[dict]:
    """Add parameter nouns which contains tokens"""
    preprocess_data = []
    for elem in data:
        elem["nouns"] = [token.lower_ for token in nlp(elem["name_product"]) if
                         len(token) > 2 and token.dep_ == 'ROOT' and token.pos_ == 'NOUN']
        preprocess_data.append(elem)
    return preprocess_data


def get_tags(candidates_tokens: List[str], tokens_freq: dict):
    """Get tags: take the first one found in the sorted dictionary of tokens"""
    for token in candidates_tokens:
        if token in tokens_freq.keys():
            return token
    return None


@app.route('/', methods=['GET'])
def healthcheck():
    return 'healthy', 200


@app.route('/tags', methods=['POST'])
def predict_tags():
    data = preprocess(request.json["items"])
    nouns = list(itertools.chain(*[item['nouns'] for item in data]))
    tokens = {tag: count for tag, count in Counter(nouns).most_common() if count > 1 and tag.isalpha()}
    tokens = {k: v for k, v in sorted(tokens.items(), key=lambda item: item[1], reverse=True)}
    for item in data:
        item["tags"] = get_tags(item["nouns"], tokens)

    return jsonify(data), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4444))
    app.run(host='0.0.0.0', port=port, debug=False)
