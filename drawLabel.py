import os
import cv2
import numpy as np
import math

def draw_axis(img, yaw, pitch, roll, tdx=None, tdy=None, size=25):
    # print(type(img))
    pitch = pitch * np.pi / 180
    yaw = -(yaw * np.pi / 180)
    roll = roll * np.pi / 180
    # roll = - roll * np.pi / 180

    if tdx != None and tdy != None:
        tdx = tdx
        tdy = tdy
    else:
        height, width = img.shape[:2]
        tdx = width / 2
        tdy = height / 2

    # X-Axis pointing to right. drawn in red
    x1 = size * (math.cos(yaw) * math.cos(roll)) + tdx
    y1 = size * (math.cos(pitch) * math.sin(roll) + math.cos(roll) * math.sin(pitch) * math.sin(yaw)) + tdy

    # Y-Axis | drawn in green
    #        v
    x2 = size * (-math.cos(yaw) * math.sin(roll)) + tdx
    y2 = size * (math.cos(pitch) * math.cos(roll) - math.sin(pitch) * math.sin(yaw) * math.sin(roll)) + tdy

    # Z-Axis (out of the screen) drawn in blue
    x3 = size * (math.sin(yaw)) + tdx
    y3 = size * (-math.cos(yaw) * math.sin(pitch)) + tdy

    cv2.line(img, (int(tdx), int(tdy)), (int(x1), int(y1)), (0, 0, 255), 2)
    cv2.line(img, (int(tdx), int(tdy)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.line(img, (int(tdx), int(tdy)), (int(x3), int(y3)), (255, 0, 0), 1)

    return img
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


def _is_img(file_name):
    ext = file_name.split('.')[-1]
    return ext in ['jpg', 'jpeg', 'png', 'bmp']
# 载入json文件
def loadJson(label_path):
    import json
    try:
        with open(label_path, 'r') as fin:
            # curr_label = json.load(fin)
            curr_label = json.load(fin)
        # print('[load]', label_name, curr_label)
        # exit(0)
        return curr_label
    except Exception as e:
        QMessageBox.warning(self, 'Warning', str(e))
        return None
# 加载参数
# import argparse
# parser = argparse.ArgumentParser(description=' your project description')
# parser.add_argument('--InputPath',  type=str)
# parser.add_argument('--OutputPath', type=str)
# args = parser.parse_args()
#
# InputPath = args.InputPath
# OutputPath = args.OutputPath

InputPath = r'C:\Users\DM\Documents\WXWork\1688854007436323\Cache\File\2019-07\unlabeled_images-manfu'


OutputPath =r'D:\workspace\xmc\label\label_headDirection\reference_label_tool\testDrawOut'


if __name__ == '__main__':
    mkdir(OutputPath)
    file_list = sorted([name for name in os.listdir(InputPath) if _is_img(name)])
    print(file_list)
    for img_path in file_list:
        json = os.path.join(InputPath, img_path.split('.')[0] + '.json')
        # json = os.path.join(InputPath, 'corse_' + img_path.split('.')[0] + '.json')
        img_path = os.path.join(InputPath,img_path)
        if not os.path.isfile(json):
            print('not exist ' + json)
        else:
            curr_label = loadJson(json)
            print(curr_label)
            try:
                with open(img_path, 'rb') as f:
                    img = cv2.imread(img_path)
                    # print(curr_label['yaw'])
                    # print(curr_label['pitch'])
                    # print(curr_label['roll'])

                    emptyImage2 = draw_axis(img, curr_label['yaw'], curr_label['pitch'], curr_label['roll'])
                    cv2.imwrite(os.path.join(OutputPath, 'draw_axis', img_path), img)
            except Exception as e:
                print(e)
        # exit(0)


















