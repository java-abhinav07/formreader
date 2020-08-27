
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
    1. Testing of best model complete!
    1. Added testing, training logs
    1. Added result samples + visualizations
    1. Train-Test distribution was same, need public dataset to evaluate properly
    1. Starting to implement modified aocr 
1. 26/08/2020
    1. The results indicate that the network is unable to generalize on assignment data and the dataset used for training is not desirable
    1. The network performs well on my testdata (97% acc)
    1. Made more realistic data
    1. Training again
    1. Testing+Training complete, much better results on sample data however still scope for a lot of improvement
    1. Improvement areas noted: a) Size of attention mask b) Dataset!  
    1. Resuls still poor on new dataset, model attending to the vertical separators instead of text, overfitting
    1. Retraining with lower model complexity: params tweaked
    1. Accuracies on sample data largely improved, testing on public data. Still scope for improvement
    1. Making model complexity lower makes results worse, attention mask too small, not learned properly. Need to tune further and generate new images
    1. Despite multiple rounds of hyperparameter tuning and even with a dataset very similar to the original pubic dataset the accuracy on the public dataset is poor **due to small size of the attention mask/sliding window.**
1. 27/08/20
    1. Implementing the modified network to accomodate a larger window and location aware attention