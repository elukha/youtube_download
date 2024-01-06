import threading
from tkinter import *
from tkinter import ttk
import yt_dlp
import logging
import os
from youtubesearchpython import *
import sys


#関数定義
def video_download():
    Video_URL = URL.get()
    global VideoInfo
    VideoInfo = Video.getInfo(Video_URL)

    #yt-dlpのオプション
    ydl_opts = {
    'outtmpl': './' + VideoInfo["title"] + ".mp4",  # ファイル名と保存場所を指定
    'progress_hooks': [progress_bar]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([Video_URL])


def file_delete():
    os.remove("./" + VideoInfo["title"] + ".mp4")



root = Tk()

#オブジェクトの定義
label_1 = ttk.Label(root,text="Youtubeの動画をダウンロードします")
URL = ttk.Entry(root,text="URLを入力")

button_1 = ttk.Button(root,text = "MP4",command=video_download)
button_delete = ttk.Button(root,text = "ファイル削除", command=file_delete)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#プログレスバー
pb = ttk.Progressbar(root,maximu=100,mode="determinate",variable=vars)
def progress_bar(p):
  if p['status'] == 'downloading':
    pct = (p['downloaded_bytes'] / p['total_bytes'])
    result = int(pct*100)  
    pb.configure(value=result)
    pb.update()
  elif p['status'] == 'finished':
    print('Complete.')


#レイアウト
label_1.pack()
URL.pack()
button_1.pack()
button_delete.pack()
pb.pack()


root.mainloop()
