import os   
import moviepy.editor as moviepy

class convertVideo:
    
    def convert_video_to_mp4(filename,videoFile, saveFolder):
        output_filename = filename + ".mp4"
        output_path = os.path.join(saveFolder, output_filename)
        # print(output_filename)
        # print(output_path)
        # converter = moviepy.VideoFileClip(videoFile)
        # converter.write_videofile(output_path ,  codec='libx264', audio_codec='aac')              