import cv2
import numpy as np


def create_video(text):
    # base video params
    letter_size, between_letter_size = 30, 2
    width, height = 100, 100
    fps, video_length = 33, 3
    position_x, position_y = width, height // 2 + letter_size // 2
    path_name = 'static/video/'
    filename = 'My_run_string_video.mp4'

    # background settings
    background_color = (64, 124, 192)

    # text font settings
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale, font_weight, font_color = 1.5, 3, (255, 255, 255)

    # stream for writing new frame
    video_stream = cv2.VideoWriter(path_name + filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # base frame foundation on numpy 3D array
    frame = np.zeros((width, height, 3), dtype=np.uint8)

    # function for reset color frame on current shot
    def reset_frame():
        frame[:, :, 0] = np.ones([width, height]) * background_color[0]
        frame[:, :, 1] = np.ones([width, height]) * background_color[1]
        frame[:, :, 2] = np.ones([width, height]) * background_color[2]

    for _ in range(fps * video_length):
        # reset frame and write text on it
        reset_frame()
        position_x -= (width + len(text) * (letter_size + between_letter_size)) // (fps * video_length)  # speed text
        cv2.putText(frame, text, (position_x, position_y),
                    font, font_scale, font_color, font_weight)
        video_stream.write(frame)

    # save video
    video_stream.release()

    return filename
