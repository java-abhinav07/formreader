import os
import json
import random

with open(
    "/home/abhinavjava/Projects/IITB_Assignment/dataset/ds2/labels.json", "r"
) as f:
    data = json.loads(f.read())
    # num_samples = data["num_samples"]
    label_dict = data["labels"]

train_dict = dict(list(label_dict.items()))
# test_dict = dict(list(label_dict.items())[-len(label_dict) // 20 :])


train_json = json.dumps(train_dict)
# test_json = json.dumps(test_dict)

with open(
    "/home/abhinavjava/Projects/IITB_Assignment/dataset/ds2/annotations-training.txt",
    "a",
) as f:
    for key, val in train_dict.items():
        f.write("ds2/images/" + key + ".jpg")
        f.write(" ")
        f.write(val)
        f.write("\n")

# with open(
#     "/home/abhinavjava/Projects/IITB_Assignment/dataset/ds1/annotations-testing.txt",
#     "a",
# ) as f:
#     for key, val in test_dict.items():
#         f.write("ds1/images/" + key + ".jpg")
#         f.write(" ")
#         f.write(val)
#         f.write("\n")
