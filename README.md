# CNN+Transformer Model
The CNN+Transformer architecture consists of a MobileNetv2 convolutional neural network (CNN) for feature extraction concatenated with a bi-layer Transformer-Encoder network.  
![figure2](https://user-images.githubusercontent.com/44348827/120879105-f825bb80-c575-11eb-935d-330fbcb9f16a.png)

**NOTE:** The content of this code repository is for research purposes only and is not intended for clinical use of any kind, including but not limited to diagnosis or prognosis.

## Paper
_Toward Reduction in False-Positive Thyroid Nodule Biopsies with a Deep Learning–based Risk Stratification System Using US Cine-Clip Images_
Rikiya Yamashita, Tara Kapoor, Minhaj Nur Alam, Alfiia Galimzianova, Saad Ali Syed, Mete Ugur Akdogan, Emel Alkim, Andrew Louis Wentland, Nikhil Madhuripan, Daniel Goff, Victoria Barbee, Natasha Diba Sheybani, Hersh Sagreiya, Daniel L. Rubin, and Terry S. Desser
Radiology: Artificial Intelligence 2022 4:3   

Published Online: May 11 2022  
DOI: https://doi.org/10.1148/ryai.210174  
Citations on google-scholar: https://scholar.google.com/scholar?oi=bibs&hl=en&cluster=3541439675105718208 

## Dataset
Download Thyroid Ultrasound Cine-clip, containing ultrasound cine-clip images, radiologist-annotated segmentations, patient demographics, lesion size and location, TI-RADS descriptors, and histopathological diagnoses at https://stanfordaimi.azurewebsites.net/datasets/a72f2b02-7b53-4c5d-963c-d7253220bfd5   
See further details [data](data).

## Clone repository
After generating your SSH keys as suggested [here](https://github.com/mxochicale/tools/blob/main/github/SSH.md).
You can then clone the repository by typing (or copying) the following line in a terminal at your selected path in your machine:
```
mkdir $HOME/repositories/github-projects && cd $HOME/repositories/github-projects
git clone git@github.com:mxochicale/thyroid_deep_learning.git
```

## Files
**configtest.yaml:**
Contains pre-set variables for CNN model development (e.g. learning rate, batch size) for model as well as variables updated during model training automatically (e.g. probability prediction threshold, lowest validation loss epoch). Do not manually update.

**configtransformer.yaml:**

Contains pre-set variables for Transformer model development (e.g. learning rate, batch size) for model as well as variables updated during model training automatically (e.g. probability prediction threshold, lowest validation loss epoch). Do not manually update.

--------
**mobilenet_preprocess.py:**

Contains functions (crop_bounding_box, transform_and_crop_new, transform_and_crop_largest) for cine-clip video frame preprocessing: cropping images around masks (covering nodule) with 5 pixel buffer and resizing to 224x224.

**mobilenet_dataset.py:**

Create CNN model dataset. Function load_datasets_new for loading CNN inputs: sorting images into cross validation folds and stacking 3 images at a time into input instances along with corresponding labels and patient IDs.
DataLoader (DatasetThyroid3StackedNew custom class) calls functions from **mobilenet_preprocess** file to load images, then feeds them into load_datasets_new (use all frames) or load_datasets_single_frame (stack each patient's largest frame +-1) function to get CNN inputs.

**train_cnn.py:**

Train CNN model. Called twice by **cnn_main** file: once to train on only train data and determine lowest validation loss epoch (trainval false); then to train until that epoch on training and validation data (trainval true).
Setup MobileNetv2 model with all layers unfrozen.
Create dataloader using DatasetThyroid3StackedNew class from **mobilenet_dataset** file.
Update configtest.yaml file with lowest validation loss epoch and optimal probability prediction thresholds based on training outputs (normal, weighting true positive rate, weighting false positive rate).
Save model weights using save_networks function from **model_setup** file when in trainval true phase.

**test_cnn.py:**

Test CNN model.
Load trained CNN model using setup_model function from **model_setup** file.
Run on test data and output predictions to cnn_test_all_outs[cvphase].csv by calling analyze_test_outputs function from **analyze_model_outputs** file.

**cnn_main.py:**

Run entire data preprocessing, training and testing of CNN model and output of model predictions to cnn_test_all_outs[cvphase].csv


--------

**cnn_feature_extraction.py:**

Create function to load (from lowest validation loss epoch, saved to configtest.yaml file) and run trained CNN model (exclude final classification layer) on train, validation and test data to extract feature vectors to feed into Transformer model. 

**transformer_model.py:**

Creates the custom Transformer architecture (TransformerModel class). The Transformer architecture consists of a bi-layer Transformer-Encoder followed by a fully-connected classification layer. Each Transformer encoder layer contains 2-head encoders, comprised of self-attention and feedforward sub-layers for classification. The Transformer encoder layer input is of size (S,N,E), where S is the sequence length of the number of feature vectors per patient (36), N is batch size of 1 per mini-batch, and E is the length (256) of each feature vector.

**transformer_dataset.py:**

Create Transformer model dataset. Function load_csv_padded_transformer for loading CNN feature vectors and grouping by patient. Functions available for appending manually extracted 2D features either horizontally or vertically to CNN extracted features.
DataLoader (load_csv_padded_transformer class) calls load_csv_padded_transformer or function equivalent for adding manual features to get Transformer input vectors.

**transformer_main.py:**

Run entire CNN feature vector extraction, training and testing of Transformer model and output of model predictions to transformer_test_all_outs[cvphase].csv

**model_setup.py:**

Function setup_model for creating directories for new model and loading pretrained model weights if in test phase.
Function save_networks for saving model weights.

**analyze_model_outputs.py:**

Functions calc_test_stats and plot_test_stats.
Function analyze_test_outputs for calculating AUROC and other stats and saving model outputs to csv files.


## How to run
Edit the parser arguments in [cnn_main.py](cnn_main.py) and [transformer_main.py](transformer_main.py) with your own home directory and paths to images, labels and masks.

* Run [cnn_main.py](cnn_main.py) to train and test CNN (MobileNet-v2) model and output CNN model predictions to `cnn_test_all_outs[cvphase].csv`
```
cd $HOME/repositories/github-projects/thyroid_deep_learning/
export PYTHONPATH=$HOME/repositories/github-projects/thyroid_deep_learning/ #set PYTHONPATH environment variable
conda activate transformersVE
python cnn_main.py --project_home_dir $HOME/repositories/github-projects/thyroid_deep_learning/

```

* Run [transformer_main.py](transformer_main.py) to train and test Transformer model (on extracted CNN features) and output CNN+Transformer model predictions to `transformer_test_all_outs[cvphase].csv`

## Dependencies
### Hardware:
* [Original] GPU Tesla T4 used in this project to develop models
* [Current]
```
$ nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Fri Dec  9 19:10:10 2022
Driver Version                            : 520.61.05
CUDA Version                              : 11.8

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : NVIDIA RTX A2000 8GB Laptop GPU
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled


    FB Memory Usage
        Total                             : 8192 MiB

``` 

### Software
* [Original] (python package requirements are listed in requirements.txt):
```
OS: Debian GNU/Linux 10
CUDA Version 11.0
Pytorch 1.6.0
Python 3.8.6
albumentations
```

* [Current] machine OS:
```
$ hostnamectl
Operating System: Ubuntu 22.04.1 LTS              
          Kernel: Linux 5.15.0-56-generic
    Architecture: x86-64
```

```
$ cd $HOME/repositories/github-projects/thyroid_deep_learning/dependencies
$ conda activate transformersVE
$ python testing_versions.py 
python: 3.10.8 (main, Nov 24 2022, 14:13:03) [GCC 11.2.0]
opencv: 4.6.0
torch: 1.11.0
torch cuda_is_available: True
torch cuda version: 11.3
torch cuda.device_count  1
h5py: 3.6.0
albumentations: 1.3.0
```
See [packages versions and conda setup](dependencies/) for further details. 
