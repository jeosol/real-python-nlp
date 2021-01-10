# Preprocessing functions
# Create a preprocessing function that takes a text as input and applies the following
# operations:
# - lowercase the text
# - lemmatizes each token
# - removes punctuation symbols
# - Removes stop words

import spacy
nlp = spacy.load('en_core_web_sm')

def is_token_allowed(token):
    """ Only allow valid token which are not stop words
        and punctuation symbols.
    """
    if (not token or not token.string.strip() or
        token.is_stop or token.is_punct):
        return False
    return True
        
def preprocess_token(token):
    """ Reduce token to its lowercase lemma form """
    return token.lemma_.strip().lower()


complete_text = ('Gus Proto is a Python developer currently'
     ' working for a London-based Fintech company. He is'
     ' interested in learning Natural Language Processing.'
     ' There is a developer conference happening on 21 July'
     ' 2019 in London. It is titled "Applications of Natural'
     ' Language Processing". There is a helpline number '
     ' available at +1-1234567891. Gus is helping organize it.'
     ' He keeps organizing local Python meetups and several'
     ' internal talks at his workplace. Gus is also presenting'
     ' a talk. The talk will introduce the reader about "Use'
     ' cases of Natural Language Processing in Fintech".'
     ' Apart from his work, he is very passionate about music.'
     ' Gus is learning to play the Piano. He has enrolled '
     ' himself in the weekend batch of Great Piano Academy.'
     ' Great Piano Academy is situated in Mayfair or the City'
     ' of London and has world-class piano instructors.')

complete_doc = nlp(complete_text)

complete_filtered_tokens = [preprocess_token(token) for token in complete_doc if is_token_allowed(token)]
print(complete_filtered_tokens)

# the completed_filtered_tokens does not contain any stop word or punctuation symbols and consist of lemmatized
# lowercase tokens
