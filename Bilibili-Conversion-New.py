import os
import json


path = r"D:\待转换文件"     # 待转换文件的路径，请修改为自己的

save_path = r"D:\output"      # 转换完毕后的存放路径，可以修改为需要的

if __name__ == '__main__':

    all_title = []
    all_video = []
    all_audio = []

    for k, (a, b, c) in enumerate(os.walk(path)):
        for i in c:

            if i == 'entry.json':
                title_path = os.path.join(a, i)
                all_title.append(title_path)
            elif i == "video.m4s":
                video_path = os.path.join(a, i)
                all_video.append(video_path)
            elif i == "audio.m4s":
                audio_path = os.path.join(a, i)
                all_audio.append(audio_path)

    for i, j in enumerate(all_title):
        with open(j, encoding='utf-8') as data:
            title_ = json.load(data)
            title1 = title_["title"].replace(" ", "")
            title2 = title_["page_data"]["part"].replace(" ", "")
            print(f"输出目录：{title1}")
            print(f"输出文件：{title2}")
            _path = f"{save_path}/{title1}"
            os.makedirs(_path, exist_ok=True)
            cmd = f'ffmpeg -i {all_video[i]} -i {all_audio[i]} {_path}/{title2}.mp4'
            os.system(cmd)
        print("\n", "*" * 15, f"已完成{i + 1}个文件", "*" * 15)
        