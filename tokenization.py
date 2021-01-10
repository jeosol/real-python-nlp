# Tokenization in spaCy
# Tokenization is the next step after sentence detection. it allows you to identify
# the basic units in your text. These basic units are called tokens. Tokenization is useful
# because it breaks a text into meaningful units. These units are used for further analysis, like
# part of speech tagging

import spacy
import re
from spacy.tokenizer import Tokenizer

# Load the default model for the English Language en_core_web_sm
nlp = spacy.load('en_core_web_sm') 
about_text = ('Gus Proto is a Python developer currently' ' working for a London-based Fintench' ' company. He is interested in learning' ' Natural Language Processing')

about_doc = nlp(about_text)

# In spaCy, we print tokens by iterating on the Doc object
for token in about_doc:
    print(token, token.idx)

# spaCy provides various attributes for the Token Class
# text_with_ws - prints token with trailing space (if present)
# is_alpha - detects if the token consists of alphabetic characters or not
# is_punct detects if the token is a punctuation symbol or not.
# is_space detects if the token is a space or not.
# shape_ prints out the shape of the word
# is_stop detects if the toekn is a stop word or not.
for token in about_doc:
    print(token, token.idx, token.text_with_ws, token.is_alpha, token.is_punct, token.is_space,
    token.shape_, token.is_stop)
               

# Detecting hyphenated words, e.g., London-based
custom_nlp = spacy.load('en_core_web_sm')
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re =  re.compile(r'''[-~]''')               
def customize_tokenizer(nlp):
    # Adds support to use `-` as the delimiter tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                    suffix_search=suffix_re.search,
                    infix_finditer=infix_re.finditer,
                    token_match=None)
                
custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_about_doc = custom_nlp(about_text)
print([token.text for token in custom_tokenizer_about_doc])                