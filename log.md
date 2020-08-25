
## Daily Logs

This file contains daily logs of work done in a sequential manner. For example, <br>
```1 denotes day one, ie 22/08/2020 and the subtasks will be listed as i, ii and so on.```
<br><br>
***

1. 22/08/2020
    1. Initialized empty repository with gitignore, readme and logfile
    1. Understanding problem statement and researching 
1. 23/08/2020
    1. Further research
    1. Fixing roadblocks in synth datagenerator
    1. Made bounding box on the entire text, need to make it per char
    1. Fixed PIL error, successfully made bboxes around each char
    1. Lighting, perspective, noise, padding added ---> moving to tfrecords
1. 24/08/2020
    1. Selected best handwritten fonts, various backgrounds
    1. 50k images generated
    1. Started working on tfrecords for attention-net (target start training by 24th)
    1. Fixing training errors
    1. Fixed training errors, started training: loss 0.001 after 30k steps
    1. Fixing dataset: only alphanumeric (acc to problem statement)
1. 25/08/2020
    1. Preparing dataset again
    1. Colab useage limit exceeded
    1. Made new branch for testing the modified aocr: need to train both!
    1. Training the aocr completed, onto testing the best model 