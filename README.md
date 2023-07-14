# badapple_on_CCaption
在CC字幕上观看badapple
# 如何使用
## 第一步，准备你的视频文件和ffmpeg
你可以从[这里](https://ffmpeg.org/)下载ffmpeg，并且按照网上的教程将ffmpeg添加到你的环境变量。<br>
接着，从[这里](https://www.bilibili.com/video/BV1xx411c79H/)下载badapple的PV，您需要注意，下载的视频的帧率必须为15帧每秒，不然可能会导致处理出来的画面有延迟。<br>
如果您不是15帧每秒，请使用以下命令：
```
ffmpeg -i badapple.mp4 -r 15 15fps.mp4 
```
其中，badapple.mp4是输入文件，15fps.mp4是输出文件。<br>
程序内还提供了10帧，30帧的选项，具体操作如下：<br>
如果您的视频是30帧每秒，请注释掉text_to_srt.py的第二行代码，删除第一行代码前面的#号<br>
如果您的视频是10帧每秒，请注释掉text_to_srt.py的第二行代码，删除第三行代码前面的#号<br>
（实际上就是改了ms列表）
## 第二步，将视频全部帧提取出来
请使用以下命令:<br>
```
ffmpeg -i "badapple.mp4" -vf "select=between(n\,0\,6573)*not(mod(n\,1))" -vsync 0 D:\output\%05d.jpg
```
其中，badapple.mp4是视频的位置，您最好使用绝对位置，最后面的D:\output\%05d.jpg是保存的位置，%05d.jpg可以让ffmpeg将提取出来的帧命名为xxxxx.jpg（5位数字），这样比较方便排序和处理，这个位置可以自行更改<br>
## 第三步，准备运行环境
你需要准备的库有numpy，cv2，colorama，pillow<br>
(实际上colorama纯粹就是为了好看的，将其从源代码中删掉也可以)
```
pip install colorama
pip install pillow
pip install numpy
```
由于openCV的库有一些特殊（我这边直接用pip安装跑不起来），您可能要参考[这篇教程](https://blog.csdn.net/m0_73767377/article/details/130072986)
## 第四步，处理视频
将文件解压至D:\python_projects\badapple_on_CCaption目录下，如果不复制到此处，您可能需要修改代码中以下位置：

|文件  |行数|
|---|---|
|main.py  |12,15,16|
|srtprogress.py  |16,18,54,76|
|text_to_srt.py  |49|

下一步，在D:\python_projects\badapple_on_CCaption目录下新建done及text_output文件夹，这些分别用来存储分割后的图片和转成字符后的图片<br>
首先，运行main.py，其作用是将一帧一帧的图片分割成48x48的小块，其生成的结果会保存在done文件夹下。<br>
下一步，运行srtprogress.py，其作用是将小块转化成实心和空心的字符，其生成的结果会保存在text_output文件夹下<br>
下一步，运行text_to_srt.py，其作用是将字符重新排列成srt的字幕文件，处理时间大概几秒到十几秒，完成后会在程序根目录下生成srt.srt文件<br>
