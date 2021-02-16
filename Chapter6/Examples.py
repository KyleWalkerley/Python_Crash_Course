#person_0 = {'first_Name': 'Piet','last_Name': 'Pampoen','eye_Color': 'blue', "age":26}

#print(f"His name is {person_0['first_Name']}")
#print(f"His surname is {person_0['last_Name']}")
#print(f"He has {person_0['eye_Color']} eye color")
#print(f"His current age is{person_0['age']}")

#for key, value in person_0.items():
    #print(f"\nKey: {key}")
    #print(f"Value: {value}")


#favorite_Foods = {
    #'Frikkie':['Burger', 'Steak'],
    #'Sara':['Bacon'],
    #'Ewald':['Nik Naks','Potatoes'],
    #'Juan':['Sushi','Pizza','Salami','McDonalds'],

#}
#for name, Foods in favorite_Foods.items():
    #print(f"\n{name.title()}'s favorite foods are:")
    #for Food in Foods:
       # print(f"\t{Food.upper()}")

users = {
    'ppompies': {
        'first': 'piet',
        'last': 'pompies',
        'nickname': 'Papgooi',
    },

    'jcena': {
        'first': 'john',
        'last': 'cena',
        'nickname': 'CenaNiks',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    nick_name = user_info['nickname']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tNick name: {nick_name.title()}")


