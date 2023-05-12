# NOT USED

import json, os

class TokenManager:
    @staticmethod   
    def save_token(token, remember_me=False):
        if remember_me:
            with open('token.json', 'w') as f:
                json.dump(token, f)
        else:
            try:
                os.remove('token.json')
            except FileNotFoundError:
                pass

    @staticmethod
    def get_token():
        try:
            with open('token.json', 'r') as f:
                token = json.load(f)
        except FileNotFoundError:
            token = None
        return token