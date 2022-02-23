# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


# alien_0 = {'color': 'green'}
# alien_color = alien_0.get('color')
# alien_points = alien_0.get('points',0)

# print(alien_color, alien_points)


# alien_0 = {'color':'green', 'points': 5}
# alien_0['x'] = 0
# alien_0['y'] = 25
# alien_0['speed'] = 1.5


# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# alien_0['color'] = 'yellow'
# alien_0['points'] = 10

# print(alien_0)

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# fav_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# for name, language in fav_languages.items():
#     print(f"{name}: {language}")

# # for name in fav_languages.keys():
# #     print(name)

# # for language in fav_languages.values():
# #     print(language)

# for name in sorted(fav_languages.keys(), reverse=True):
#     print(f"{name}: langugae")


# print(len(fav_languages))


# users = []

# new_user = {
#     'last': 'fermi',
#     'first': 'enrico',
#     'username': 'efermi',
# }

# users.append(new_user)

# new_user = {
#     'last': 'curie',
#     'first': 'marie',
#     'username': 'mcurie',
# }

# users.append(new_user)

# for user_dict in users:
#     for k, v in user_dict.items():
#         print(f"{k}: {v}")
#     print("\n")



users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi',
    },
    {
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie',
    }
]

for user_dict in users:
    for k, v in user_dict.items():
        print(f"{k}:{v}")
    print("\n")


fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}


for name, langs in fav_languages.items():
    print(f"{name}: ")
    for lang in langs: 
        print(f"- {lang}")


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")



###### Dictionary Comprehensions ######

# squares = {}
# for x in range(5):
#     squares[x] = x**2
# print(squares)

# squares = {x:x**2 for x in range(5)}
# print(squares)

group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']

group_3 = zip(group_1, group_2)

print(group_3)

pairings = {name: name_2 for name, name_2 in zip(group_1, group_2)}
print(pairings)


aliens = []

for alien_num in range(10):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0 
    aliens.append(new_alien)

num_aliens = len(aliens)
print(num_aliens, aliens)