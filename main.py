import requests
print("What Type Of Jokes Do You Like?")
print("Select Options: \n1. Programming\n2. Misc\n3. Dark\n4. Pun\n5. Spooky\n6. Christmas\n")
TYPE = input()
url = f"https://v2.jokeapi.dev/joke/{TYPE}"
response = requests.get(url)
a = response.json()
if a['type'] == 'twopart':
    print(a['setup'])
    print(a['delivery'])
elif a['type'] == 'onepart':
    print(a['joke'])
