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

# In this example, pattern is a list of objects that defines the combinations of tokens
# to be matched. Both POS tags it are PROPN (proper noun). So, the pattern consists of two
# objects in which the POS tags for both tokens should be PROPN. This pattern is then added
# to Matcher using FULL_NAME and the match_id. Finally, matches are obtained with their 
# starting and end indexes

# Another example
conference_org_text = ('There is a developer conference' 'happening on 21 July 2019 in London. it is titled'
'"Applications of Natural Language Processing".' 'There is a helpline number available' ' at (123) 456-789')
matcher = Matcher(nlp.vocab)
def extract_phone_number(nlp_doc):
    pattern = [{'ORTH':'('}, {'SHAPE': 'ddd'},
               {'ORTH':')'}, {'SHAPE': 'ddd'},
               {'ORTH': '-', 'OP': '?'},
               {'SHAPE': 'ddd'}]
    matcher.add('PHONE_NUMBER',None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text 
        
conference_org_doc = nlp(conference_org_text)
print(extract_phone_number(conference_org_doc))                

# In this example, only the pattern is updated in order to match phone numbers from 
# the previous example. Here, some attributes of the tokens are also used:
# ORTH gives the exact text of the token
# SHAPE transforms the token string to show orthographic features
# OP defines operators. Using ? as a value means that the pattern is optional, meaning it 
# can match 0 or 1 times. 

# Rule-based matching helps you identify and extract tokens and phrases accordign to 
# lexical patterns (such as lower case) and grammatical features (such as part of speech).