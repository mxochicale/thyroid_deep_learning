
# Mon 12 Sep 15:44:25 BST 2022

* Create env with default dependencies:
```
Pytorch 1.6.0
Python 3.8.6
```

* ERRORS:
```

(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py
Traceback (most recent call last):
  File "testing_versions.py", line 6, in <module>
    import h5py
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/version.py", line 15, in <module>
    from . import h5 as _h5
  File "h5py/h5.pyx", line 1, in init h5py.h5
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/defs.cpython-38-x86_64-linux-gnu.so: undefined symbol: H5Pget_fapl_direct
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py
Traceback (most recent call last):
  File "testing_versions.py", line 7, in <module>
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
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/__init__.py", line 5, in <module>
    from .radon_transform import (radon, iradon, iradon_sart,
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/radon_transform.py", line 5, in <module>
    from ._warps import warp
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/_warps.py", line 7, in <module>
    from ..measure import block_reduce
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/measure/__init__.py", line 8, in <module>
    from ._polygon import approximate_polygon, subdivide_polygon
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/measure/_polygon.py", line 2, in <module>
    from scipy import signal
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/__init__.py", line 309, in <module>
    from . import _sigtools, windows
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/windows/__init__.py", line 41, in <module>
    from ._windows import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/windows/_windows.py", line 7, in <module>
    from scipy import linalg, special, fft as sp_fft
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/__init__.py", line 91, in <module>
    from ._helper import next_fast_len
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_helper.py", line 3, in <module>
    from ._pocketfft import helper as _helper
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/__init__.py", line 3, in <module>
    from .basic import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/basic.py", line 6, in <module>
    from . import pypocketfft as pfft
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/torch/lib/../../../../libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-38-x86_64-linux-gnu.so)
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py
python: 3.8.13 (default, Mar 28 2022, 11:38:47) 
[GCC 7.5.0]
opencv: 4.6.0
torch: 1.6.0
cuda_is_available: False
cuda version: None
cuda.device_count  0
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ 


```

* conda list -n transformersVE 

```

h5py                      3.7.0           nompi_py38h8afedcf_100    conda-forge
harfbuzz                  2.8.1                h83ec7ef_0    conda-forge
hdf5                      1.12.1               h70be1eb_2  

jupyter                   1.0.0            py38h06a4308_8  

libgcc                    7.2.0                h69d50b8_2  

python                    3.8.13               h12debd9_0  

pytorch                   1.6.0               py3.8_cpu_0  [cpuonly]  pytorch

numpy                     1.23.1           py38h6c91a56_0  
numpy-base                1.23.1           py38ha15fc14_0  
opencv                    4.5.3            py38h578d9bd_3    conda-forge
opencv-python             4.6.0.66                 pypi_0    pypi

```

* TOTRY
```
install deftaul version for 
1. python, pytorch and albumentations 
2. install h5py
test?
```

# Sun 11 Sep 12:33:26 BST 2022
TRY:`   - h5py=2.* #=3.* # current version 3.6.0`
https://github.com/albumentations-team/autoalbument/issues/14

```  

  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/basic.py", line 6, in <module>
    from . import pypocketfft as pfft
ImportError: /home/mx19/anaconda3/envs/transformersVE/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-39-x86_64-linux-gnu.so)


```


## Sun 11 Sep 11:50:09 BST 2022

* error `../lib/libstdc++.so.6: version`
```
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python
Python 3.9.12 (main, Jun  1 2022, 11:38:51) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import albumentations
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
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
ImportError: /home/mx19/anaconda3/envs/transformersVE/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found 
(required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-39-x86_64-linux-gnu.so)
>>> 
```

* TRYING: https://askubuntu.com/questions/1418016/glibcxx-3-4-30-not-found-in-conda-environment
``` 

#DONT WORK
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/torch/lib/libstdc++.so.6

#DONTWORK
mkdir -p /home/mx19/anaconda3/envs/transformersVE/bin/sth/lib/
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6  /home/mx19/anaconda3/envs/transformersVE/bin/sth/lib/libstdc++.so.6
``` 

* TRYING: https://github.com/BVLC/caffe/issues/4953
``` 
#DONTWORK
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6  /home/mx19/anaconda3/envs/transformersVE/lib/libstdc++.so.6
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mx19/anaconda3/envs/transformersVE/lib/

#DONT WORK
* `conda install libgcc` using VE 
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6  /home/mx19/anaconda3/envs/transformersVE/lib/libstdc++.so.6
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/mx19/anaconda3/envs/transformersVE/lib/


    from . import pypocketfft as pfft
ImportError: /home/mx19/anaconda3/envs/transformersVE/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found 
(required by /home/mx19/anaconda3/envs/transformersVE/lib/python3.9/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-39-x86_64-linux-gnu.so)
  
```


## Sat 27 Aug 23:43:31 BST 2022
* creating  transformersVE from scract with   - python=3.9
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

* commenting albumentations
```
#import albumentations
#print(f'albumentations: {albumentations.__version__}')
```

```
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ vim testing_versions.py 
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py 
python: 3.9.12 (main, Jun  1 2022, 11:38:51) 
[GCC 7.5.0]
opencv: 4.6.0
torch: 1.12.1
h5py: 3.7.0
cuda_is_available: True
cuda version: 11.3
cuda.device_count  1
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ 

```


## Sat 27 Aug 16:31:30 BST 2022
* creating  transformersVE from scratch with   - python=3.8

```

(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py
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
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/__init__.py", line 5, in <module>
    from .radon_transform import (radon, iradon, iradon_sart,
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/radon_transform.py", line 5, in <module>
    from ._warps import warp
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/transform/_warps.py", line 7, in <module>
    from ..measure import block_reduce
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/measure/__init__.py", line 8, in <module>
    from ._polygon import approximate_polygon, subdivide_polygon
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/skimage/measure/_polygon.py", line 2, in <module>
    from scipy import signal
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/__init__.py", line 309, in <module>
    from . import _sigtools, windows
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/windows/__init__.py", line 41, in <module>
    from ._windows import *
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/scipy/signal/windows/_windows.py", line 7, in <module>
    from scipy import linalg, special, fft as sp_fft
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

without albumentations

```
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ python testing_versions.py
Traceback (most recent call last):
  File "testing_versions.py", line 7, in <module>
    import h5py
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/version.py", line 15, in <module>
    from . import h5 as _h5
  File "h5py/h5.pyx", line 1, in init h5py.h5
ImportError: /home/mx19/anaconda3/envs/transformersVE/lib/python3.8/site-packages/h5py/defs.cpython-38-x86_64-linux-gnu.so: undefined symbol: H5Pget_fapl_direct
(transformersVE) mx19@sie133-lap:~/repositories/thyroid_deep_learning/dependencies$ 
```

Let's go back to python 3.9


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
