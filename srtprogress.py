from PIL import Image
import os
from colorama import Back, init

init(autoreset=False)
os.system("chcp 65001")

output = {}
temp = {}
out = ""
count = -1
line_count = 1
progress = 0
frame_count = 0

for a in os.listdir(r"D:\python_projects\badapple_on_CCaption\done"):
	#print(a)
	open_path = r"D:\python_projects\badapple_on_CCaption\done\\" + a + r"\\"  # 拼接出处理文件夹的完整路径
	folder_content = os.listdir(open_path)
	for picture in folder_content:
		point_white = 0
		point_black = 0
		point_all = 0
		picture_path = open_path + picture
		picture_info_list = picture
		picture_info_list = picture_info_list.replace("_", " ")
		picture_info_list = picture_info_list.split()
		picture_line = picture_info_list[0]
		picture_count = picture_info_list[1]
		im = Image.open(picture_path)
		rgb_im = im.convert('RGB')
		for i in range(64):
			for j in range(64):
				r, g, b = rgb_im.getpixel((i, j))
				if r == 255 and g == 255 and b == 255:
					point_white = point_white + 1
					point_all = point_all + 1
				elif r == 0 and g == 0 and b == 0:
					point_black = point_black + 1
					point_all = point_all + 1
				else:
					point_all = point_all + 1
		if point_black / point_all > 0.4:  # BLACK
			print("BLACK POINT,count = " + str(count))
			if count == 7:
				if line_count == 6:
					print(out)
					progress = progress + 1
					line_count = 0
					#save
					filename = r"D:\python_projects\badapple_on_CCaption\text_output\\" + a + ".txt"
					with open(filename,"wt",encoding="UTF-8") as file_object:
						file_object.write(out)
					out = ""
				out = out + "\n" + "□"
				line_count = line_count + 1
				count = 0

			else:
				out = out + "□"
				count = count + 1
		else:
			print("WHITE POINT!,count = " + str(count))
			if count == 7:
				if line_count == 6:
					print(out)

					progress = progress + 1
					line_count = 0
					# save
					filename = r"D:\python_projects\badapple_on_CCaption\text_output\\" + a + ".txt"
					with open(filename, "w", encoding="UTF-8") as file_object:
						file_object.write(out)
					out = ""
				line_count = line_count + 1
				out = out + "\n" + "■"
				count = 0
			else:
				out = out + "■"
				count = count + 1

