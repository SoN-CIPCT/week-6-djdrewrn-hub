# conditional lists
web_users = ['doc', 'grumpy', 'happy', 'sleepy', 'bashful']
new_users = ['sneezy', 'dopey', 'greg', 'sleepy', 'bashful']

for user in new_users:
    if user in web_users:
        print (f"{user}. This user name is already in use, please choose a different user name.")
    else:
        print (f"{user}. This user name is available.")

#nested dictionaries
#cities = {}
#   print (user.title)
