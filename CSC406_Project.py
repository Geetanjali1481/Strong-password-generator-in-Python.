#!/usr/bin/env python
# coding: utf-8

# ## Name: Geetanjali Sharma

# ## 1. A brute force attack 

# In[3]:


from random import *
def brute_force_password_cracker():

    # taking input from user
    user_pass = input("Enter your password-> ")

    # storing alphabet letter to use thm to crack password
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                'w', 'x', 'y', 'z',]

    # initializing an empty string
    guess = ""

    counter = 0

    # using while loop to generate many passwords untill one of
    # them does not matches user_pass
    while (guess != user_pass):
        guess = ""
        counter += 1
        # generating random passwords using for loop
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 25)]
            guess = str(guess_letter) + str(guess)
        # printing guessed passwords
        print(guess)

    # printing the matched password
    print("\nYour password is:",guess)
    print("\nThe number of attempts to guess the user's password:", counter)


# In[4]:


brute_force_password_cracker()


# This brute force attack was able to guess a weak password in only about 5364 attempts. 

# ## 2. A possible defend (secure password generator).

# In[12]:


def strong_password_generator():
    
    #taking user input
    user_password = input("Enter a password-> ")
    
    #logic to check if there is at least one uppercase character in the user-typed password
    upper = False
    
    for i in user_password:
        if i.isupper():
            upper = True
            break 
    
    #logic to check if there is at least one lowercase character in the user-typed password
    lower = False
    
    for j in user_password:
        if j.islower():
            lower = True
            break
            
    #logic to check if there is at least one number in the user-typed password
    number = False
    
    for k in user_password:
        if k.isdigit():
            number = True
            break
      
    #logic to check if there is at least one special character in the user-typed password
    
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*'] #list of special characters
    
    character = False
    
    for l in user_password:
        if l in special_char:
            character = True
            break
            
    #checking if the user's password fulfills all the criteria for a strong password
    if len(user_password) >= 12 and upper == True and lower == True and number == True and character == True:
        print("You have successfully created a strong password!\n")
        print("Your password is:", user_password)
       
    elif len(user_password) <= 12:
        print("Invalid password!\n")
        print("Your password should be at least 12 characters long!")
        
    elif upper == False:
        print("Invalid password!\n")
        print("Your password should contain at least one uppercase character!")
    
    elif lower == False:
        print("Invalid password!\n")
        print("Your password should contain at least one lowercase character!")
        
    elif number == False:
        print("Invalid password!\n")
        print("Your password should contain at lease one number!")
        
    else:
        print("Invalid password!\n")
        print("Your password should contain at least one special character!")


# In[13]:


strong_password_generator()


# In[14]:


strong_password_generator()


# In[15]:


strong_password_generator()


# In[16]:


strong_password_generator()


# In[17]:


strong_password_generator()


# ## Using the brute force attack after generating a strong password using the defense program.

# In[ ]:


brute_force_password_cracker()


# This brute force attack was not able to guess the password generated by the defense program.

# In[ ]:




