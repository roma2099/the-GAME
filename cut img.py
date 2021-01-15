# Improting Image class from PIL module
from PIL import Image
import fuctions

# Opens a image in RGB mode
files = fuctions.get_files_from_directory(r"C:\Users\Hoo Lee Shet 2.0\PycharmProjects\the-GAME\sprites\Martial artist")


#adventurer-attack1-00   Size of the image in pixels (size of orginal image)
# (This is not mandatory)


# Setting the points for cropped image


# Cropped image of above dimension
# (It will not change orginal image)
files=[r"C:\Users\Hoo Lee Shet 2.0\PycharmProjects\the-GAME\sprites\Martial artist\Jump.png"]
for file in files:
    im = Image.open(file)
    width, height = im.size
    print(height)
    print(width)

    name = file[74:file.index(".png")]
    name= name.lower()
    print(file)
    print(name)
    for i in range(0,int(width/height)):
        im1 = im.crop((height*i, 0, height*(i+1), 200))

        im1.save(r"martial-artist-" + name + "-" +str(i)+".png")


# Shows the image in image viewe