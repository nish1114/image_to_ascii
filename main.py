import PIL.Image

CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def change_image_size(image,new_width=100):
	w,h=image.size
	new_height=int(new_width*(h/w))
	changed_image_size=image.resize((new_width,new_height))
	return(changed_image_size)

def turn_image_to_grey(image):
	gi=image.convert("L")
	return(gi)

def conversion_of_pixels_to_ascii(image):
	pixels=image.getdata()
	chars= "".join([CHARS[pixel//25] for pixel in pixels])
	return(chars)



def main(new_width=100):
	path=input("Enter the path for the image:\n")
	try:
		image=PIL.Image.open(path)
	except:
		print(path,"is not a valid pathname")

	data_new_image=conversion_of_pixels_to_ascii(turn_image_to_grey(change_image_size(image)))

	ascii_image="\n".join(data_new_image[i:(i+new_width)] for i in range(0,len(data_new_image),new_width))

	print(ascii_image)

	with open("image_file.txt","w") as f:
		f.write(ascii_image)
main()