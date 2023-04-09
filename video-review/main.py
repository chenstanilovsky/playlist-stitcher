import configparser, os, shutil
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize


# Opens video, waits for it to finish, then closes after some delay
def play_video(video_file, delay):
    clip = VideoFileClip(video_file)
    clip = resize(clip, 0.5)
    clip.preview()
    clip.close()


if __name__ == "__main__":
    # Read from config file
    config = configparser.ConfigParser()
    config.read("config.ini")
    video_dir = config["DEFAULT"]["video_dir"]

    # Create approved and disapproved directories if they don't exist
    if not os.path.exists(video_dir + "/approved"):
        os.makedirs(video_dir + "/approved")
    if not os.path.exists(video_dir + "/disapproved"):
        os.makedirs(video_dir + "/disapproved")

    # Get list of .mp4 files in video directory
    video_files = []
    for file in os.listdir(video_dir):
        if file.endswith(".mp4"):
            video_files.append(file)

    # Sort video files alphabetically
    video_files.sort()

    # Loop through each video file
    for video_file in video_files:
        print("Playing:", video_file)
        play_video(video_dir + "/" + video_file, 2)
        user_approval = input("Do you approve this video? (y/n) ")

        # Move file to appropriate directory based on approval status
        if user_approval.lower() == "y":
            shutil.move(
                video_dir + "/" + video_file, video_dir + "/approved/" + video_file
            )
            print(video_file, "has been moved to the approved folder.")
        else:
            shutil.move(
                video_dir + "/" + video_file, video_dir + "/disapproved/" + video_file
            )
            print(video_file, "has been moved to the disapproved folder.")
