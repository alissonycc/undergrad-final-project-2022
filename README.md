# undergrad-final-project-2022

Improved version of my final undergraduate project.

To run the model and evaluate it, just run

`make run`

To perform the emotion recognition task using your camera, run

`make cam`

More about the commands inside the Makefile (about run, download, install and more.)

It will download the FER2013 dataset, transform it into images (that can be
visualized by the user inside its folders), and later serve as the input for the machine learning model.

# Sample Images from TestSet
![Sample](imgs/sample.jpg)

# Architecture of the model
![ModelArch](imgs/model_plot.png)

# Results of the model
![Results](imgs/output.jpg)

### TODO
### Future Improvements

- [ ] Hyperparameter Optimization
- [ ] Data Augmentation
- [ ] Use Another Dataset to improve results
- [ ] Architecture Optimization
- [ ] Tranfer Learning

These are all possible improvements for this approach, while the 2nd and 3rd seems to be the most promissing, at a first glance. The 1st, 4th and 5th possible improvements were tried, but not significant improvements were assessed during the experiments.
