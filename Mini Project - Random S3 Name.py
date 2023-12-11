#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Simple script to create random S3 Bucket names based on user input of preferred length of S3 bucket name, user's department and number of S3 buckets needed.

import string
import random

num_buckets = int(input('How many S3 Buckets do you want to launch?'))
dept_name= input('What department are you in?')
dept_name_length = len(dept_name)
length = int(input('How long do you want your S3 name to be?'))
for i in range(1,num_buckets+1):
    digits = ''.join(random.choices(string.ascii_uppercase + string.digits, k=(length - dept_name_length)))
    random_name = str(digits) + dept_name
    print(random_name)
    


# In[2]:


##Function to create random S3 Bucket names based on user input of preferred length of S3 bucket name, user's department and number of S3 buckets needed.
import string
import random

def final_names():
    num_buckets = int(input('How many S3 Buckets do you want to launch? '))
    dept_name = input('What department are you in? ')
    length = int(input('How long do you want your S3 name to be? '))

    generated_names = generate_s3_names(num_buckets, dept_name, length)

    print("Your Random S3 Bucket Names:")
    for name in generated_names:
        print(name)

def generate_s3_names(num_buckets, dept_name, desired_length):
    dept_name_length = len(dept_name)
    s3_names = []

    for i in range(1, num_buckets + 1):
        random_letters = ''.join(random.choices(string.ascii_uppercase + string.digits, k=(desired_length - dept_name_length)))
        random_name = random_letters + dept_name
        s3_names.append(random_name)

    return s3_names
     

final_names()


# In[ ]:




