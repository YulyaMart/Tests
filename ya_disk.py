import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {'path': 'Test', "overwrite": "true"}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code

if __name__ == '__main__':
    with open('token_ya.txt', 'r') as file:
        token_ya = file.read().strip()
        yandex = YaUploader(token_ya)
        yandex.get_create_folder()
        print(yandex.get_create_folder())