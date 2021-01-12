# Dependency parsing
# Dependency parsing is th eprocess of extracting parts of a sentence to
# represent its grammatical structure. It defines the dependency relationship
# between headwords and their dependents. The head of a sentence has no 
# dependency and is called the root of the sentence. The verb is usually the head
# of the sentence. All other words are linked to the headword. 

# The dependencies can be mapped in a directed graph representation:
# words are the nodes
# the grammatical relationships are the edges

# Dependency parsing helps you know what role a word plays in the text and how
# different words relate to each other. It's also used in shallow parsing and named
# entity recognization

import spacy
nlp = spacy.load('en_core_web_sm')

piano_text = 'Gus is learning piano'
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(token.text, token.tag_, token.head, token.dep_)


# In this example, the sentence contains three relationships:
# nsubj is the subject of the word. Its headword is a verb.
# aux is an auxillary word. Its headword is a verb.
# dobj is the directory object of the verb. Its headword is a verb

# You can visualize the dependency tree using displaCy
from spacy import displacy
displacy.serve(piano_doc, style='dep')