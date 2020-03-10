#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# save xml files

import glob
import os
import xml.etree.ElementTree as ET

def createXmlFiles(pathToXmlFiles, pathToPicsDir, images_aug, bbs_aug, images_names_d, numD):

    for i in range (len(images_aug)):

        filename = (pathToXmlFiles + images_names_d[i] + ".xml")
        tree = ET.parse(filename)
        root = tree.getroot()

        # bounding box position
        root[6][4][0].text = str(int(round(bbs_aug[i][0].x1)))
        root[6][4][1].text = str(int(round(bbs_aug[i][0].y1)))
        root[6][4][2].text = str(int(round(bbs_aug[i][0].x2)))
        root[6][4][3].text = str(int(round(bbs_aug[i][0].y2)))

        # shape: width, height, depth
        root[4][0].text = str(bbs_aug[i].shape[1])
        root[4][1].text = str(bbs_aug[i].shape[0])
        root[4][2].text = str(bbs_aug[i].shape[2])

        # filename and path
        root[1].text = (images_names_d[i] + "_aug" + str(i%numD+1) +".jpg")
        root[2].text = (pathToPicsDir + "augm/" + images_names_d[i] + "_aug" + str(i%numD+1) + ".jpg")

        # save
      
        if os.path.exists(pathToPicsDir + "xmlFiles/") == 0:
            os.mkdir(pathToPicsDir + "xmlFiles/")
        tree.write(pathToPicsDir + "xmlFiles/" + images_names_d[i] + "_aug" + str(i%numD+1) + ".xml")
            

