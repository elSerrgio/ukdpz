#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/python

import glob
import os
import xml.etree.ElementTree as ET
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

# for now only for single Boxes!

#pathToXml1 = ("C:/Users/go697/Documents/Augmentation/images/labelled/test1/")




def getBbsFromXml(sup):

    bbs = []

    for filename in glob.glob(sup + "*.xml"):

        tree = ET.parse(filename)
        root = tree.getroot()

        xmin = int(root[6][4][0].text)
        ymin = int(root[6][4][1].text)
        xmax = int(root[6][4][2].text)
        ymax = int(root[6][4][3].text)

        width  = int(root[4][0].text)
        height = int(root[4][1].text)
        depth  = int(root[4][2].text)

        shapeTuple = (height, width, depth)

        bbs1 = BoundingBoxesOnImage([
            BoundingBox(x1=xmin, y1=ymin, x2=xmax, y2=ymax)
        ], shape=shapeTuple)

        bbs.append(bbs1)

    return bbs

#bbs = getBbsFromXml(pathToXml1)


# In[9]:


#bbs


# In[ ]:




