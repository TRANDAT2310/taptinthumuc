import os
def creating_directory():
    directory = "nnlt"
    parent_dir = "D:/data/"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print("Directory '% s' created" % directory)
    return directory
creating_directory()