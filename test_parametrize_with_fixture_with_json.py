import json
from pytest import fixture

my_file_path = "/Users/palaniappanparamasivam/PycharmProjects/pythonProject/SysProject/data.json"

def load_json_data(path):
    with open(path) as my_data:
        data = json.load(my_data)
        return data



data = load_json_data(my_file_path)
print(type(data))
print(data)

@fixture(params=load_json_data(my_file_path))
def my_test_data(request):
    data = request.param
    return data


def test_product(my_test_data):
    print(my_test_data)
    print(f"I am {my_test_data['product_name']} with {my_test_data['product_color']}")





