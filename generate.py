from requests import get
import os

# Input fields
namewindowinp = input("Enter window name: ")
sizewindowinp = input("Enter the size of the window (example: 400x200): ")
colwindowinp = input("Enter window color(example: #F7E6AD): ")

# Create a .txt file and open it
my_file = open("compiled.txt", "w")

# Writing text from the pastebin to a variable
site = get("https://pastebin.com/raw/6SMGNUNu").text

# Replacing data
a = site.replace('NAMETITLE', namewindowinp)
b = a.replace('WINDOWSIZE', sizewindowinp)
c = b.replace('WINDOWCOLOR', colwindowinp)

# Writing text to .txt file with pastebin
my_file.write(c)
my_file.close()
# Change the file extension from .txt to .py
os.rename("compiled.txt", "compiled.py")
