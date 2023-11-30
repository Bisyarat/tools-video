#pip install -U scikit-learn
import os
import shutil
from sklearn.model_selection import train_test_split

datasetFolder = 'dataset' # tempat dataset di simpan
saveFolder = 'splitDataset' #lokasi tempat penyimpanan pembagian dataset


sizeTestFolder = 0.2 #20%
sizeDevFolder = 0.1 #10%
#size TrainFolder menjadi 100% - (20 - 10)%

def move_file(files, sourcePath, toFolder):

    if not os.path.exists(toFolder):
        os.makedirs(toFolder)

    for file in files:
        sourceFilePath = os.path.join(sourcePath,file)
        toFolderPath = os.path.join(toFolder,file)

        shutil.copy(sourceFilePath,toFolderPath)


for subFolder in os.listdir(datasetFolder):

    train_path = os.path.join(saveFolder, 'train', subFolder)
    test_path  = os.path.join(saveFolder, 'test', subFolder)
    dev_path   = os.path.join(saveFolder, 'dev', subFolder)

    subFolderPath = os.path.join(datasetFolder,subFolder)

    for folder in os.listdir(subFolderPath):

        folderPath = os.path.join(subFolderPath,folder)

        trainDataFiles, testDataFiles = train_test_split(os.listdir(folderPath), test_size=sizeTestFolder)
        testDataFiles , devDataFiles  = train_test_split(testDataFiles, test_size=sizeDevFolder)

        move_file(trainDataFiles, folderPath, train_path)
        move_file(testDataFiles, folderPath, test_path)
        move_file(devDataFiles, folderPath, dev_path)

