import numpy as np
from scipy.cluster.vq import kmeans2
import matplotlib
matplotlib.use('Agg')
from matplotlib.image import imread
import matplotlib.pyplot as plt
import argparse
import os.path


def transform_img(img_path, k, new_img_path):
    # img read
    img = imread(img_path)
    img = img.astype('float32')
    dim1, dim2, _ = img.shape

    new_img = img.reshape((img.shape[0]*img.shape[1]), img.shape[2])

    centroid, label = kmeans2(new_img, k, minit='++')

    for i in range(new_img.shape[0]):
        new_img[i] = centroid[label[i]]

    _img = new_img.reshape(dim1, dim2, 3)
    plt.imshow(_img, interpolation='nearest')
    # plt.show()
    plt.savefig(new_img_path)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required= True)
    parser.add_argument("--k", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()
    img_path = args.input
    k = int(args.k)
    new_img_path = args.output

    # file_name = os.path.basename(img_path)
    # file_name_without_extnsion, extnsion = os.path.splitext(file_name)

    transform_img(img_path, k, new_img_path )



if __name__=="__main__":
    main()