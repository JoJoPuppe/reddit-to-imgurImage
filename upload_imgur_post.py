from imgurpython import ImgurClient
import config
from datetime import datetime

image_path = "./Posts/2020-09-05 12:57:41.891746"

def upload_kitten(client):

    config = {
        'album': None,
        'name':  '01',
        'title': 'test',
        'description': 'test {0}'.format(datetime.now())
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image

def auth_client():
    client_id = config.client_id
    client_secret = config.client_secret
    access_token = config.access_token
    refresh_token = config.refresh_token

    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    return client


# If you want to run this as a standalone script
if __name__ == "__main__":
    client = auth_client()
    image = upload_kitten(client)

    print("Image was posted! Go check your images you sexy beast!")
    print("You can find it here: {0}".format(image['link']))
