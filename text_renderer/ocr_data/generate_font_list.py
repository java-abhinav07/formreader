import os

with open("./font_list/font_list.txt", "w") as f:
    for name in os.listdir("./font"):
        f.write(name)
        f.write("\n")
