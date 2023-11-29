import os   
import moviepy.editor as moviepy
import subprocess

class convertVideo:
    
    def convert_video_to_mp4(filename,videoFile, saveFolder):
        
        # sizeFile = os.path.getsize(videoFile) / (1024 * 1024)
        
        output_filename = filename.split('.')[0] + ".mp4"
        output_path = os.path.join(saveFolder, output_filename)
        
        converter = moviepy.VideoFileClip(videoFile)
        converter = converter.set_audio(None)
        
        converter.write_videofile(output_path ,  codec='libx264', audio_codec='aac',bitrate='1000k')              
    
    def convert_video_using_ffmpeg(filename,videoFile, saveFolder):

        bitrate = '1000k'
        output_filename = filename.split('.')[0] + ".mp4"
        output = os.path.join(saveFolder, output_filename)
        
        #convert file to mp4 and remove audio
        ffmpeg_command = f'ffmpeg -i {videoFile} -b:v "{bitrate}" -c:a copy -an {output}'
        subprocess.run(ffmpeg_command, shell=True)

