#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk


# In[2]:


from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
words = ['cared','university','fairly','easily','singing','sung','sings','singer']
st = LancasterStemmer()
print("LancasterStemmer")


# In[3]:


stem_words=[]
for w in words:
    x=st.stem(w)
    stem_words.append(x)
for e1,e2 in zip(words,stem_words):
    print(e1+'-------->'+e2)


# In[3]:


from nltk.stem import WordNetLemmatizer


# In[4]:


import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')


# In[5]:


lemmatizer=WordNetLemmatizer()


# In[7]:


words=['cared','university','fairly','easily','singing','sung','sings','singer']
pos='v'
print("WordNetLemmatizer")


# In[8]:


stem_words = []
for w in words:
    x=lemmatizer.lemmatize(w,pos="v")
    stem_words.append(x)
for e1,e2 in zip(words,stem_words):
    print(e1+'-------->'+e2)


# In[2]:


import nltk


# In[6]:


nltk.download('averaged_perceptron_tagger')


# In[4]:


if __name__=="__main__":
    sentence="we saw the yellow dog"
    tokens=nltk.word_tokenize(sentence)
    print(tokens)
    


# In[3]:


get_ipython().system('pip install spacy')


# In[9]:


import nltk

# Download necessary data files (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

if __name__ == "__main__":
    sentence = "We saw the yellow dog"
    
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    print("Tokens:", tokens)

    # Part-of-Speech (POS) tagging
    tagged = nltk.pos_tag(tokens)
    print("POS Tags:", tagged)

    # Named Entity Recognition (NER)
    entities = nltk.chunk.ne_chunk(tagged)
    print("Named Entities:", entities)


# In[ ]:




