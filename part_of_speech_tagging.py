# Part of Speech Tagging
# POS is a grammatical role that explains how a particular word is used in a sentence
# There are eight parts of speech:
# Noun, Pronoun, Adjective, Verb, Adverb, Preposition, Conjunction, Interjection
#
# Part of speech tagging is the process of assigning a POS tag to each token depending on its
# usage in the sentence. 
# POS tags are useful for assigning a syntactic category like noun or verb to each word

# In spaCy, POS tags are available as an attribute on the Token object:

import spacy
nlp = spacy.load('en_core_web_sm')

about_text = ('Gus Proto is a Python developer currently' ' working for a London-based Fintench' ' company. He is interested in learning' ' Natural Language Processing')
about_doc = nlp(about_text)

# Two attributes of the Token class are accessed:
# tag_ lists the fine-grained part of speech
# pos_ lists the coarse-grained part of speech
# spacy.explain gives description details about a particular POS tag.
for token in about_doc:
    print(token, token.tag_, token.pos_, spacy.explain(token.tag_))

nouns = []
adjectives = []
for token in about_doc:
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)
print(nouns)
print(adjectives)    