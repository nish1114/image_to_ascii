import PIL.Image

ASCII_CHARACTERS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def change_image_size(image,new_width=100):
	width,height=image.size
	hw_ratio=height/width
	new_height=int(new_width*hw_ratio)
	changed_image_size=image.resize((new_width,new_height))
	return(changed_image_size)

def turn_image_to_grey(image):
	grayscale_image=image.convert("L")
	return(grayscale_image)

def conversion_of_pixels_to_ascii(image):
	pixels=image.getdata()
	characters = "".join([ASCII_CHARACTERS[pixel//25] for pixel in pixels])
	return(characters)



def main(new_width=100):
	path=input("Enter the path for the image:\n")
	try:
		image=PIL.Image.open(path)
	except:
		print(path,"is not a valid pathname")

	data_new_image=conversion_of_pixels_to_ascii(turn_image_to_grey(change_image_size(image)))

	ascii_image="\n".join(data_new_image[i:(i+new_width)] for i in range(0,len(data_new_image),new_width))

	print(ascii_image)

	with open("ascii_image_file.txt","w") as f:
		f.write(ascii_image)
main()