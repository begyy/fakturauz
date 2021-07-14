import requests
import base64


class FAKTURA:
    def __init__(self):
        self.link = 'https://stagingapi.faktura.uz'
        self.username = ''
        self.password = ''
        self.client_id = ''
        self.client_secret = ''
        self.token_key = 'Bearer'

    def auth(self):
        url = 'https://stagingaccount.faktura.uz/token'
        data = {
            'username': self.username,
            'password': self.password,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'password'
        }
        r = requests.post(url, data=data)
        return r.json()['access_token']

    def upload_invoice(self, file_path='agreement.pdf'):
        file = open(file_path, 'rb')
        file_read = file.read()
        file_encode = base64.b64encode(file_read)
        file_encode = file_encode.decode()
        data = {
            'Base64Content': f'{file_encode}',
            'ContractorInn': 'inn',
            'Comment': 'this is comment :))',
            'Title': 'this is title :)',
            'SendToContractor': True,
            'FileName': 'test_pdf'
        }
        url = f'{self.link}/Api/ImportDocument'
        r = requests.post(url, json=data, headers=self.get_headers())
        return r

    def get_headers(self):
        token = self.auth()
        return {'Authorization': f'{self.token_key} {token}'}
