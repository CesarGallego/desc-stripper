import json
import sys
from pprint import pprint
import spacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

for line in sys.stdin:
    json_line = json.loads(line)
    doc = nlp(json_line)
    clean = [X.text for X in doc.ents]
    print(json.dumps(clean))
