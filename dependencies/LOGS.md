

## Sun 21 Aug 20:51:11 BST 2022
* python-3.9.12 with import albumentations. Re-install from scratch VE
``` 
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py 
Traceback (most recent call last):
  File "/home/mx19/repositories/thyroid_deep_learning/dependencies/testing_versions.py", line 6, in <module>
    import albumentations
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/__init__.py", line 5, in <module>
    from .augmentations import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/augmentations/__init__.py", line 2, in <module>
    from .crops.functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/augmentations/crops/__init__.py", line 1, in <module>
    from .functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/augmentations/crops/functional.py", line 10, in <module>
    from ..geometric import functional as FGeometric
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/augmentations/geometric/__init__.py", line 1, in <module>
    from .functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/albumentations/augmentations/geometric/functional.py", line 7, in <module>
    import skimage.transform
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/skimage/transform/__init__.py", line 4, in <module>
    from .radon_transform import (radon, iradon, iradon_sart,
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/skimage/transform/radon_transform.py", line 5, in <module>
    from scipy.fft import fft, ifft, fftfreq, fftshift
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/__init__.py", line 91, in <module>
    from ._helper import next_fast_len
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_helper.py", line 3, in <module>
    from ._pocketfft import helper as _helper
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/__init__.py", line 3, in <module>
    from .basic import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/basic.py", line 6, in <module>
    from . import pypocketfft as pfft
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/torch/lib/../../../../libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-39-x86_64-linux-gnu.so)

```

* python-3.8.13 with import albumentations. Re-use the 3.9 env

``` 

$ python testing_versions.py 
Traceback (most recent call last):
  File "testing_versions.py", line 6, in <module>
    import albumentations
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/__init__.py", line 5, in <module>
    from .augmentations import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/augmentations/__init__.py", line 2, in <module>
    from .crops.functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/augmentations/crops/__init__.py", line 1, in <module>
    from .functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/augmentations/crops/functional.py", line 10, in <module>
    from ..geometric import functional as FGeometric
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/augmentations/geometric/__init__.py", line 1, in <module>
    from .functional import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/albumentations/augmentations/geometric/functional.py", line 7, in <module>
    import skimage.transform
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/__init__.py", line 4, in <module>
    from .radon_transform import (radon, iradon, iradon_sart,
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/radon_transform.py", line 5, in <module>
    from scipy.fft import fft, ifft, fftfreq, fftshift
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/__init__.py", line 91, in <module>
    from ._helper import next_fast_len
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_helper.py", line 3, in <module>
    from ._pocketfft import helper as _helper
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/__init__.py", line 3, in <module>
    from .basic import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/basic.py", line 6, in <module>
    from . import pypocketfft as pfft
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/torch/lib/../../../../libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-38-x86_64-linux-gnu.so)

```

SOLUTION_TRY00: https://github.com/lhelontra/tensorflow-on-arm/issues/13 
SOLUTION_TRY01: https://askubuntu.com/questions/1418016/glibcxx-3-4-30-not-found-in-conda-environment
``` 
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/torch/lib/../../../../libstdc++.so.6
``` 
SOLUTION_TRY02: https://stackoverflow.com/questions/73008614/scikit-image-glibcxx-importerror-is-the-problem-with-skimage-anaconda-or-ubun
SOLUTION_TYR03:https://github.com/BVLC/caffe/issues/4953
``` 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mx19/anaconda3/envs/transformersVE/lib/
```

TODO: remove and install VE with python 3.9



## Sun 21 Aug 08:31:15 BST 2022
* python-3.10
``` 
$ python testing_versions.py 
Traceback (most recent call last):
  File "/home/mx19/repositories/thyroid_deep_learning/dependencies/testing_versions.py", line 7, in <module>
    import h5py
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.10/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.10/site-packages/h5py/version.py", line 15, in <module>
    from . import h5 as _h5
  File "h5py/h5.pyx", line 1, in init h5py.h5
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.10/site-packages/h5py/defs.cpython-310-x86_64-linux-gnu.so: undefined symbol: H5Pget_fapl_direct
```

SOLUTION_TRY00: https://github.com/h5py/h5py/issues/2037