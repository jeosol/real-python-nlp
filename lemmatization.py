# Lemmatization: is the process of reducing inflected forms of a word while still 
# ensuring that the reduced form belongs to the language. The reduced form or root
# word is called a lemma
# For example, organizes, organized, and organizing are all forms of organize. Here
# organize is the lemma
# The inflection of a word allows you to express different grammatical categorizes
# like tense (organized vs organize), number (trains vs train) and so on. Lemmatization
# is necessary because it helps you reduce the inflected forms of a word so that they
# can be analyzed as a single term. It can also help normalize text

# Lemmatization helps avoid duplicate words that have similar meanings. If you do not 
# lemmatize the text, similar words (e.g., organize and organizing in the example below) will
# be counted as different tokens, even though they have similar meaning.
# spaCy as the attribute lemma_ on the Token class. The attribute has the lemmatized form
# of a token

import spacy
nlp = spacy.load('en_core_web_sm')

conference_help_text = ('Gus is helping organize a developer' 'conference on Applications of Natural Language'
' Processing. he keeps organizing local Python meetups' ' and several internal talks at his workplace.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print(token, token.lemma_)

    