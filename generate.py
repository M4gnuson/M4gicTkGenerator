from requests import get
import os


namewindowinp = input("Введите имя окна: ")
sizewindowinp = input("Введите размер окна(пример: 400x200): ")
colwindowinp = input("Введите цвет окна(пример: #F7E6AD): ")

# Create a .txt file and open it
my_file = open("compiled.txt", "w")

site = get("https://pastebin.com/raw/6SMGNUNu").text

a = site.replace('NAMETITLE', namewindowinp)
b = a.replace('WINDOWSIZE', sizewindowinp)
c = b.replace('WINDOWCOLOR', colwindowinp)

# Writing text to .txt file with pastebin
my_file.write(c)
my_file.close()
# Change the file extension from .txt to .py
os.rename("compiled.txt", "compiled.py")