import os
FILE = "file.txt"
print("options:\n\tadd\n\tremove")
choice = input("option:")
if choice.lower() == "add":
    newip = str(input("New ip to add to whitelist: "))
    confirm = input(f"confirm that {newip} is correct? [Y/N]")
    if confirm.lower() in ["y", "yes"]:
        try:
            os.system(f"sudo ufw allow from {newip} to any port 22 proto tcp")
            print(f"{newip} added to the whitelist")
        except:
            print("something went wrong")
    elif confirm.lower() in ["n", "no"]:
        print("aborted.")
    else:
        print("aborted.")
if choice.lower() == "remove":
    oldip = str(input("Old ip to remove from whitelist: "))
    confirm = input(f"confirm that {oldip} is correct? [Y/N]")
    if confirm.lower() in ["y", "yes"]:
        try:
            os.system(f"sudo ufw delete allow from {oldip} to any port 22 proto tcp")
            print(f"{oldip} removed from the whitelist")
        except:
            print(f"{oldip} is not on the whitelist")
    elif confirm.lower() in ["n", "no"]:
        print("aborted.")
    else:
        print("aborted.")
