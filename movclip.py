import moviepy.editor as mp
import numpy as np

# Input video file
input_video = "input_video.mp4"

# Output video file
output_video = "output_video.mp4"

# Duration of the desired cut (in seconds)
cut_duration = 20

# Load the video
video_clip = mp.VideoFileClip(input_video)

# Calculate the duration of the input video
total_duration = video_clip.duration

# Generate a random start time within the valid range
start_time = np.random.uniform(0, total_duration - cut_duration)

# Cut the video
cut_video = video_clip.subclip(start_time, start_time + cut_duration)

# Write the cut video to the output file, preserving audio
cut_video.write_videofile(output_video, codec="libx264", audio_codec="aac")

# Close the video clip objects
video_clip.reader.close()
video_clip.audio.reader.close_proc()

print(f"Random 20-second section cut from {input_video} and saved as {output_video} with audio")
