import time

def ToHome():
    print("""
######################
#                    #
#      SOULSHELL     #
#  Just be yourself  #
#                    #
######################

Welcome to SoulShell - your personal diary via terminal.

Please, choose any option beneath:

1. Add a new chapter;
2. View a chapter;
3. Edit chapter;
4. Delete a chapter;
5. View all chapter;
6. Create a new notebook;
7. Delete a new notebook;
8. Exit.
""")

ToHome()

def ToTime():
    icons = ["|", "/", "-", "\\", "|"]
    i = 0
    while i < 5:
        print(f"\rLoading {icons[i%len(icons)]}", end="", flush=True)
        i += 1
        time.sleep(0.1)

    time.sleep(1)
    print("\nDone!")

def ToChoose():
    try:
        c = int(input("> "))

    except ValueError:
        print("There isn't this option.")
        return 8

    else:
         match c:
            case 1:
                ToTime()
                ToAddChapter()
            case 2:
                ToTime()
            case 3:
                ToTime()
            case 4:
                ToTime()
            case 5:
                ToTime()
            case 6:
                ToTime()
                ToAddNotebook()
            case 7:
                ToTime()
            case 8:
                print("Logout!")

def ToAddChapter():
    n = input("Which notebook?: ")
    pen = input("=>")
    with open(n+".txt", "a") as file:
        file.write(f"{pen}"+"\n")

def ToAddNotebook():
    n = input("What name do you wish to your new notebook?")
    try:
        f = open(n+".txt", "x")
    except FileExistsError:
        print("Ops! This notebook already exists.")
    else:
        print("Awasome! Your new notebook was created.")


ToChoose()
