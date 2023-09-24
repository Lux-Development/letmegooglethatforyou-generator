# Credits to: https://letmegooglethat.com/ for there amazing site :)

import webbrowser
import os

os.system("title joelb.services")

userinput = input("Enter google search query: ")
replaced = userinput.replace(' ', '+')
final = f"https://letmegooglethat.com/?q={replaced}"

print(f"Your link: {final}\n")
openquestion = input("Open link? (Y/N): ")

if (openquestion == "Y"):
    webbrowser.open(final)

os.system("pause")