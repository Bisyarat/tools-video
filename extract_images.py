#pip install -U scikit-learn
import os
import shutil
import subprocess

datasetFolder = 'convert-video-avi' # tempat dataset di simpan
saveFolder = 'extract-images' #lokasi tempat penyimpanan pembagian dataset

for subFolder in os.listdir(datasetFolder):

    subFolderPath = os.path.join(datasetFolder,subFolder)

    for file in os.listdir(subFolderPath):

        filePath = os.path.join(subFolderPath,file)

        fileName = file.split('.')[0]
        
        SAVE_FOLDER = os.path.join(saveFolder,subFolder,fileName)
        if not os.path.exists(SAVE_FOLDER):
            os.makedirs(SAVE_FOLDER)

        VIDEO_FILE = filePath
        print(fileName)
        _FILENAME = fileName.split('_')
        FILENAME = _FILENAME[0]
        
        ffmpeg_command = f'ffmpeg -i {VIDEO_FILE} -r 30 {SAVE_FOLDER}/{FILENAME}_%03d.jpg'
        subprocess.run(ffmpeg_command, shell=True)