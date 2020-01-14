import ABR as ABR
from video_sim.player import VideoPlayer
from const import *

network_file_dir = 'fixed'
video_file_dir = 'sports'
Debug = True


myVideoPlayer = VideoPlayer(
    abr_model=ABR,
    network_trace=networkFileDir + network_file_dir,
    video_trace=videoFileDir + video_file_dir,
    debug=Debug
)
myVideoPlayer.reset()
myVideoPlayer.playVideo()
myVideoPlayer.show()
myVideoPlayer.result()
