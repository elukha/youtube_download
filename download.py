pip install yt-dlp



video_youtube_url = input(str("urlを入力してください")) #URLを入力

####################################################################

%rm sagemaker-studiolab-notebooks/save_videos/video.mp4 #mp4のファイルを削除

####################################################################

import yt_dlp      #youtubeからmp4をダウンロード

# カスタマイズしたオプションを設定
ydl_opts = {
    'outtmpl': 'sagemaker-studiolab-notebooks/save_videos/video.mp4',  # ファイル名と保存場所を指定
}

# YoutubeDLインスタンスを作成してダウンロード
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_youtube_url])

###################################################################

from IPython.display import Video   #ダウンロードしたファイルを表示します
Video("sagemaker-studiolab-notebooks/save_videos/video.mp4")
