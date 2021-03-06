#Python 3
import os


def main():
    path = input("Enter the folder directory: ")
    if os.path.isdir(path):
        print("Dir OK.\n")
    else:
        print("Not a dir.\n")
        exit(0)
    fileList = os.listdir(path)

    os.chdir(path)
    renameDocPath = "title.txt"

    fileType = '.mp4'
    specifiedFileType = input('Enter the file type. Ex: mp4 . Default is mp4 \n').strip('\n')
    if specifiedFileType != '':
        fileType = '.' + specifiedFileType
        print(fileType, 'OK.\n')
    else:
        print('Using default .mp4.\n')

    try:
        with open(renameDocPath) as f:
            renameList = f.readlines()
    except FileNotFoundError:
        print("File not exists")
        exit(0)

    ithLine = 2
    for file in fileList:
        if ithLine >= len(renameList):
            print("There are other files needed to be manually changed.\n")
            break
        if '[00]' in file or file == "title.txt":
            print("Skipped the [00] episode.\n", file, "\n")
        else:
            print("Renaming file: ", file, " to: ", renameList[ithLine].strip('\n')+fileType)
            srcPath = file
            dstPath = renameList[ithLine].strip('\n')+fileType
            os.rename(srcPath, dstPath)
            ithLine += 1

    os.chdir('D:\\BaiduNetdiskDownload')
    print('Working path changed to D:\\BaiduNetdiskDownload .\n')
    os.rename(path, 'D:\\BaiduNetdiskDownload\\' + renameList[0].replace(' ', '', 1).strip())


if __name__ == "__main__":
    main()
