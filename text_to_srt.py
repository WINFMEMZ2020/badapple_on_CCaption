ms = ['000', '030', '060', '090', '120', '150', '180', '210', '240', '270', '300', '330', '360', '420', '450', '510', '540', '570', '600', '630', '690', '720', '750', '780', '840', '870', '900', '930', '960', '990']
import os
os.system("chcp 65001")
os.system("cls")

def time_adding(hour,minutes,seconds,mseconds):
	a = hour
	b = minutes
	c = seconds
	d = mseconds
	a = int(a)
	b = int(b)
	c = int(c)
	#先获取当前时间索引
	d = ms.index(mseconds)
	e = d + 1
	try:
		f = ms[e]
	except IndexError:  #说明输入的毫秒是999
		f = ms[0]
		c = c + 1
	if c >= 60:
		b = b + 1
		c = 0
	if b >= 60:
		a = a + 1
		b = 0
	a = str(a).zfill(2)
	b = str(b).zfill(2)
	c = str(c).zfill(2)
	d = str(d).zfill(3)
	time = {}
	time["hour"] = a
	time["minutes"] = b
	time["seconds"] = c
	time["mseconds"] = f
	return time
	
#print(time_adding(0,59,59,"999"))
#os.system("pause")
now_hour = 0
now_minutes = 0
now_seconds = 0
now_mseconds = "000"
srt_number = 1
open_path = r"D:\python_projects\badapple_on_CCaption\\" + "text_output" + r"\\"  # 拼接出处理文件夹的完整路径
folder_content = os.listdir(open_path)
srt = ""
for txt in folder_content:
	txt_path = open_path + "\\" +  txt
	with open(txt_path,encoding = "UTF=8") as file_object:
		txt_content = file_object.read()
		txt_content = txt_content.strip()
		target_time_dict = time_adding(hour=now_hour,minutes=now_minutes,seconds = now_seconds,mseconds=now_mseconds)
		time_to = str(now_hour).zfill(2) + ":" + str(now_minutes).zfill(2) + ":" + str(now_seconds).zfill(2) + "," + now_mseconds + " --> " + str(target_time_dict["hour"]).zfill(2) + ":" +  str(target_time_dict["minutes"]).zfill(2) +":"+ str(target_time_dict["seconds"]).zfill(2) +"," +  target_time_dict["mseconds"]
		#print(time_to)
		now_hour = target_time_dict["hour"]
		now_minutes = target_time_dict["minutes"]
		now_seconds = target_time_dict["seconds"]
		now_mseconds = target_time_dict["mseconds"]
		srt = srt + str(srt_number) + "\n" + time_to + "\n" + "fps:30.00\n" + txt_content + "\n\n"
		srt_number = srt_number + 1


with open("srt.srt","w",encoding = "UTF-8") as file_object:
	file_object.write(srt)
