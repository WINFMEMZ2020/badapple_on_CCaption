# badapple_on_CCaption
在CC字幕上观看badapple
# 如何使用
## 第一步，准备你的视频文件和ffmpeg
你可以从[这里](https://ffmpeg.org/)下载ffmpeg，并且按照网上的教程将ffmpeg添加到你的环境变量。<br>
接着，从[这里](https://www.bilibili.com/video/BV1xx411c79H/)下载badapple的PV，您需要注意，下载的视频的帧率必须为30.00帧每秒，不然可能会导致处理出来的画面有延迟。<br>
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
