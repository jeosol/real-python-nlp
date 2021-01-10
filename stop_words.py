import spacy
nlp = spacy.load('en_core_web_sm')
spacy_stopwords = nlp.Defaults.stop_words
print(len(spacy_stopwords))

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

about_text = ('Gus Proto is a Python developer currently' ' working for a London-based Fintench' ' company. He is interested in learning' ' Natural Language Processing')
about_doc = nlp(about_text)

# Remove stop words from the input text
for token in about_doc:
    if not token.is_stop:
        print(token)

about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
print(about_no_stopword_doc)
#print(about_no_stopword_doc.join(' '))
print(' '.join(about_no_stopword_doc))