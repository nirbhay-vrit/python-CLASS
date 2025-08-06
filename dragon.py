def attack_dragon(attack_type):
    if attack_type == "punch":
        return 15
    elif attack_type == "kick":
        return 25
    elif attack_type == "magic":
        return 50
    else:
        print("You missed your turn!")
        return 0

def dragon_battle():
    total_damage = 0


    for i in range(3):
        try:
            move = input(f"Turn {i+1}: Choose your attack (punch/kick/magic): ").lower()
            damage = attack_dragon(move)
            total_damage = total_damage + damage
            print(f"You dealt {damage} damage!\n")
        except Exception as e:
            print("Something went wrong!", e)
        finally:
            print(f"You have {3-(i+1)} chances left")
    
    print(f"Total damage dealt: {total_damage}")
    if total_damage >= 100:
        print("You defeated the dragon!")
    else:
        print("The dragon flew away... You need more power next time!")
    print("Game Over.")

dragon_battle()
