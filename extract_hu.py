import cv2
import numpy as np
from progress.bar import Bar

def extractHuMomentsFeatures(images):
    bar = Bar('[INFO] Extracting Hu Moments features...', max=len(images), suffix='%(index)d/%(max)d  Duration:%(elapsed)ds')
    featuresList = []
    for image in images:
        if np.ndim(image) > 2:  # > 2 = colorida
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Calcular os momentos de Hu
        moments = cv2.HuMoments(cv2.moments(image)).flatten()
        featuresList.append(moments)
        bar.next()
    bar.finish()
    return np.array(featuresList, dtype=object)