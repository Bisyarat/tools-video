import os   
# import imageio_ffmpeg as ffmpeg
import moviepy.editor as moviepy

folder = 'vid-bahasa-isyarat' #ganti sesuai dengan nama tempat folder
saveFolder = 'result' #ganti sesuai dengan nama tempat penyimpanan folder

def convert_mov_to_mp4(input_folder,saveFolder):
    # Membaca isi folder input
    for folder in os.listdir(input_folder): 
        
        folderFile = os.path.join(input_folder , folder)
        nameFolder = folder
        
        for filename in os.listdir(folderFile):
            
            if filename.endswith(".MOV"):
                
                input_path = os.path.join(folderFile, filename)
                output_filename = os.path.splitext(filename)[0] + ".mp4"
                toFolder = os.path.join(saveFolder, nameFolder)              
        
                #jika folder belum ada,maka akan dibuat terlebih dahulu
                if not os.path.exists(toFolder):
                    os.makedirs(toFolder)

                #menyimpan hasil folder ke output_path
                output_path = os.path.join(toFolder, output_filename)

                clip = moviepy.VideoFileClip(input_path)
                clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
                
        print('Completed convert file')

# Ganti 'input_folder' dengan nama folder yang berisi file-file video
# Ganti 'saveFolder' dengan nama folder tempat Anda ingin menyimpan file hasil konversi
convert_mov_to_mp4(folder,saveFolder)
