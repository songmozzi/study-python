from programmer import Programmer
# from actor import Actor
# from farmer import Farmer


# dave = Programmer("Dave", 42, "Python")
# dave.introduce()
# song = Actor("Song", 55, "Parasite")
# song.introduce()
# kim = Farmer("Kim", 40, "Apple")
# kim.introduce()


# people = [
#         Programmer("Dave", 42, "Python"), 
#         Actor("Song", 55, "Parasite"), 
#         Farmer("Kim", 40, "Apple")
# ]
# for person in people:
#     person.introduce()

dave = Programmer("Dave", 42, "Python")
dave.__age = -1
dave._hello()
 