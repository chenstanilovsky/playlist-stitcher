import os, shutil
import multiprocessing as mp
from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips


def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()
    return video.default_filename

def stitch_clips(video_files, playlist_title):
    video_clips = []
    for video_file in video_files:
        clip = VideoFileClip(video_file)
        video_clips.append(clip)

    final_clip = concatenate_videoclips(video_clips, method="compose")
    final_clip.write_videofile(f'{playlist_title}.mp4', fps=25)
    final_clip.close()

    results_path = os.path.realpath(__file__).split('main.py')[0] + "results/"
    shutil.move(os.getcwd() + f'/{playlist_title}.mp4', results_path)




if __name__ == '__main__':
    playlist_url = input("Enter the playlist URL: ")
    playlist = Playlist(playlist_url)
    pool = mp.Pool(processes=10)  # Set the number of processes to use
    video_urls = playlist.video_urls
    video_files = pool.map(download_video, video_urls)
    stitch_clips(video_files, playlist.title)
    for file in video_files:
        # construct the full path of the file
        file_path = os.path.abspath(file)

        # check if file exists and is a regular file
        if os.path.isfile(file_path):
            # delete the file
            os.remove(file_path)
