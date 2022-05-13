from moviepy.editor import *
import os

source_directory = 'source'
result_directory = 'result'
split = 5
i = 0

if(os.path.exists(source_directory) and os.path.exists(result_directory)):
    for filename in os.listdir(source_directory):
        f = os.path.join(source_directory, filename)

        if(os.path.isfile(f)):
            video = VideoFileClip(f).subclip(split)
            video.write_videofile(result_directory + "/result" + str(i) + ".mp4", fps = 25)
            i = i + 1
else:
    print('Missing: ' + source_directory + ' || ' + result_directory)