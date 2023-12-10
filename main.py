import os
import time

import numpy as np
from progress.bar import Bar
from sklearn import preprocessing

from extract_hu import extractHuMomentsFeatures
from extract_lbp import extractLBPFeatures
from grayHistogram_FeatureExtraction import encodeLabels, getData, saveData


def main():
    mainStartTime = time.time()
    trainImagePath = './images_split/train/'
    testImagePath = './images_split/test/'
    trainFeaturePath = './features_labels/train/'
    testFeaturePath = './features_labels/test/'
    
    print(f'[INFO] ========= TRAINING IMAGES ========= ')
    trainImages, trainLabels = getData(trainImagePath)
    trainEncodedLabels, encoderClasses = encodeLabels(trainLabels)
    
    # Escolha o método de extração de características desejado ('hu_moments' ou 'lbp')
    trainFeatures = extractHuMomentsFeatures(trainImages)
    # ou
    #trainFeatures = extractLBPFeatures(trainImages)

    # Salvar dados diretamente após a extração

    saveData(trainFeaturePath, trainEncodedLabels, trainFeatures, encoderClasses)
    
    print(f'[INFO] =========== TEST IMAGES =========== ')
    testImages, testLabels = getData(testImagePath)
    testEncodedLabels, encoderClasses = encodeLabels(testLabels)
    
    # Escolha o método de extração de características desejado ('hu_moments' ou 'lbp')
    testFeatures = extractHuMomentsFeatures(testImages)
    # ou
    #testFeatures = extractLBPFeatures(testImages)

    saveData(testFeaturePath, testEncodedLabels, testFeatures, encoderClasses)
    
    elapsedTime = round(time.time() - mainStartTime, 2)
    print(f'[INFO] Code execution time: {elapsedTime}s')


if __name__ == "__main__":
    main()
