
import os

from renderImages import renderVideo, deleteFolder


PATH = os.path.expanduser("~\Pictures\DailyRecap")


def createVideoOfFolder(path):
    print("Creating video from images in " + path)

    images = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png"):
                images.append(os.path.join(root, file))

    images.sort(key=lambda x: os.path.getmtime(x))

    videoPath = path.replace("Pictures", "Videos")

    if not os.path.exists(videoPath):
        os.makedirs(videoPath)

    renderVideo(images, videoPath)

    deleteFolder(path)


def main():
    for yearFolder in os.listdir(PATH):
        yearPath = os.path.join(PATH, yearFolder)

        for monthFolder in os.listdir(yearPath):
            monthPath = os.path.join(yearPath, monthFolder)

            for dayFolder in os.listdir(monthPath):
                dayPath = os.path.join(monthPath, dayFolder)

                if dayFolder.endswith(".done"):
                    continue

                createVideoOfFolder(dayPath)


if __name__ == "__main__":
    main()
