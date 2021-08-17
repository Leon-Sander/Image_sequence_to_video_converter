import cv2
import numpy as np
import glob

class converter:

    def __init__(self):
        pass

    def convert(self, imgs_path, fps ,img_format = "jpg", output_format = "avi", output_name = "converted_video", output_dir = 'output/'):
        img_array, size = self.__load_imgs__(imgs_path, img_format)
        out = cv2.VideoWriter(output_dir + output_name + '.' + output_format, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        print("Saved " + output_name + '.' + output_format + ' to output directory.')
    

    def __load_imgs__(self,imgs_path, img_format):
        if imgs_path[-1] != '/':
            imgs_path = imgs_path + '/'
        
        filenames = glob.glob(imgs_path + '*.' + img_format)
        filenames.sort()
        size = self.__get_size__(filenames[0])

        img_array = []
        for filename in filenames:
            img = cv2.imread(filename)
            img_array.append(img)

        return img_array , size


    def __get_size__(self, img_path):
        img = cv2.imread(img_path)
        height, width, layers = img.shape
        size = (width,height)

        return size
