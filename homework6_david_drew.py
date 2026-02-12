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
 
cities['New York City'] = {'Country': 'United States', 'Population': 8400000 , 'Fact': 'The Big Apple'}
cities['Tokyo'] = {'Country': 'Japan', 'Population': 9200000, 'Fact': 'The largest metropolitan area in the world'}
cities['Paris'] = {'Country': 'France', 'Population': 2100000, 'Fact': 'The City of Light'}

print(cities)
