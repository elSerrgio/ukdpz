#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python
# Bilder duplizieren. Muster: pic1,pic2,pic3,pic_last, pic1,pic2,pic3,pic_last, pic1,....

# Duplicates every picture in a list multiple times 
def duplicatePics(images, numOfDuplicates): 
    images_dupl = []
    for n in range(numOfDuplicates):
        for i in range(len(images)):
            images_dupl.append(images[i])
    return images_dupl

