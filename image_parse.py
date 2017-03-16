from PIL import Image
import os
import glob
import json

results = []
names = []
key = {}

image_list=[]
for file in glob.glob('images/*.png'):
	names.append(os.path.basename(file)[:-4])
	im = Image.open(file)
	image_list.append(im)

xCoord = 1730
yCoord = [867,733,597,460,322,188]

def rgbToHex(rgbList):       
      return "#"+"".join(hex(x)[2:] for x in rgbList)

for img in image_list:
	resultList = []
	RGB = [0,0,0]
	for i in range(6):
		rgb_im = img.convert('RGB')
		RGB = rgb_im.getpixel((xCoord, yCoord[i]))
		resultList.append(rgbToHex(RGB))
	results.append(resultList)

for i in range(len(names)):
	key[names[i]] = results[i] 

print(key['Five Pairs'])
#special cases, discrete transitions occuring at capture points (colors are partitioned into multiples of 5)

fc= ("Five Colors",[[1,228,26,28],[2,228,26,28],[2,55,126,184],[3,55,126,184],[3,77,175,74],[4,77,175,74],[4,152,78,163],[5,152,78,163],[5,255,127,0],[6,255,127,0]],"Set1 / Cynthia Brewer / colorbrewer2.org")
fp = ("Five Pairs",[[1,166,206,227],[2,166,206,227],[2,31,120,180],[3,31,120,180],[3,178,223,138],[4,178,223,138],[4,51,160,44],[5,51,160,44],[5,251,154,153],[6,251,154,153],[6,227,26,28],[7,227,26,28],[7,253,191,111],[8,253,191,111],[8,255,127,0],[9,255,127,0],[9,202,178,214],[10,202,178,214],[10,106,61,154],[11,106,61,154]],"Paired / Cynthia Brewer / colorbrewer2.org")
fs = ("Five Scales",[[1,166,206,227],[3,31,120,180],[3,178,223,138],[5,51,160,44],[5,251,154,153],[7,227,26,28],[7,253,191,111],[9,255,127,0],[9,202,178,214],[11,106,61,154]],"Paired / Cynthia Brewer / colorbrewer2.org")

def customParse(pal, start, length):
	resultList = []
	resultList.append(rgbToHex(pal[1][0][1:]))
	for i in range(start,len(pal[1])-1,length):
		resultList.append(rgbToHex(pal[1][i][1:]))
	resultList.append(rgbToHex(pal[1][-1][1:]))
	return resultList

key[fc[0]]=customParse(fc,1,2)
key[fp[0]]=customParse(fp,3,4)
key[fs[0]]=customParse(fs,2,2) 
print(key['Five Pairs'])

out = open("results.txt","w")
out.write(json.dumps(key))
out.close()