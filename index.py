import os
import shutil
from ConvertVideo import convertVideo
from RegexSearch import regexSearch

rootFolder = '../video-bahasa-isyarat' # tempat penyimpanan video
saveFolder = 'result' #lokasi penyimpanan video

def open_dir_folder(rootFolder,saveFolder):
    
    for foldername , subfolder , filenames in os.walk(rootFolder):
        
        for filename in filenames: 
            
            locationFile = os.path.join(foldername,filename)
            
            folderName = regexSearch.create_folder_name(filename)
            folderLocation = os.path.join(saveFolder , folderName)
            
            checkFileExits = os.path.join(folderLocation,filename.split('.')[0] + '.mp4')
            
            if os.path.exists(checkFileExits):
                print( checkFileExits + ' already exists')
                
                continue
            
            else:  
                
                os.makedirs(folderLocation)
                
                if not filename.endswith('.mp4') and not filename.endswith('.MP4'):
                    print('file' + filename + ' not mp4, converting file to mp4....')
                    convertVideo.convert_video_to_mp4(filename,locationFile,folderLocation)
                
                else:
                    print('doing duplicate file ' + filename + ' to folder result....')
                    shutil.copy(locationFile, os.path.join(folderLocation, os.path.basename(filename)))

open_dir_folder(rootFolder, saveFolder)
