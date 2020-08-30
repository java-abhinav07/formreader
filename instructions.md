## Instructions
---
Please execute the following instructions step by step to reproduce the results of this repository on your data:

1. Clone the repository on your local machine:<br>

    ```git clone https://github.com/java-abhinav07/abhinav_java_9873155323-IITB-Assignment-Jul-Dec2020-Batch2.git```

2. Install aocr locally using ```setup.py```:<br>

    1. ```cd abhinav_java_9873155323-IITB-Assignment-Jul-Dec2020-Batch2```
    2. ```pip(3) install -e``` <br>

3. Install necessary packages:<br>

    ```pip3 install -r requirements.txt```

4. Prepare your datasets:<br>
    In order to test the model the datasets needs to be in tfrecords format, and must have dimensions ```width < 320```. Note that maximum width argument can be set during testing (default: 320)
    1. Create new directory called ```datasets/images```:<br>
            -- ```cd datasets```<br>
            -- ```mkdir images```<br>
            -- ```cd ..```
    2. Add all images in ```datasets/images```. Also include an annotation file in this directory such that ```datasets/annotation-testing.txt``` is its relative path. Annotations should be in the format:<br>
            -- ```relative_path/image_name.extension label```
       
    3. Make TfRecords file:<br>
    -- ```aocr dataset ./datasets/annotations-testing.txt ./datasets/testing.tfrecords```
    Subsequently the tfrecords will be written to the ```testing.tfrecords``` file

5. Testing:<br>
    ```aocr test ./datasets/testing.tfrecords --full-ascii --use-gru --model-dir ./checkpoint```
    The list of optional arguments can be found in ```./aocr/README.md``` and the output will be in a folder ```./predictions/output.txt```.
    

