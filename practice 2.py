#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install nltk


# In[6]:


import nltk
nltk.download('vader_lexicon')


# In[7]:


from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text = "I love this product! It's amazing."
print(sia.polarity_scores(text))


# In[9]:


sentence = "This movie was amazing, but the acting was a bit disappointing."
sentiment_scores = sia.polarity_scores(sentence)
print(sentiment_scores) 


# In[ ]:





# In[ ]:




