import requests
import json
from ztpy.zerotier import ZeroTier


class RequestManager:

    @staticmethod
    def do_get_request(resource: str) -> dict:
        header_auth = {'Authorization': 'Bearer ' + ZeroTier.get_token()}
        print(f"https://api.zerotier.com/api/v1/{resource}")
        result = requests.get(f'https://api.zerotier.com/api/v1/{resource}', headers=header_auth)
        result_data = result.text
        print(result_data)
        data = json.loads(result_data) 
        return data

    def do_post_request(resource: str, data: dict ):
        pass
    

