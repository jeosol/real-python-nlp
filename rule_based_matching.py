# Rule-based matching is one of the steps in extracting information from
# unstructured text.
# It is used to identify and extra tokens and phrases according to patterns
# (such as lowercase) and grammatical features (such as parts of speech).

# Rule-based matching can use regular expressions to extract entities (such
# as phone numbers) from an unstructured text. It's different from extracting
# text using regular expressions only in the sense that regular expressions don't 
# consider lexical and grammatical attributes of the text.

import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
def extract_full_name(nlp_doc):
    pattern = [{'POS': 'PROPN'},{'POS':'PROPN'}]
    matcher.add('FULL_NAME', None, pattern)
    matches = matcher(nlp_doc)
    for matches, start, end in matches:
        span = nlp_doc[start:end]
        return span.text 

about_text = ('Gus Proto is a Python developer currently' ' working for a London-based Fintench' ' company. He is interested in learning' ' Natural Language Processing')
about_doc = nlp(about_text)

print(extract_full_name(about_doc))