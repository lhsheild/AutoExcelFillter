import os
import shutil


if __name__ == '__main__':
    path = r'D:\Project\PythonProjects\AutoExceller\output'
    for sub_folder in os.listdir(path):
        sub_folder = os.path.abspath(os.path.join(path, sub_folder))
        if os.path.isdir(sub_folder):
            if not os.path.exists(os.path.abspath(os.path.join(sub_folder, '照片'))):
                os.makedirs(os.path.abspath(os.path.join(sub_folder, '照片')))
                # pic_folder = os.path.abspath(os.path.join(sub_folder, '照片'))

            for file in os.listdir(sub_folder):
                if os.path.splitext(file)[-1][1:] == "jpg" or os.path.splitext(file)[-1][1:] == 'png':
                    pic_folder = os.path.abspath(os.path.join(sub_folder, '照片'))
                    shutil.move(os.path.abspath(os.path.join(sub_folder       , file)),
                                os.path.abspath(os.path.join(pic_folder, file)))

            # for dirpath, dirnames, filenames in os.walk(sub_folder):
            #     for file in filenames:
            #         if os.path.splitext(file)[-1][1:] == "jpg" or os.path.splitext(file)[-1][1:] == 'png':
            #             pic_folder = os.path.abspath(os.path.join(dirpath, '照片'))
            #             shutil.move(os.path.abspath(os.path.join(dirpath, file)), os.path.abspath(os.path.join(pic_folder, file)))
            #             print(os.path.basename(os.path.abspath(os.path.join(dirpath, file))))