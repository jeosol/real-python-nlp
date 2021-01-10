# spaCy comes with a built-in visualizer called displaCy. it can be used used to visualize
# a dependency parse or named entities in a browser

import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
about_interest_text = ('He is interested in learning' ' Natural Language Processing.')
about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style='dep')
