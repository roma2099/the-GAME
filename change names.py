# Improting Image class from PIL module
from PIL import Image
import fuctions
type="Goblin"
# Opens a image in RGB mode
files = fuctions.get_files_from_directory(r"C:\Users\Hoo Lee Shet 2.0\PycharmProjects\the-GAME\sprites\Enemies\\"+type)


#adventurer-attack1-00   Size of the image in pixels (size of orginal image)
# (This is not mandatory)


# Setting the points for cropped image


# Cropped image of above dimension
# (It will not change orginal image)

for file in files:
    if "individual" not in file:


        im = Image.open(file)
        width, height = im.size
        print(height)
        print(width)

        name = file[file.index(type)+len(type)+1:file.index(".png")]
        name= name.lower()
        print(file)
        print(name)
        print(type)
        for i in range(0,int(width/height)):
            im1 = im.crop((height*i, 0, height*(i+1), height))
            print(r""+type.lower()+"-" + name + "-" + str(i) + ".png")
            im1.save(type.lower()+"-" + name + "-" +str(i)+".png")


# Shows the image in image viewe