import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# https://cloudinary.com/documentation/resizing_and_cropping#control_gravity

if os.path.exists("env.py"):
    import env


cloudinary.config(
  cloud_name=os.environ.get("cloud_name"),
  api_key=os.environ.get("api_key"),
  api_secret=os.environ.get("api_secret")
)


def upload_image(url):
    """
    Take full source url as a string
    Upload and transforms image to a size of 250x250
    pad image if aspect ratio is differ from square
    return full url for transformed media file
    """
    cdn = cloudinary.uploader.upload(url, 
                                     folder="fitness_master",
                                     width=250,
                                     height=250,
                                     crop="fill_pad",  # scale / fill / fill_pad
                                     gravity="auto",  # "liquid"/auto
                                     use_filename=True
                                    )
    return cdn["secure_url"]
