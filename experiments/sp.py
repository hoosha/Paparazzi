from paparazzi import Paparazzi


meshPath = '../assets/bumpyCube_normalize.obj' # normalized geometry bounded by radius 1 cube
offsetPath = '../assets/bumpyCube_normalize_offset.obj' # offset surface of the geometry 

# SLIC superpixel [Achanta et al. 2012]
compactness = 10
numSegments = 100
maxIter = 3000
imgSize = 256
windowSize = 0.3
lr = 6e-5


def filterFunc(img):
    segs = skimage.segmentation.slic(img, compactness=compactness, n_segments=numSegments)
    return skimage.color.label2rgb(segs, img, kind='avg')

p = Paparazzi(meshPath,offsetPath,imgSize=imgSize,windowSize=windowSize)

p.run(maxIter,filterFunc)