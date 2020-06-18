# Here are all the installs and imports you will need for your word cloud script and uploader widget



import wordcloud
import numpy as np
from matplotlib import pyplot as plt
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    n_file=''
    word_dict={}
    for l in file_contents:
        if l not in punctuations:
            n_file+=l

    words_list=n_file.lower().split()

    for word in words_list:
        if word not in uninteresting_words:
            word_dict[word]=words_list.count(word)
     #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()

# Display your wordcloud image
f=open("C:/Users/RUKHSAR KHAN/Desktop/python code/handling_files/crossroad.txt")
file_contents=f.read()
f.close()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
