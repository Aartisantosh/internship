#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re



# In[43]:


#1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


# In[44]:


#2. Write a Python program that matches a string that has an a followed by zero or more b's
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))


# In[26]:


# Write a Python program that matches a string that has an a followed by one or more b's
pattern='ab+?'
text="ac abc abbbc abbbb"
matches=re.findall(pattern,text)
print(matches)


# In[ ]:





# In[27]:


#4) Write a Python program that matches a string that has an a followed by zero or one 'b'
pattern='ab?'
text="ac abc abbbc abbbb"
matches=re.findall(pattern,text)
print(matches)


# In[28]:


#5) Write a Python program that matches a string that has an a followed by three 'b'
pattern='ab{3}?'
text="ac abc abbbc abbbb"
matches=re.findall(pattern,text)
print(matches)


# In[29]:


#6) Write a Python program that matches a string that has an a followed by two to three 'b'.
pattern='ab{2,3}?'
text="ac abc abbc abbbb"
matches=re.findall(pattern,text)
print(matches)


# In[34]:


#7) Write a Python program to find sequences of lowercase letters joined with a underscore.
pattern='^[a-z]+_[a-z]+$'
text="abc_def xyz_Abc asdgfhj adgsgt_sf"
result=re.search(pattern,text)
print(result)


# In[42]:


# 8)Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if not re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


# In[16]:


#9) Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))


# In[17]:


#10) Write a Python program that matches a word at the beginning of a string.
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))


# In[ ]:




