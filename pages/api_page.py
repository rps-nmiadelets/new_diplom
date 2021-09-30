import requests
import json
from time import sleep


class Api:

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.id = 202221113
        self.pet_name = "NAME890"
        self.pet_name_new = "Minna"

    def add_new_pet(self):
        add_pet_url = self.base_url + "/pet"
        # data_add_pet = {"id": self.id, "name": self.pet_name, "status": "available"}
        data_add_pet = {"id": self.id,
                        "category": {"id": 0, "name": "string"},
                        "name": self.pet_name,
                        "photoUrls": ["string"],
                        "tags": [{"id": 0, "name": "string"}],
                        "status": "available"}
        headers_add_pet = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.post(add_pet_url, headers=headers_add_pet, data=json.dumps(data_add_pet))
        status_code = response.status_code
        assert status_code == 200, f'{status_code} invalid status code'

    def check_added_pet(self):
        check_pet_url = self.base_url + "/pet/" + str(self.id)
        headers_check_added_pet = {'accept': 'application/json'}
        response = requests.get(check_pet_url, headers=headers_check_added_pet)
        json_response = response.json()
        json_response = json_response['id']
        assert json_response == self.id, f'{json_response} not found'

    def update_pet_name(self):
        update_pet_name_url = self.base_url + "/pet"
        new_data_for_pet = {"id": self.id,
                            "category": {"id": 0, "name": "string"},
                            "name": self.pet_name_new,
                            "photoUrls": ["string"],
                            "tags": [{"id": 0, "name": "string"}],
                            "status": "available"}
        headers_update_pet_name = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.put(update_pet_name_url, headers=headers_update_pet_name, data=json.dumps(new_data_for_pet))
        # update_pet_name_url = self.base_url + "/pet/" + str(self.id)
        # new_data_for_pet = 'name=' + self.pet_name_new + '&status=available'
        # headers_update_pet_name = {'accept': 'application/json',
        #                            'content-type': 'application/x-www-form-urlencoded'
        #                            }
        # response = requests.post(update_pet_name_url,  headers=headers_update_pet_name, data=new_data_for_pet)
        status_code = response.status_code
        assert status_code == 200, f'{status_code} invalid status code'

    def check_updated_name(self):
        check_updated_name = self.base_url + "/pet/" + str(self.id)
        headers_check_updated_name = {'accept': 'application/json'}
        response = requests.get(check_updated_name, headers=headers_check_updated_name)
        json_response = response.json()
        json_response = json_response['name']
        assert json_response == self.pet_name_new, f'{json_response} not eq {self.pet_name_new}'

    # def delete_pet(self):
    #     delete_pet_url = self.base_url + "/pet/" + str(self.id)
    #     headers_delete_pet = {'accept': 'application/json', 'api_key': 'special-key'}
    #     response = requests.delete(delete_pet_url, headers=headers_delete_pet)
    #     status_code = response.status_code
    #     if status_code == 404:
    #         pass
    #     else:
    #         assert status_code == 200, f'{status_code} invalid status code'


