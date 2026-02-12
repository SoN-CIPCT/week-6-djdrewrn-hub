# conditional lists
web_users = ['doc', 'grumpy', 'happy', 'sleepy', 'bashful']
new_users = ['sneezy', 'dopey', 'greg', 'sleepy', 'bashful']

for user in new_users:
    if user in web_users:
        print (f"{user}. This user name is already in use, please choose a different user name.")
    else:
        print (f"{user}. This user name is available.")

#nested dictionaries
cities = {}
 
cities['New York City'] = {'Country': 'United States', 'Population': '8.4 million', 'Fact': 'The Big Apple'}
cities['Tokyo'] = {'Country': 'Japan', 'Population': '9.2 million', 'Fact': 'The largest metropolitan area in the world'}
cities['Paris'] = {'Country': 'France', 'Population': '2.1 million', 'Fact': 'The City of Light'}

print(cities)
