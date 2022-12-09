# conda activate transformersVE
# python testing_versions.py
import sys
import cv2
import torch 
import h5py
import albumentations

print(f'python: {sys.version}')
print(f'opencv: {cv2.__version__}')
print(f'torch: {torch.__version__}')
print(f'torch cuda_is_available: {torch.cuda.is_available()}')
print(f'torch cuda version: {torch.version.cuda}')
print(f'torch cuda.device_count  {torch.cuda.device_count()}')
print(f'h5py: {h5py.__version__}')
print(f'albumentations: {albumentations.__version__}')