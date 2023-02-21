import os, sys, stat
import glob
import shutil

class FolderUtil:

    def __init__(self):
        print("init")

    @staticmethod
    def create_new_folder(folder_name):
        parent_folder = "D:/Files"
        path = os.path.join(parent_folder, folder_name)
        if os.path.exists(path) == False:
            os.mkdir(path)
            print("Folder '% s' created" % folder_name)
        else:
            print("folder already present")

    @staticmethod
    def clear_folder(folder_name):
        parent_folder = "D:/Files"
        path = os.path.join(parent_folder, folder_name)
        shutil.rmtree(path)
        os.mkdir(path)


    @staticmethod
    def move_docs_from_download_to_folder(folder_name):
        parent_folder = "D:/Files"
        source = "C:/Users/ASHESH CHAKRABORTY/Downloads"
        destination = os.path.join(parent_folder, folder_name)
        allfiles = os.listdir(source)
        for f in allfiles:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            shutil.move(src_path, dst_path)