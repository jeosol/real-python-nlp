# Word Frequency
# You can convert a given text into tokens and perform statistical analysis over it. 
# This analysis can give you various insights about words patterns, such as common words
# unique words in the text:

from collections import Counter
import spacy
nlp = spacy.load('en_core_web_sm')

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

# Remove stop words and punctuation smbols
words = [token.text for token in complete_doc if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occuring words with their frequencies
common_words = word_freq.most_common(5)
print(common_words)

# unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print(unique_words)

# From the result of the frequency analysis, we can see what the text is about. In the example
# above, the text is about Gus, London, or Natural Language Processing. 

# Another example with stop words
words_all = [token.text for token in complete_doc if not token.is_punct]
words_freq_all = Counter(words_all)
# 5 commonly occuring words with their frequency
common_words_all = words_freq_all.most_common(5)
print(common_words_all)

# In the above example, four out of five of the most common words are stop words, which does not
# tell us much about the text. If you consider stop words while doing word frequency analysis, then
# you won't be able to derive meaningful insights from the input text. This is why removing stop words
# is so important.