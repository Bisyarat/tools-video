import os

from ConvertVideo import convertVideo
from RegexSearch import regexSearch

rootFolder = '../video-bahasa-isyarat' # tempat penyimpanan video
saveFolder = 'result' #lokasi penyimpanan video
errorLogFile = 'error_file_name.txt'  #error log 


def open_dir_folder(rootFolder,saveFolder):

    for foldername , subfolder , filenames in os.walk(rootFolder):
        
        for filename in filenames: 

            locationFile = os.path.join(foldername,filename)

            folderName = regexSearch.create_folder_name(filename)
            
            if folderName is False:
                with open(errorLogFile, 'a') as errorLog:
                    errorLog.write('file {} pada folder {} tidak sesuai dengan format'.format(filename,subfolder))
                    continue #lanjutkan ke file baru jika nama file tidak sesuai
            
            folderLocation = os.path.join(saveFolder , folderName)

            checkFileExits = os.path.join(folderLocation,filename.split('.')[0] + '.mp4')

            if os.path.exists(folderLocation):
                
                if os.path.exists(checkFileExits):

                    print(checkFileExits + ' already exists')
                    continue #lanjutkan ke file baru jika nama file sudah ada
            else:
                os.makedirs(folderLocation)

            convertVideo.convert_video_using_ffmpeg(filename,locationFile,folderLocation)
            print('{} sudah berhasil di convert dan di simpan di {}'.format(filename ,folderName))

open_dir_folder(rootFolder, saveFolder)
