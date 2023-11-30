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

    for filename in files:
        sourceFilePath = os.path.join(sourcePath,filename)
        toFolderPath = os.path.join(toFolder,filename)

        shutil.copy(sourceFilePath,toFolderPath)


for subFolder in os.listdir(datasetFolder):

    train_path = os.path.join(saveFolder, 'train', subFolder)
    test_path  = os.path.join(saveFolder, 'test', subFolder)
    dev_path   = os.path.join(saveFolder, 'dev', subFolder)

    subFolderPath = os.path.join(datasetFolder,subFolder)

    for folder in os.listdir(subFolderPath):

        folderPath = os.path.join(subFolderPath,folder)

        trainDataFile, testDataFile = train_test_split(os.listdir(folderPath), test_size=sizeTestFolder)
        testDataFile , devDataFile  = train_test_split(testDataFile, test_size=sizeDevFolder)

        move_file(trainDataFile, folderPath, train_path)
        move_file(testDataFile, folderPath, test_path)
        move_file(devDataFile, folderPath, dev_path)

