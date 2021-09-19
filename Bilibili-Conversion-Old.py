import os
import json
# from moviepy.editor import *


path = r"E:\待转换文件"    # 待转换文件的路径，请修改为自己的

save_path = r"E:\output"  # 转换完毕后的存放路径，可以修改为需要的

if __name__ == '__main__':

    all_title = []
    all_video = []

    for k, (a, b, c) in enumerate(os.walk(path)):
        e = []
        for i in c:
            if i == 'entry.json':
                title_path = os.path.join(a, i)
                all_title.append(title_path)
            elif os.path.splitext(i)[1] == '.blv':
                video_path = os.path.join(a, i)
                e.append(video_path)
                all_video.append(e)

    for i, j in enumerate(all_title):
        with open(j, encoding='utf-8') as data:
            title_ = json.load(data)
            title1 = title_["title"].replace(" ", "")
            title2 = title_["page_data"]["part"].replace(" ", "")
            print(f"输出目录：{title1}")
            print(f"输出文件：{title2}")
            _path = f"{save_path}/{title1}"
            os.makedirs(_path, exist_ok=True)
            with open(f"{title2}.txt", "w", encoding='utf-8') as w:
                [w.write(f"file '{i}'\n") for i in all_video[i]]
            cmd = f'ffmpeg -f concat -safe 0 -i {title2}.txt -c copy {_path}/{title2}.mp4'
            os.system(cmd)

        print("\n", "*" * 15, f"已完成{i + 1}个文件", "*" * 15)
        
