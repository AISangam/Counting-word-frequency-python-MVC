# text = "India is a famous country all over the world. Geographically, our country is located to the south of Asia continent. India is a high population country and well protected from all directions naturally. It is a famous country for its great cultural and traditional values all across the world. It contains a mountain called Himalaya which is biggest in the world. It is surrounded by the three big oceans from three directions such as in south with Indian Ocean, in east with Bay of Bengal and in west with Arabic sea. India is a democratic country ranks second for its population. The national language of India is Hindi however almost fourteen nationally recognized languages are spoken here"

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

# tokenize the words of the given text

def frequency_occurence(text): 
	words_tokens = word_tokenize(text.lower())

# Load stop words
	stop_words = stopwords.words('english')

	recitified_words = [words  for words in words_tokens if words not in stop_words]
# remove punctuation from the text using isalpha
	cleaned_words = [words for words in recitified_words if words.isalpha()]

# removing article 'the' from the list
	tok_to_remove = "the"
	final_words = [words for words in cleaned_words if words not in tok_to_remove]
	list_dupl_check= list()
	for words in final_words:
		if words not in list_dupl_check:
			list_dupl_check.append(words)
    
	final_dict = dict()
	for unique_words in list_dupl_check:
		 final_dict[unique_words] = final_words.count(unique_words) 
		 	
	return (final_dict)
