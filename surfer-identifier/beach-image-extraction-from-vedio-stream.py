from landingai.pipeline.image_source import NetworkedCamera, FrameSet

playlist_url = "https://live.hdontap.com/hls/hosb1/topanga_swellmagnet.stream/playlist.m3u8"

# Define the length of the video you want to capture and the fps
video_len_sec = 10
fps = 2

# Initialize the camera object which will allow you to obtain the video
# stream and the FrameSet which allows you to save and process the frames
vid_src = NetworkedCamera(playlist_url, fps=fps)
frs = FrameSet()
for i, frame in enumerate(vid_src):
    # limit the capture time so we don't capture frames forever
    if i >= video_len_sec * fps:
        break
    frs.extend(frame)

# Save your frames as beach-images with the prefix "surfers"
frs.save_image(filename_prefix="surfers")