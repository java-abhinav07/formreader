import os
import json
import random


with open("/home/abhinavjava/Projects/IITB_Assignment/dataset/final_realistic/labels.json", "r") as f:
    data = json.loads(f.read())
    # num_samples = data["num_samples"]
    label_dict = data["labels"]

train_dict = dict(list(label_dict.items())[len(label_dict) // 20 :])
test_dict = dict(list(label_dict.items())[: len(label_dict) // 20])


train_json = json.dumps(train_dict)
test_json = json.dumps(test_dict)

with open("annotations-training.txt", "w") as f:
    for key, val in train_dict.items():
        f.write("final_realistic/images/" + key + ".jpg")
        f.write(" ")
        f.write(val)
        f.write("\n")

with open("annotations-testing.txt", "w") as f:
    for key, val in test_dict.items():
        f.write("realistic_alpha/images/" + key + ".jpg")
        f.write(" ")
        f.write(val)
        f.write("\n")
