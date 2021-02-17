unregistered_players = ['Frank','Pieter','Shaun','Aiden']
registered_players = []

while unregistered_players:
    current_player=unregistered_players.pop()
    print(f"Verifying player ID: {current_player.title()}")
    registered_players.append(current_player)

print("\nThe following players have been registered for the matchday squad:")
for registered_player in registered_players:
    print(registered_player.title())