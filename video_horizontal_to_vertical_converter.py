from moviepy.editor import VideoFileClip

def convert_horizontal_to_vertical(input_video_path, output_video_path):
    # Load the video clip from the given input path
    video_clip = VideoFileClip(input_video_path)
    
    # Resize the video clip to have a vertical orientation by swapping the height and width
    vertical_clip = video_clip.resize(height=video_clip.size[0], width=video_clip.size[1])
    
    # Rotate the vertical clip by 90 degrees clockwise to convert it to a vertical orientation
    vertical_clip = vertical_clip.rotate(90, expand=True)
    
    # Write the final vertical clip to the given output path as a video file
    vertical_clip.write_videofile(output_video_path)

# Example usage
input_path = "path_to_input_video.mp4"
output_path = "path_to_output_video.mp4"

# Convert the input video from horizontal to vertical and save the output to the specified path
convert_horizontal_to_vertical(input_path, output_path)
