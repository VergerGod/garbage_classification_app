# 导入相应模块
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests
import time
# 定义跳转函数
def go_home():
    find_frame.pack_forget()
    quest_frame.pack_forget()
    news_frame.pack_forget()
    push_frame.pack_forget()
    begin_frame.pack()
def go_find():
    begin_frame.pack_forget()
    quest_frame.pack_forget()
    news_frame.pack_forget()
    push_frame.pack_forget()
    find_frame.pack()
def go_quest():
    begin_frame.pack_forget()
    find_frame.pack_forget()
    news_frame.pack_forget()
    push_frame.pack_forget()
    quest_frame.pack()
def go_news():
    begin_frame.pack_forget()
    find_frame.pack_forget()
    quest_frame.pack_forget()
    push_frame.pack_forget()
    news_frame.pack()
def go_push():
    begin_frame.pack_forget()
    find_frame.pack_forget()
    quest_frame.pack_forget()
    news_frame.pack_forget()
    push_frame.pack()

# create root
root = tk.Tk()
root.title('垃圾分类，从我做起！')
root.geometry('1024x600')
root.resizable(width=False, height=False)
# change icon
icon_get = requests.get('https://ftp.bmp.ovh/imgs/2021/04/e5e0774b1bdf7cdb.png')
icon_img = Image.open(BytesIO(icon_get.content))
icon_pho = ImageTk.PhotoImage(icon_img)
root.iconphoto(True, icon_pho)
# create basic frames
icon_frame = tk.Frame()
begin_frame = tk.Frame()
find_frame = tk.Frame()
quest_frame = tk.Frame()
news_frame = tk.Frame()
push_frame = tk.Frame()
# pack begin_frame
icon_frame.pack(fill='x')
begin_frame.pack()


# fill icon_frame
tk.Button(icon_frame, text='垃圾分类交互平台', font=('微软雅黑', 16, 'bold'), width=15, height=2, command=go_home).pack(side='left')
tk.Button(icon_frame, text='查询分类', font=('微软雅黑', 16), width=15, height=2, bg='lightyellow', command=go_find).pack(side='left')
tk.Button(icon_frame, text='分类问答', font=('微软雅黑', 16), width=15, height=2, bg='lightblue', command=go_quest).pack(side='left')
tk.Button(icon_frame, text='相关新闻', font=('微软雅黑', 16), width=15, height=2, bg='lightgreen', command=go_news).pack(side='left')
tk.Button(icon_frame, text='知识普及', font=('微软雅黑', 16), width=15, height=2, bg='pink', command=go_push).pack(side='left')


# fill begin_window
# 顶部放上天气状况
coming_url = 'http://api.tianapi.com/txapi/tianqi/index?key=308557e43bd113a0f240ff59cfa66ad2&city=北京市'
coming_get = requests.get(coming_url)
coming_json = coming_get.json()
coming_list = coming_json['newslist']
coming_today = coming_list[0]
today_date = coming_today['date']
today_week = coming_today['week']
today_weat = coming_today['weather']
today_wind = coming_today['wind']
today_text = '北京' + ' ' + today_date + ' ' + today_week + ' ' + today_weat + ' ' + today_wind
tk.Label(begin_frame, text=today_text, font=('微软雅黑', 16)).pack()
# 下方放上宣传海报
def change_img(i):
    if i % 4 == 1:
        pop_label.configure(image=public_pho_0)
        i = i + 1
        pop_label.after(2000, change_img, i)
    elif i % 4 == 2:
        pop_label.configure(image=public_pho_1)
        i = i + 1
        pop_label.after(2000, change_img, i)
    elif i % 4 == 3:
        pop_label.configure(image=public_pho_2)
        i = i + 1
        pop_label.after(2000, change_img, i)
    else:
        pop_label.configure(image=public_pho_3)
        i = i + 1
        pop_label.after(2000, change_img, i)
public_0 = 'https://ftp.bmp.ovh/imgs/2021/04/2c5b827c6a265c8a.jpg'
public_1 = 'https://ftp.bmp.ovh/imgs/2021/05/2897bbf47f115bdf.jpeg'
public_2 = 'https://ftp.bmp.ovh/imgs/2021/05/3c43b46e12cd0fa6.jpeg'
public_3 = 'https://ftp.bmp.ovh/imgs/2021/05/7d1759d9effe4766.jpeg'
public_list = [public_0, public_1, public_2, public_3]
for i, public in zip(range(4), public_list):
    locals()['public_get_'+str(i)] = requests.get(public)
    locals()['public_img_'+str(i)] = Image.open(BytesIO(locals()['public_get_'+str(i)].content))
    locals()['public_mod_'+str(i)] = locals()['public_img_'+str(i)].resize((800, 500), Image.ANTIALIAS)
    locals()['public_pho_'+str(i)] = ImageTk.PhotoImage(locals()['public_mod_'+str(i)])
pop_label = tk.Label(begin_frame)
pop_label.pack()
change_img(1)


# fill find_window
def find_type():
    if input_name == '':
        messagebox.showinfo('提示', '要先输入垃圾名称哦！')
        return
    text_name = input_name.get()
    quest_url = 'https://api.66mz8.com/api/garbage.php?name=' + text_name
    quest_get = requests.get(quest_url)
    quest_json = quest_get.json()
    gar_type = quest_json['data']
    tk.Label(find_find_frame, text=gar_type, font=('微软雅黑', 16), relief='groove').pack()
# create frame
find_top_frame = tk.Frame(find_frame)
find_mid_frame = tk.Frame(find_frame)
find_bot_frame = tk.Frame(find_frame)
find_find_frame = tk.Frame(find_frame)
separator_0 = ttk.Separator(find_frame, orient='horizontal')
# pack frame
find_top_frame.pack()
find_find_frame.pack()
separator_0.pack(pady=4, fill='x')
find_mid_frame.pack()
find_bot_frame.pack()
# 上栏放上提示语、输入框、查询按钮和退出按钮
tk.Label(find_top_frame, text='请输入垃圾名称：', font=('微软雅黑', 16)).pack(side='left')
input_name = tk.Entry(find_top_frame, font=('微软雅黑', 16))
input_name.pack(side='left')
tk.Button(find_top_frame, text='查询', font=('微软雅黑', 16), command=find_type).pack(side='left')
# 中部左栏放上热门搜索API
star_url = 'http://api.tianapi.com/txapi/hotlajifenlei/index?key=308557e43bd113a0f240ff59cfa66ad2'
star_get = requests.get(star_url)
star_json = star_get.json()
star_news = star_json['newslist']
tk.Label(find_mid_frame, text='热 门 搜 索：\n', font=('微软雅黑', 14)).pack()
for i in range(10):
    star_rank = star_news[i]
    star_name = star_rank['name']
    tk.Label(find_mid_frame, text=star_name, font=('微软雅黑', 14)).pack(side='left')
# 下栏放上图片
# format rubbish photo
rub_get_0 = requests.get('https://ftp.bmp.ovh/imgs/2021/04/7cb9116591d6893b.png')
rub_get_1 = requests.get('https://ftp.bmp.ovh/imgs/2021/04/6d4733f1fbe7d87a.png')
rub_get_2 = requests.get('https://ftp.bmp.ovh/imgs/2021/04/d1268c675af54d48.png')
rub_get_3 = requests.get('https://ftp.bmp.ovh/imgs/2021/04/744902bf31d085ae.png')
rub_img_0 = Image.open(BytesIO(rub_get_0.content))
rub_pho_0 = ImageTk.PhotoImage(rub_img_0)
rub_img_1 = Image.open(BytesIO(rub_get_1.content))
rub_pho_1 = ImageTk.PhotoImage(rub_img_1)
rub_img_2 = Image.open(BytesIO(rub_get_2.content))
rub_pho_2 = ImageTk.PhotoImage(rub_img_2)
rub_img_3 = Image.open(BytesIO(rub_get_3.content))
rub_pho_3 = ImageTk.PhotoImage(rub_img_3)
tk.Label(find_bot_frame, image=rub_pho_0).pack(side='left')
tk.Label(find_bot_frame, image=rub_pho_1).pack(side='left')
tk.Label(find_bot_frame, image=rub_pho_2).pack(side='left')
tk.Label(find_bot_frame, image=rub_pho_3).pack(side='left')


# fill quest_window
quiz_url = 'http://api.tianapi.com/txapi/anslajifenlei/index?key=308557e43bd113a0f240ff59cfa66ad2'
quiz_get = requests.get(quiz_url)
quiz_json = quiz_get.json()
quiz_list = quiz_json['newslist']
quiz_0 = quiz_list[0]
quiz_name = quiz_0['name']
quiz_type = quiz_0['type']
def judge():
    quiz_one = v.get()
    if quiz_one == quiz_type:
        messagebox.showinfo('提示', '答对了，你真棒！')
    else:
        messagebox.showinfo('提示', '没答对，继续努力哦！')
# create frame
quiz_frame = tk.Frame(quest_frame)
frame_01 = tk.Frame(quest_frame)
frame_23 = tk.Frame(quest_frame)
separator_1 = ttk.Separator(quest_frame, orient='horizontal')
return_frame = tk.Frame(quest_frame)
# pack frame
quiz_frame.pack()
separator_1.pack(pady=4, fill='x')
frame_01.pack()
frame_23.pack()
return_frame.pack()
# pack label
tk.Label(quiz_frame, text='请选择相应的垃圾类型\n', font=('微软雅黑', 14)).pack()
tk.Label(quiz_frame, text=quiz_name, font=('微软雅黑', 14)).pack()
v = tk.IntVar()
tk.Radiobutton(frame_01, text='厨余垃圾', image=rub_pho_0, value=2, indicatoron=False, variable=v, command=judge).pack(side='left')
tk.Radiobutton(frame_01, text='可回收物', image=rub_pho_1, value=0, indicatoron=False, variable=v, command=judge).pack(side='left')
tk.Radiobutton(frame_23, text='有害垃圾', image=rub_pho_2, value=1, indicatoron=False, variable=v, command=judge).pack(side='left')
tk.Radiobutton(frame_23, text='其他垃圾', image=rub_pho_3, value=3, indicatoron=False, variable=v, command=judge).pack(side='left')


# fill news_frame
# create city_frame and look_frame
city_frame = tk.Frame(news_frame)
look_frame = tk.Frame(news_frame)
# pack city_frame and look_frame
city_frame.pack(side='left')
look_frame.pack(side='left')
# fill city_frame
tk.Button(city_frame, text='北京', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='上海', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='广州', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='深圳', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='南京', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='郑州', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='西安', font=('微软雅黑', 16), width=10).pack(pady=3)
tk.Button(city_frame, text='武汉', font=('微软雅黑', 16), width=10).pack(pady=3)
# fill look_frame
news_url = 'http://api.tianapi.com/lajifenleinews/index?key=308557e43bd113a0f240ff59cfa66ad2&num=5&word='+'北京'
news_get = requests.get(news_url)
news_json = news_get.json()
news_list = news_json['newslist']
for i in range(5):
    # create row frame
    locals()['news_row_' + str(i)] = tk.Frame(look_frame)
    # pack row frame
    locals()['news_row_' + str(i)].pack()
    # create and pack separator
    ttk.Separator(news_frame).pack(fill='x')
    # create cat and dog frame
    locals()['cat_' + str(i)] = tk.Frame(locals()['news_row_' + str(i)])
    locals()['dog_' + str(i)] = tk.Frame(locals()['news_row_' + str(i)])
    # pack cat and dog frame
    locals()['cat_' + str(i)].pack(side='left')
    locals()['dog_' + str(i)].pack(side='left')
    # get API list
    news = news_list[i]
    news_ctime = news['ctime']
    news_title = news['title']
    news_description = news['description']
    news_picurl = news['picUrl']
    newspic_get = requests.get(news_picurl)
    newspic_img = Image.open(BytesIO(newspic_get.content))
    newspic_mod = newspic_img.resize((200, 100), Image.ANTIALIAS)
    locals()['newspic_pho' + str(i)] = ImageTk.PhotoImage(newspic_mod)
    # pack label and message
    tk.Label(locals()['dog_' + str(i)], text=news_title, font=('微软雅黑', 14)).pack()
    tk.Message(locals()['dog_' + str(i)], text=news_description, font=('微软雅黑', 10), width=600).pack()
    tk.Label(locals()['dog_' + str(i)], text=news_ctime, font=('微软雅黑', 10)).pack()
    tk.Label(locals()['cat_' + str(i)], image=locals()['newspic_pho' + str(i)]).pack()
# fill push_frame
# create frame
push_left_frame = tk.Frame(push_frame)
push_hand_frame = tk.Frame(push_frame)
# pack frame
push_left_frame.pack(side='left', padx=24)
push_hand_frame.pack(side='left', padx=24)
# fill left frame
def go_upon():
    push_see_2.pack_forget()
    push_see_3.pack_forget()
    push_see_0.pack(side='left', padx=16, pady=16)
    push_see_1.pack(side='left', padx=16, pady=16)
def go_down():
    push_see_0.pack_forget()
    push_see_1.pack_forget()
    push_see_2.pack(side='left', padx=16, pady=16)
    push_see_3.pack(side='left', padx=16, pady=16)
tk.Button(push_left_frame, text='厨余垃圾&可回收物', font=('微软雅黑', 16), command=go_upon).pack(pady=16)
tk.Button(push_left_frame, text='有害垃圾&其他垃圾', font=('微软雅黑', 16), command=go_down).pack(pady=16)
# fill hand frame
push_url_0 = 'https://ftp.bmp.ovh/imgs/2021/04/3c6c01e10120a6ef.png'
push_url_1 = 'https://ftp.bmp.ovh/imgs/2021/04/dcddff30c19da416.png'
push_url_2 = 'https://ftp.bmp.ovh/imgs/2021/04/da7c74803adec85c.png'
push_url_3 = 'https://ftp.bmp.ovh/imgs/2021/04/b96fb5aa87555dc9.png'
push_list = [push_url_0, push_url_1, push_url_2, push_url_3]
for i, push in zip(range(4), push_list):
    locals()['push_get_'+str(i)] = requests.get(push)
    locals()['push_img_'+str(i)] = Image.open(BytesIO(locals()['push_get_'+str(i)].content))
    locals()['push_mod_'+str(i)] = locals()['push_img_'+str(i)].resize((329, 465), Image.ANTIALIAS)
    locals()['push_pho_'+str(i)] = ImageTk.PhotoImage(locals()['push_mod_'+str(i)])
    locals()['push_see_'+str(i)] = tk.Label(push_hand_frame, image=locals()['push_pho_'+str(i)])
push_see_0.pack(side='left', padx=16, pady=16)
push_see_1.pack(side='left', padx=16, pady=16)
root.mainloop()
