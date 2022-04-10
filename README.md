# undergrad-final-project-2022

Improved version of my final undergraduate project.

To run the model and evaluate it, just run

`make all`

More about the commands inside the Makefile (about run, download, install and more.)

It will download the FER2013 dataset, transform it into images (that can be
visualized by the user inside its folders), and later serve as the input for
the machine learning model.

# Sample Images from TestSet
![Sample](imgs/sample.jpg)

# Results from the model
![Results](imgs/output.jpg)

### TODO
- [ ] Add Architecture picture
- [x] Add model evaluation
- [ ] Add support for live evalution of emations using OpenCV

### Future Improvements

- [ ] Hyperparameter Optimization
- [ ] Data Augmentation
- [ ] Use Another Dataset to improve results
