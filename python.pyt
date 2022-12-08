lst = list(map(str, input("Enter phrases separated by commas: ").split(', ')))

for a in lst:
    phrase = (a.replace('of', '')).split()
    acronym = ""
    for word in phrase:
        acronym = acronym + word[0].upper()
    print(f'Acronym of "{a}" is {acronym}.')