from imgurpython import ImgurClient


class ImgurPost(object):
    def __init__(self):
        self.client = None

    def upload_post(self, name, title, description, image_path):
        if self.client is None:
            print("Please authenticate with your imgur credentials")
            return

        config = {
            'album': None,
            'name':  name,
            'title': title,
            'description': description
        }

        print("Uploading image... ")
        image = self.client.upload_from_path(image_path, config=config, anon=False)
        print(f"{image['link']} uploaded")


        return image

    def auth_client(self, client_id, client_secret, access_token, refresh_token):
        self.client = ImgurClient(client_id, client_secret, access_token, refresh_token)
