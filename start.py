#coding = utf-8
import wda
import random
import os
import time
from PIL import Image

c = wda.Client()
s = c.session()
result = False

def random_input_data():
    random_data = random.randint(0, 3)
    x = 15 + random_data * 33
    y = 384
    s.double_tap(x, y)
    s.double_tap(x, y)

def main_menu():
    '''
    return main menu and refresh
    '''
    s.swipe_right()
    s.tap(40, 538)

def estimate_same(pic1, pic2):
    '''
    judge is that two picture is the same
    return bool
    '''
    the_pic1 = Image.open(pic1)
    the_pic2 = Image.open(pic2)
    the_pixel1 = []
    the_pixel2 = []
    for a in range(10):
        x = random.randint(0, 460)
        y = random.randint(333, 430)
        the_pixel1.append(the_pic1.getpixel((x, y)))
        the_pixel2.append(the_pic2.getpixel((x, y)))
    return the_pixel1 == the_pixel2

def page_method():
    '''
    action for each page
    '''
    s.double_tap(40, 538) #点赞
    s.tap(280, 538) #回复
    s.tap(120, 538) #点击回复框
    random_input_data()
    s.tap(37, 334) #点击字
    s.tap(287, 291) #发布
    s.swipe_right()
    s.swipe_left()

def next_page():
    '''
    To the next page
    '''
    s.swipe_left()

while not result:
    c.screenshot('1.png')
    page_method()
    c.screenshot('2.png')
    result = estimate_same('1.png', '2.png')
    main_menu() if result else page_method()
    os.system('re -rm *.png')
