import glob
from PIL import Image


images=glob.glob('input_images/*.jpg')


cnt=0


for image in images:
	print(cnt)
	fullfileurl  = 'output/'+str(cnt)+'.jpg'

	image = Image.open(image)
	new_image = image.resize((1000, 1500))
	new_image.save(fullfileurl)

	print(image.size) # Output: (1920, 1280)
	print(new_image.size) # Output: (400, 400)

	cnt=cnt+1