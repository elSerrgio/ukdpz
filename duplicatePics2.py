#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python
# Bilder duplizieren. Muster: pic1, pic1, pic1,..., pic2, pic2,pic2...,...

# Duplicates every picture in a list multiple times 
def duplicatePics2(images, numOfDuplicates): 
    images_dupl = []
    for n in range(len(images)):
        for i in range(numOfDuplicates):
            images_dupl.append(images[n])
    return images_dupl

