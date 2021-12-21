import random
import sys

import pyfiglet
from colorama import Fore,Style
import os
all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)



def banner():
    os.system("clear")

    print(ran, pyfiglet.figlet_format("\tWordList\n\tGen"))
    print(ran + "\t\tV_3.0\t\n\n")
    print("*" * 63)

    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
    print("\n", "*" * 63)

banner()




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
                file.write(id + id + "\n")
                file.write(dob + id + "\n")
                file.write(id + p_num + "\n")
                file.write(id + company + "\n")
                file.write(id + any + "\n")
                file.write(id + city + "\n")
                file.write(city + dob + "\n")
                file.write(city + p_num + "\n")
                file.write(any + city + "\n")
                file.write(dob + country + "\n")
                file.write(dob + any + "\n")
                file.write(ig + any + "\n")
                file.write(ig + "\n")
                file.write(dob + "\n")
                for i in range(amount):
                        r_num = random.randint(0000, 99999)
                        r_num = str(r_num)

                        file.write(id+r_num+"\n")
                        file.write(p_num+r_num+"\n")
                        file.write(ig+r_num+"\n")
                        file.write(dob+r_num+"\n")
                        file.write(company+r_num+"\n")
                        file.write(city+r_num+"\n")
                        file.write(country+r_num+"\n")
                        file.write(any+r_num+"\n")


                        file.write(r_num+any+"\n")
                        file.write( r_num+id +"\n")
                        file.write( r_num+ p_num+"\n")
                        file.write( r_num+ ig)
                        file.write(r_num+dob+"\n")
                        file.write( r_num+ company+"\n")
                        file.write( r_num+ city+"\n")
                        file.write(r_num +country +"\n")
                        file.write(r_num + r_num + "\n")

                        file.write(r_num + any+"\n")

                print(ran + "\nSaved in passswords.txt")


        else:

                print(ran + "\n\t\tWait it might take some seconds- - - - - -")
                file = open("passwords.txt", "a+")
                file.write(id + id + "\n")
                for i in range(amount):
                            r_num = random.randint(1000, 9999)
                            r_num = str(r_num)
                            file = open("passwords.txt", "a+")
                            file.write(id + r_num + "\n")
                            file.write(r_num + r_num + "\n")

                            file.write(r_num+id + "\n")

                print(ran + "\nSaved in passswords.txt")

def view():
    file = open("passwords.txt","r")
    read = file.read()
    print(ran + "\n\t\tThis is what i found: \n")

    print(all_col[2%6] + read)

cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Generate Passwords\n\t\t[2] View Generated passwords\n\t\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        program()

    elif choice == "2":
        view()
    elif choice == "3":
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

