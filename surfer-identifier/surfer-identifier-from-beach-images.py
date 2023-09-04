from landingai.predict import Predictor
from landingai.pipeline.image_source import NetworkedCamera, FrameSet

# Replace with your own endpoint_id and api_key that will be provided by Landing AI
endpoint_id = ""
api_key = ""
# Image source for the video stream
playlist_url = "https://live.hdontap.com/hls/hosb1/topanga_swellmagnet.stream/playlist.m3u8"

video_len_sec = 10
fps = 2

surfer_model = Predictor(endpoint_id, api_key=api_key)
vid_src = NetworkedCamera(playlist_url, fps=fps)
frs = FrameSet()
for i, frame in enumerate(vid_src):
    if i >= video_len_sec * fps:
        break
    # Get predictions for each frame and then overlay the predictions
    # on the frame for visualizing
    frs.extend(frame)

frs.run_predict(predictor=surfer_model).overlay_predictions()