import cv2
import os


def scrape_videos_for_frames(videos_dir, image_dir, delay):
    """Takes in the path of a folder containing
    multiple videos and another path where it saves all
    captured frames from all files into one folder"""
    image_counter = 1
    videos_dir_content = os.listdir(videos_dir)
    if videos_dir or image_dir:
        for video in videos_dir_content:
            #  path for saved frames for each video
            current_video_dir = os.path.join(videos_dir, video)
            cap = cv2.VideoCapture(current_video_dir)
            fps = cap.get(cv2.CAP_PROP_FPS)
            delay = int(fps * delay)
            i = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                if i % delay == 0:
                    cv2.imwrite(os.path.join(image_dir,
                                             'img' + str(image_counter) + '.jpg'), frame)
                    image_counter += 1

                i += 1
            cap.release()
            cv2.destroyAllWindows()
    else:
        print('specify input and output directories')


# *****************************************************************************
# *******************************************PROGRESS BAR ***********************
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()
