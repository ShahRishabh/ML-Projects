#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import math


# In[ ]:


num_pixels = 4096 # 64x64 pixels
num_images = 10 # number of images for each person
num_subjects = 15 # number of people


# In[ ]:


DATADIR = "E:/Studies/CH5019/Project/Term project 2020/Term project 2020/Dataset_Question1" # directory path


# In[ ]:


# Initializations
data = np.zeros(shape=(num_subjects,num_pixels,num_images), dtype='int') # data matrix that will store the images
data_shifted = np.zeros(shape=(num_subjects,num_pixels,num_images)) # mean shifted data matrix
data_rep = np.zeros(shape=(num_pixels,num_subjects)) # representative image data matrix


# In[ ]:


# Converting images into data matrix
for i in range(num_subjects):
    for j in range(num_images):
        a = str(i+1)
        b = str(j+1)
        path = DATADIR + '/' + a + '/' + b + '.pgm'
        img = plt.imread(path)
        data[i, :, j] = np.matrix.flatten(img, 'F') # converting to column vector
    data_shifted[i,:,:] = data[i,:,:] - np.mean(data[i,:,:],0) # mean shifting
    u, s_, v = la.svd(data_shifted[i,:,:]) # applying svd
    s = la.diagsvd(s_,*data_shifted[i,:,:].shape)
    temp = u[:,0].reshape(num_pixels,1)@s[0,:].reshape(1,num_images)@v[:,0].reshape(num_images,1) # compressing images
    data_rep[:,i] = temp.reshape(num_pixels)


# In[ ]:


# Percentage Variance retained
var_ret = (s_[0] ** 2) / (sum(np.square(s_))) * 100
print('Percentage variance retained is %2.2f %%' %(var_ret))


# In[ ]:


# Determining number of correctly indentified images
correct = 0
print("These images do not match (sub, image):")
for i in range(num_subjects):
    for j in range(num_images):
        error = math.inf
        ind = -1
        for k in range(num_subjects):
            l2_norm = la.norm(data_shifted[i,:,j] - data_rep[:,k]) # calculating norm
            if l2_norm < error:
                error = l2_norm
                index = k
        if index == i:
            correct += 1
        else:
            print(i+1, ',', j+1)
print("\nNumber of images correctly identified:", correct)

# Accuracy
accuracy = correct / 150 * 100
print('\nThe accuracy obtained is %2.2f %%' %(accuracy))


# In[ ]:


# Printing representative images
for i in range(num_subjects):
    img = data_rep[:,i] + np.mean(data[i,:,:])
    img = img.reshape((64,64)).T
    a = str(i+1)
    name = a + '.png'
    plt.figure()
#     plt.imsave(name, img, cmap='gray')
    plt.imshow(img, cmap='gray')

