import random
import sys
from colorama import Fore
import pyfiglet

import os
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
all_col = [red, green, orange, cyan, lightred, lightgreen, yellow, lightcyan,lightblue,pink]
ran = random.choice(all_col)


def banner():
        os.system("clear")
        en = pyfiglet.figlet_format("Password\nGenerator\n")
        print(ran, en)
        print(ran + "\n\t\tV_1.0\t\n\n")

        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)


banner()
r_num = random.randint(1000,9999)
r_num=str(r_num)


def exit():
    sys.exit()


def program():
        id = input(ran+"\nEnter the name of victim: ")
        amount = input(ran+"\nEnter the amount of passwords:")
        amount = int(amount)
        comf = input(ran+"\nDo you want to add more information? [y/n]: ")
        if comf == "y":
                p_num = input(ran+"\nEnter any specific short number: ")
                ig = input(ran+"\nEnter id name: ")
                dob = input(ran+"\nEnter Date of birth or month name: ")
                company = input(ran+"\nEnter comapany name: ")
                city = input(ran+"\nEnter city name: ")
                country = input(ran+"\nEnter Country: ")
                any = input(ran+"\nEnter Any specific piece of information: ")

                print(ran+"\n\t\tWait it might take some seconds- - - - - -")
                file = open("passwords.txt", "a+")
                for i in range(amount):

                        file.write(id+r_num+"\n")
                        file.write(p_num+r_num+"\n")
                        file.write(ig+r_num+"\n")
                        file.write(dob+r_num+"\n")
                        file.write(company+r_num+"\n")
                        file.write(city+r_num+"\n")
                        file.write(country+r_num+"\n")
                        file.write(any+r_num+"\n")
                        file.write(p_num+id+"\n")
                        file.write(dob + id+"\n")
                        file.write(id+p_num+"\n")
                        file.write(id+company+"\n")
                        file.write(id+any+"\n")
                        file.write(id+city+"\n")
                        file.write(city+dob+"\n")
                        file.write(city+p_num+"\n")
                        file.write(any+city+"\n")
                        file.write(dob+country+"\n")
                        file.write(dob+any+"\n")
                        file.write(r_num+any+"\n")
                        file.write( r_num+id +"\n")
                        file.write( r_num+ p_num+"\n")
                        file.write( r_num+ ig)
                        file.write(r_num+dob+"\n")
                        file.write( r_num+ company+"\n")
                        file.write( r_num+ city+"\n")
                        file.write(r_num +country +"\n")
                        file.write(r_num + r_num + "\n")
                        file.write(id + id + "\n")
                        file.write(r_num + any+"\n")
                        file.write(ig+ any + "\n")
                        file.write(ig+ "\n")
                        file.write(dob+"\n")





        else:

                print(ran + "\n\t\tWait it might take some seconds- - - - - -")
                file = open("passwords.txt", "a+")
                for i in range(amount):
                            file = open("passwords.txt", "a+")
                            file.write(id + r_num + "\n")
                            file.write(r_num + r_num + "\n")
                            file.write(id + id + "\n")
                            file.write(r_num+id + "\n")



                print(ran + "\nSaved in passswords.txt")





cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Generate Passwords\n\t\t[2] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        program()
    elif choice == "2":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()

