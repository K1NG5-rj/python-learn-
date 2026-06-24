import time
import os
import shutil

merry_christmas = [
        (0, "Merry Christmas, i miss you - Alex Crichton"),
        (3, "But what if I call"),
        (7.5, "And you pick up the phone?"),
        (12, "And I use this holiday"),
        (15, "To make my way to your ghost"),
        (20, "")
]

from colorama import Fore

print(Fore.BLUE)

def ketik(teks):
    os.system("cls")
    ukuran = shutil.get_terminal_size()

    lebar = ukuran.columns
    tinggi = ukuran.lines

    print("\n" * (tinggi // 2))

    print(" " * ((lebar - len(teks)) // 2), end="")
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(0.05)

start = time.time()

for detik, lirik in merry_christmas:
    while time.time() - start < detik:
        time.sleep(0.01)
    ketik(lirik)    