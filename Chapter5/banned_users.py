banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

#if user in banned_users:
 #   print(f"{user.title()}, you can post a response if you wish.")
#else:
#    print(f"{user.title()}, you cannot post a response.")

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()}, you cannot post a response.")