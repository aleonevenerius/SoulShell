home = """
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
6. Exit.
"""
print(home)

def ToChoose():
    try:
        c = int(input("> "))
    
    except ValueError:
        print("There isn't this option.")
        return 6
ToChoose()
