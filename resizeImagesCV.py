{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    " \n",
    "img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)\n",
    " \n",
    "print('Original Dimensions : ',img.shape)\n",
    " \n",
    "scale_percent = 60 # percent of original size\n",
    "width = int(img.shape[1] * scale_percent / 100)\n",
    "height = int(img.shape[0] * scale_percent / 100)\n",
    "dim = (width, height)\n",
    "# resize image\n",
    "resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)\n",
    " \n",
    "print('Resized Dimensions : ',resized.shape)\n",
    " \n",
    "cv2.imshow(\"Resized image\", resized)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}