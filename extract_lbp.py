import cv2
import numpy as np
from progress.bar import Bar
from skimage.feature import local_binary_pattern


def extractLBPFeatures(images):
    bar = Bar('[INFO] Extracting LBP features...', max=len(images), suffix='%(index)d/%(max)d  Duration:%(elapsed)ds')
    featuresList = []
    for image in images:
        if np.ndim(image) > 2:  # > 2 = colorida
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Calcular os Local Binary Patterns
        lbp = local_binary_pattern(image, P=8, R=1, method='uniform')
        hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, 10), range=(0, 10))
        featuresList.append(hist)
        bar.next()
    bar.finish()
    return np.array(featuresList, dtype=object)

