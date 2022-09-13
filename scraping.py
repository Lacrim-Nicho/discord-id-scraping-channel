import requests
import json

def scraper(jsonn): 
    x = 0
    i = len(jsonn)
    l = []

    while x < i:

        dizionario = jsonn[x]['author'] ['id'] 
        l.append(dizionario) 
        x+=1 

    stringa = '\n'.join(l)
    print(stringa, end='\n')


    f = open("users.txt", "a") 
    for users in l:
        f.write(users + '\n')
    f.close()

    


def main():

    header = {
        'authorization': '' #your token here
    }

    try:
        print()
        id = input(">>> channel id\n")

    except KeyError:
        print()
        print("canale non trovato")
        main()


    a = requests.get(f'https://discord.com/api/v9/channels/{id}/messages', headers=header) 

    json_load = (json.loads(a.text)) 

    scraper(json_load)





if __name__ == "__main__":
    main()