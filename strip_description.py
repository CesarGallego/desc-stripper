import json
import sys
from pprint import pprint
import spacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

for line in sys.stdin:
    parts = json.loads(line)
    doc = nlp(parts[1])
    clean = [X.text for X in doc.ents]
    parts[1] = clean
    print(json.dumps(parts))
