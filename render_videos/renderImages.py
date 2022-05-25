import os
import cv2


def renderVideo(images, outputPath):

    width, height = (1600, 900)

    filename = os.path.join(outputPath, "recap.mp4")

    video = cv2.VideoWriter(
        filename, cv2.VideoWriter_fourcc(*'MP4V'), 2, (width, height))

    for idx, image in enumerate(images):

        resized = cv2.resize(cv2.imread(image), (width, height))

        video.write(resized)
        print("Writing frame " + str(idx) +
              " of " + str(len(images)) + " to: "+outputPath, flush=True)

    cv2.destroyAllWindows()
    video.release()


def deleteFolder(path):
    print("Deleting folder: " + path)
    os.system("rmdir /S /Q " + path)
