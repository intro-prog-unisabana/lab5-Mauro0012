import utils
tin=input("Please type your message\n")
print(f"Your encoded message is: {utils.flip(tin)}{utils.count_letters(tin, letter="a")}")
