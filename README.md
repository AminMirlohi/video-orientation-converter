# video-orientation-converter

This Python project provides a convenient solution to transform videos from a horizontal aspect ratio to a vertical aspect ratio. It uses the popular `moviepy` library to perform the necessary video processing operations.

### Features

- Converts horizontal videos to vertical orientation
- Retains the original video quality during the aspect ratio transformation
- Supports various video formats, including MP4, AVI, MOV, etc.
- Automatically adjusts the video height and width for optimal output

### Usage

1. Install the required dependencies:

```
pip install moviepy
```

2. Import the package and call the `convert_horizontal_to_vertical` function with the file paths for the input and output videos:

```python
from video_aspect_ratio_transformer import convert_horizontal_to_vertical

input_video_path = "path_to_input_video.mp4"
output_video_path = "path_to_output_video.mp4"

convert_horizontal_to_vertical(input_video_path, output_video_path)
```

### Contributions

Contributions to this project are welcome! If you have any ideas or improvements, feel free to submit a pull request. Please ensure that your changes adhere to the established coding guidelines and pass the unit tests.

### License

This project is licensed under the [MIT License](LICENSE.txt).

### Acknowledgements

- This project utilizes the `moviepy` library. Special thanks to the creators and contributors of `moviepy`.
- We appreciate the open-source community for their valuable resources and guidance.
