import os

from ConvertVideo import convertVideo
from RegexSearch import regexSearch

rootFolder = 'video' # tempat penyimpanan video
saveFolder = 'convert-video-avi' #lokasi penyimpanan video
errorLogFile = 'error_file_name.txt'  #error log 


def open_dir_folder(rootFolder,saveFolder):
    
    for subFolder in os.listdir(rootFolder):

        FOLDER_PATH = os.path.join(rootFolder,subFolder)
        for folder in os.listdir(FOLDER_PATH):

            if folder != 'checked' and folder != 'Checked':
                continue

            CHECKED_FOLDER = os.path.join(FOLDER_PATH, folder)

            for categoryFolder in os.listdir(CHECKED_FOLDER):

                CATEGORY_FOLDER  = os.path.join(CHECKED_FOLDER, categoryFolder)

                for filename in os.listdir(CATEGORY_FOLDER):

                    folderName = (regexSearch.create_folder_name(filename)).lower()
                    folderLocation = os.path.join(CATEGORY_FOLDER,filename)
                    print(folderLocation)
                    if folderName is False:
                        with open(errorLogFile, 'a') as errorLog:
                            errorLog.write('file {} pada folder {} tidak sesuai dengan format\n'.format(filename,CATEGORY_FOLDER))
                            continue #lanjutkan ke file baru jika nama file tidak sesuai

                    SAVE_LOCATION = os.path.join(saveFolder , folderName)

                    if not os.path.exists(SAVE_LOCATION):
                        os.makedirs(SAVE_LOCATION)

                    convertVideo.convert_video_using_ffmpeg(filename,folderLocation,SAVE_LOCATION)
                    print('{} sudah berhasil di convert dan di simpan di {}'.format(filename ,SAVE_LOCATION))


open_dir_folder(rootFolder, saveFolder)
