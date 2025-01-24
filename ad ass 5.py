#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter
import re

def word_frequency(text):
    
    text = text.lower()
    
   
    words = re.findall(r'\b\w+\b', text)
    
    
    word_count = Counter(words)
    
    
    for word, count in word_count.items():
        print(f"'{word}': {count}")


text = """Hello world! Hello everyone. This is a simple test. 
          Testing word frequency, hello."""
word_frequency(text)


# In[ ]:




