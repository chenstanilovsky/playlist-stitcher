import os, time
import subprocess
import configparser
import shutil
from moviepy.editor import VideoFileClip 
from moviepy.video.fx.all import resize
# Opens video, waits for it to finish, then closes after some delay
def play_video(video_file, delay):
    clip = VideoFileClip(video_file)
    clip = resize(clip, 0.5)
    clip.preview()
    clip.close()
    # Open the video file
    # cap = cv2.VideoCapture(video_file)

    # # Check if the video file was opened successfully
    # if not cap.isOpened():
    #     print("Error opening video file")

    # # Loop through the frames of the video
    # while cap.isOpened():
    #     # Read a frame from the video
    #     ret, frame = cap.read()

    #     # If the frame was read successfully, display it
    #     if ret:
    #         cv2.imshow('Frame', frame)

    #         # Check if the 'q' key was pressed to exit
    #         if cv2.waitKey(25) & 0xFF == ord('q'):
    #             break

    #     # If we have reached the end of the video, exit the loop
    #     else:
    #         break

    # # Release the video capture object and close all windows
    # cap.release()
    # cv2.destroyAllWindows()
    # subprocess.call(['osascript', '-e', 'tell application "QuickTime Player"', '-e', 'activate', '-e', 'open "' + video_file + '"', '-e', 'play document 1', '-e', 'repeat until (current time of document 1 = duration of document 1)', '-e', 'end repeat', '-e', 'delay ' + str(delay), '-e', 'close document 1', '-e', 'end tell'])

# Read from config file
config = configparser.ConfigParser()
config.read('config.ini')
video_dir = config['DEFAULT']['video_dir']

# Create approved and disapproved directories if they don't exist
if not os.path.exists(video_dir + '/approved'):
    os.makedirs(video_dir + '/approved')
if not os.path.exists(video_dir + '/disapproved'):
    os.makedirs(video_dir + '/disapproved')

# Get list of .mp4 files in video directory
video_files = []
for file in os.listdir(video_dir):
    if file.endswith('.mp4'):
        video_files.append(file)

# Sort video files alphabetically
video_files.sort()

# Loop through each video file
for video_file in video_files:
    print('Playing:', video_file)
    play_video(video_dir + '/' + video_file, 2)
    user_approval = input('Do you approve this video? (y/n) ')

    # Move file to appropriate directory based on approval status
    if user_approval.lower() == 'y':
        shutil.move(video_dir + '/' + video_file, video_dir + '/approved/' + video_file)
        print(video_file, 'has been moved to the approved folder.')
    else:
        shutil.move(video_dir + '/' + video_file, video_dir + '/disapproved/' + video_file)
        print(video_file, 'has been moved to the disapproved folder.')