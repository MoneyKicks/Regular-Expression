
# coding: utf-8

# In[14]:


#Chinking is use to extract a portion of sentence based on a set of grammar by defining some rules that must not 
# to be followed in the extracted portion. Whatever is to be excluded if defined between  }<Some Regular Exp. here>{
import re
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
sample='People who own pets recommend the same to everyone. Pets are one of sweetest creation of nature.'
sentences=sent_tokenize(sample)
data=[]
for sentence in sentences:
    data=data+nltk.pos_tag(word_tokenize(sentence))
# I defined my grammar here on the basis of which i want to create the chunks followed by chinks
grammar=r"""Chunk:{<.*>+} 
                        }<DT|W.*|VB.*|JJ.*>+{ """
#Then i passed it to the RegularExpressionParser to apply this parsing criteria
parser=nltk.RegexpParser(grammar)
# Finally parsed my list naming data which contains POS tags for each word 
tree=parser.parse(data)
# To get a GUI view i used draw method to plot it in form of tree
tree.draw()

