## Thyroid Ultrasound Cine-clip Dataset
> We collected data from 167 patients with biopsy-confirmed thyroid nodules (n=192) at the Stanford University Medical Center. 
The dataset consists of ultrasound cine-clip images, radiologist-annotated segmentations, patient demographics, lesion size and location, TI-RADS descriptors, and histopathological diagnoses."  
* dataset.hdf5 (36.42 GB) 
* metadata.csv(9.03 KB)
* SITE: https://stanfordaimi.azurewebsites.net/datasets/a72f2b02-7b53-4c5d-963c-d7253220bfd5 

To download create an account in the StanfordAIMI [site](https://aimiorg.b2clogin.com/aimiorg.onmicrosoft.com/b2c_1_signin_signup/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=e1963fdc-4746-4bc1-bc80-84dcc31df4d2&redirect_uri=https%3A%2F%2Fstanfordaimi.azurewebsites.net%2F&state=eyJpZCI6IjY2NWYxYmVjLTljMDItNGEzMS1hMzAzLWYwNzE5OTU2MGUwMiIsInRzIjoxNjYxMDU5Mzg5LCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=0b220da4-dab0-479f-8feb-1be6c5e1bf9c&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.2&client-request-id=56bf75bf-9908-4b58-9e18-2ba8fce13fc4&response_mode=fragment)

## Notebooks to check data
``` 
cd $HOME/repositories/github-projects/thyroid_deep_learning/data
export PYTHONPATH=$HOME/repositories/github-projects/thyroid_deep_learning/ #set PYTHONPATH environment variable
conda activate transformersVE
jupyter notebook --no-browser
```

## Datafiles tree
```
$ tree -s
.
├── [36418794716]  dataset.hdf5
├── [       9030]  metadata.csv
└── [        432]  README.md

0 directories, 3 files
```

## hdf5 files
Extract hdf5 files from `dataset.hdf5`:
* "--imgpath", type=str, default="/path/to/imgs.hdf5"
* "--maskpath", type=str, default="/path/to/masks.hdf5",
* "--labelpath", type=str, default="/path/to/labels.csv"
```
@mobilenet_dataset.py:
L40:    colnames = ['Labels for each frame', 'Annot_IDs', 'size_A', 'size_B', 'size_C', 'location_r_l_', 'study_dttm', 'age', 'sex', 'final_diagnoses', 'ePAD ID', 'foldNum']
L41:    label_data = pd.read_csv(labelpath, names=colnames)
```

## errors
When copying dataset.hdf5 to other drive, I get:
```
Error splicing file: File too large
```
POTENTIAL_SOLUTION: https://askubuntu.com/questions/348888/how-do-i-solve-error-splicing-files 

## License
[Stanford University Dataset Research Use Agreement](LICENSE)
