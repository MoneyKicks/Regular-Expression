
# coding: utf-8

# In[12]:


#Chunking is use to extract a section or part of a sentence as per our own defined set of grammar. 
#So as to make some sense out of the sentence 
import re
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
sample='People who own pets recommend the same to everyone. Pets are one of sweetest creation of nature.'
sentences=sent_tokenize(sample)
data=[]
for sentence in sentences:
    data=data+nltk.pos_tag(word_tokenize(sentence))
# I defined my grammar here on the basis of which i want to create the chunks 
grammar="Chunk:{<NN.?><WP><VB.?>}"
#Then i passed it to the RegularExpressionParser to apply this parsing criteria
parser=nltk.RegexpParser(grammar)
# Finally parsed my list naming data which contains POS tags for each word 
tree=parser.parse(data)
# To get a GUI view i used draw method to plot it in form of tree
tree.draw()

