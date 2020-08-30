import os
from PIL import Image
from tqdm import tqdm

r = "dataset/images_temp"
save_path = "dataset/images"

if not os.path.isdir(r):
    print("Kindly follow all the instructions in sequencial manner, dataset directory not found.")

basewidth = 320

for im in tqdm(os.listdir(r)):
    img = Image.open(os.path.join(r1, im))  
    width, height = img.size
    # print(width, height)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    img.save(os.path.join(save_path, im))

# for im in os.listdir(r2):
#     try:
#         img = Image.open(os.path.join(r2, im))  
#         width, height = img.size
#         print(width, height)
#         wpercent = (basewidth / float(img.size[0]))
#         hsize = int((float(img.size[1]) * float(wpercent)))
#         img = img.resize((basewidth, hsize), Image.ANTIALIAS)

#         img.save(os.path.join(r2, im))
#     except:
#         print("not found")


# for im in os.listdir(r3):
#     img = Image.open(os.path.join(r3, im))  
#     width, height = img.size
#     print(width, height)
#     wpercent = (basewidth / float(img.size[0]))
#     hsize = int((float(img.size[1]) * float(wpercent)))
#     img = img.resize((basewidth, hsize), Image.ANTIALIAS)

#     img.save(os.path.join(r3, im))
