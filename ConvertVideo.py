import os   
import moviepy.editor as moviepy
import subprocess

class convertVideo:
    
    def convert_video_to_mp4(filename,videoFile, saveFolder):
    
        output_filename = filename.split('.')[0] + ".mp4"
        output_path = os.path.join(saveFolder, output_filename)
        
        converter = moviepy.VideoFileClip(videoFile)
        converter = converter.set_audio(None)
        
        converter.write_videofile(output_path ,  codec='libx264', audio_codec='aac',bitrate='1000k')              
    
    def convert_video_using_ffmpeg(filename,videoFile, saveFolder):

        BITRATE = '3000k'
        _FILENAME = filename.split('.')[0]
        
        OUTPUT_FILENAME = _FILENAME.lower() + '.avi'

        OUTPUT = os.path.join(saveFolder, OUTPUT_FILENAME)
        
        if os.path.exists(OUTPUT):
            return

        #convert file to mp4 and remove audio
        ffmpeg_command = f'ffmpeg -i {videoFile} -c:v libx264 -b:v "{BITRATE}" -c:a copy -an {OUTPUT}'
        subprocess.run(ffmpeg_command, shell=True)

