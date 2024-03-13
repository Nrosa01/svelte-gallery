import os
import json
import PIL.Image

FORMAT = "webp"
EXTENSION = "." + FORMAT

# Iterate all files in the current directory, change png to webp 90% quality compression m -6, rename file to lowercase, replace spaces with underscores, delete png
current_dir = os.getcwd()
list_of_files = os.listdir(current_dir)
list_of_dirs = [f for f in list_of_files if os.path.isdir(os.path.join(current_dir, f))]

for dir in list_of_dirs:
    list_of_files = os.listdir(os.path.join(current_dir, dir))
    list_of_images = [f for f in list_of_files if os.path.isfile(os.path.join(current_dir, dir, f)) and f.endswith(".png")]
    for image in list_of_images:
        im = PIL.Image.open(os.path.join(current_dir, dir, image))
        im.convert("RGB").save(os.path.join(current_dir, dir, image.replace(".png", EXTENSION)), FORMAT, quality=80, method=6)
        os.remove(os.path.join(current_dir, dir, image))
        os.rename(os.path.join(current_dir, dir, image.replace(".png", EXTENSION)), os.path.join(current_dir, dir, image.replace(".png", EXTENSION).lower().replace(" ", "_")))
        im.close()

# For each directory, get the list of all files in that directory
json_file = open(os.path.join(current_dir, "data.json"), "w")
json_array = []
for dir in list_of_dirs:
    # Get the list of all files in the directory
    list_of_files = os.listdir(os.path.join(current_dir, dir))
    # Get the list of all images in the directory
    list_of_images = [f for f in list_of_files if os.path.isfile(os.path.join(current_dir, dir, f)) and f.endswith(EXTENSION)]
    # For each image, create an object and add it to the array
    for image in list_of_images:
        # tags is an array of strings, each string is a tag, we only have one tag, the directory name
        # but if dir name is zorio, pmd or comms, we want to add also the pokemon name as a tag
        tags = [dir.lower()]
        if dir == "zorio" or dir == "pmd" or dir == "comms":
            tags.append("pokemon")

        json_array.append({"src": "gallery\\" + os.path.join(dir, image), "title": image, "tags": tags})

# Write the json array to the json file
json.dump(json_array, json_file)

# Close the json file
json_file.close()

# Exit the program