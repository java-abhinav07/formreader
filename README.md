# Attention Based OCR Model

This OCR pipeline attempts to detect text in a cropped handwritten forms. In order to convert cropped form data to text, synthetic data of the required type was generated and trained using a modified version of the attention OCR model.<br>

![Sample prediction on real data](resources/image_2.gif)<br>
```Sample prediction on real data```


To reproduce the results of the pipeline on test data kindly refer ```instructions.txt``` and for a details about the analysis, comparison and hyperparameter tuning of the neural network refer ```report.pdf```. A log report, ```log.md``` has also been included in this repository which constains succinct description of  daily work done.

## Folder Structure
---
Find the folder tree below. Note that some details have been omitted for brevity and can be found in the respective repositories of the source code, kindly refer a separate ```README.md``` in such cases.
```
Root<br>
|
| .gitignore
| requirements.txt
| log.md
| README.md
| MANIFEST.in
| setup.py
| instructions.md
| myrun.sh
|
|___aocr
|   |
|   | __main__.py
|   | __init__.py
|   | defaults.py
|   | LICENSE.md
|   | README.md
|   |
|   |____model
|   |    |
|   |    | __init__.py
|   |    | cnn.py
|   |    | model.py
|   |    | seq2seq.py
|   |    | seq2seq_model.py
|   |
|   |____util
|        | 
|        | __init__.py
|        | bucketdata.py
|        | data_gen.py
|        | dataset.py
|        | export.py
|        | visualizations.py  
|     
|___text_renderer
|   |
|   | main.py
|   | README.md
|   | setup.py
|   |
|   |____dataset_labels
|   |    |
|   |    | convert_labels.py
|   |
|   |____ocr_data
|   |
|   |____example_data
|   |
|   |____text_renderer
|   |
|   |____tools
|   |
|   |____docs
|   |
|   |____docker
|   
|
|____experiments
    |
    | TestSyntheticDataGen.ipnb
    | Tfwriter.ipnb
    | Train.ipnb

```
1. The folder ```aocr``` contains the main code for the attention ocr along with a separate ```README.md``` which can be used as a reference. 
2. The folder ```text_renderer``` contains the code used for generation of synthetic dataset. The exact details of configuration used is inside ```text-renderer/ocr_data/gen_data.py```.
3. Since this model was trained and tested on Google Colab, sample ```ipnb``` files have been provided for reference in ```experiments```.
4. And the app folder contains the flask based REST API for testing the endpoints


## Reproduce results on local machine
---




## References
---
This repository contains code from the following two repositories:<br>
1. https://github.com/emedvedev/attention-ocr : aocr
2. https://github.com/oh-my-ocr/text_renderer : text_renderer

The reports contains a list of papers which were referenced during the design of this ocr rendition.
