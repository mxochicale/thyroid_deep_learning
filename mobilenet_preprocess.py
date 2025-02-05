import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#crop around bounding box of mask
#https://www.kaggle.com/whizzkid/crop-images-using-bounding-box
def crop_bounding_box(img, mask):
    """Crop bounding box 5 pixels around nodule mask.
    Used by transform_and_crop functions.
    Return cropped image."""
    info = np.iinfo(mask.dtype)

    ret,thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    #cnt = contours[0]

    #find coordinates to crop around mask
    (y, x) = np.where(thresh == 255)
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))

    out = img[topy-5:bottomy+5, topx-5:bottomx+5] #5 pixel border
    return out

#adjacent/equal spaced (just crop)
def transform_and_crop_new(imgs, masks):
    """Crop images and resize them to 224x224.
    Return list of all cropped and resized images."""

    all_imgs_cropped=[]
    #cropping approach by mask (crop before resizing):
    #trying cropping as cv image
    for im in range(len(imgs)):
        cv_im = imgs[im]
        mask = masks[im]
        cropped_im = crop_bounding_box(cv_im, mask) #needs 3 channels

        #downsize images with PIL
        cropped_im = np.asarray(cropped_im)
        new_im = Image.fromarray(cropped_im) #convert to PIL format Image
        new_im = new_im.resize((224, 224)) #resize with PIL

        all_imgs_cropped.append(np.array(new_im))

    print("all images array shape after cropping/resizing:", np.shape(all_imgs_cropped))
    return all_imgs_cropped



#needed for singleframe (largest), can use for all frame types
def transform_and_crop_largest(imgs, masks, pats):
    """
    Crop images and resize them to 224x224.
    Create list with a 1 at the frame index of the largest sized nodule in each patient.
    Return list of all cropped and resized images, and the list of the largest patient indices.
    """
    all_imgs_cropped=[]
    newpats = []
    biggestinpat = np.zeros((len(imgs)))
    firstinpat = False
    patmaxarea = 0
    patmaxareaind = 0

    # pats.pop(0) #take out title row

    #cropping approach by mask (crop before resizing):
    for im in range(len(imgs)):
        #print(im)
        if(pats[im] not in newpats):
            newpats.append(pats[im])
            firstinpat = True
            if(len(newpats) > 1):
                biggestinpat[patmaxareaind] = 1
                #print("last patient", pats[im-1], "(check)", pats[patmaxareaind], "max area", patmaxarea, "at ind", patmaxareaind)

            patmaxarea = 0
            patmaxareaind = 0
        else:
            firstinpat = False

        cv_im = imgs[im]
        mask = masks[im]
        cropped_im = crop_bounding_box(cv_im, mask) #needs 3 channels

        #downsize images with PIL
        cropped_im = np.asarray(cropped_im)
        new_im = Image.fromarray(cropped_im) #convert to PIL format Image

        #lesion area
        w, h = new_im.size
        if(w*h >= patmaxarea): #if largest, update patientmaxarea variables
            patmaxareaind = im
            patmaxarea = w*h
            #print("in patient", pats[im], "biggest area so far", patmaxarea,"index", im)

        new_im = new_im.resize((224, 224)) #resize with PIL

        if(im == 0):
            print("after resize")
            imgplot = plt.imshow(new_im)
            plt.show() #show cropped and resized image

        if(im%2000 == 0):
            print(f' image_index: {im}')
            #imgplot = plt.imshow(new_im)
            #plt.show() #show cropped and resized image

        all_imgs_cropped.append(np.array(new_im))

    #do last patient
    biggestinpat[patmaxareaind] = 1
    print(len(newpats), "total pats:", newpats)

    print("all images array shape after cropping/resizing:", np.shape(all_imgs_cropped))
    return all_imgs_cropped, biggestinpat