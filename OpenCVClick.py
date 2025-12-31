

import pyautogui
import pyscreeze
import cv2
import os
import sys



# 屏幕缩放系数 mac缩放是2 windows一般是1
screenScale=1

def get_correct_script_dir():
    """
    获取正确的程序目录：
    - 未打包（py文件）：返回py文件所在目录
    - 已打包（exe）：返回exe文件所在目录
    """
    if getattr(sys, 'frozen', False):
        # 打包成exe后的逻辑：sys.executable是exe文件的完整路径
        script_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        # 未打包的逻辑：原来的py文件目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
    return script_dir

def find_image(imgName):

    print(f"您好，{imgName}！")
    script_dir = get_correct_script_dir()
    target_path = os.path.join(script_dir, imgName)
    print("图片目录：" + target_path)
    target = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot = pyscreeze.screenshot('my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'my_screenshot.png', cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    print("目标图宽高：" + str(twidth) + "-" + str(theight))
    print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return twidth,theight, mn_val, max_val, min_loc, max_loc

#事先读取按钮截图
imgName = input("请输入图片名字：")
twidth,theight,mn_val, max_val, min_loc, max_loc  = find_image(imgName)
if(max_val>=0.9):
    top_left = max_loc
    bottom_right = (top_left[0] + twidth, top_left[1] + theight)
    tagHalfW = int(twidth/2)
    tagHalfH = int(theight/2)
    tagCenterX = top_left[0] + tagHalfW
    tagCenterY = top_left[1] + tagHalfH
    pyautogui.click(tagCenterX, tagCenterY, button='left')
    print("已经找到")
    isFind=True
else:
	print ("没找到")


imgName = input("请输入pico 连接状态图片名字：")
twidth,theight,mn_val, max_val, min_loc, max_loc  = find_image(imgName)
if(max_val>=0.9):
    top_left = max_loc
    bottom_right = (top_left[0] + twidth, top_left[1] + theight)
    tagHalfW = int(twidth/2)
    tagHalfH = int(theight/2)
    tagCenterX = top_left[0] + tagHalfW
    tagCenterY = top_left[1] + tagHalfH
    pyautogui.click(tagCenterX, tagCenterY, button='left')
    print("已经找到")
    isFind=True
else:
	print ("没找到")
