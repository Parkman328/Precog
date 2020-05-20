import json
import requests
base_url = "http://localhost:55932"
url_dst = "destination"
url_ds = "datasources"
url_tb = "tables"


def test_ds():
    url = base_url+'/'+url_ds
    print(url)
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get(url)
    # Print the status code of the response.
    print("Status Code")
    print(response.status_code)
    print("Header")
    print(response.headers)
    print("Content Type")
    print(response.headers["content-type"])
    data = response.content
    print("Data")
    print(data)
    obj1 = json.loads(data)
    print(type(obj1))
    # print("Data")
    print(obj1)
    print('jrp')
    print(obj1['datasources'])
    print("loop")
    # print(data)
    # print(obj)
    for datasources, items in obj1['datasources'].items():
        print(datasources, items['name'], items['status'])


def test_dst():
    url = base_url+'/'+url_dst
    print(url)
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get(url)


def test_tb():
    url = base_url+'/'+url_tb
    print(url)
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get(url)
    print("Status Code")
    print(response.status_code)
    print("Header")
    print(response.headers)
    print("Content Type")
    print(response.headers["content-type"])
    data = response.content
    print("Data")
    obj1 = json.loads(data)
    print(type(obj1))
    tablename = []
    keyname = []
    for tablesources in obj1.values():
        tablename.append(tablesources.get('name'))
    print(type(tablename))
    print(tablename)
    for tablesources in obj1:
        print(tablesources)
        keyname.append(tablesources)
    print(type(keyname))
    print(keyname)
    newstructure = dict(zip(tablename, keyname))
    print(newstructure)
    print(newstructure.get('FDA Drugs'))
    #
    #     tablesources.get('description').get('table').get('steps'))
    # for tablesources in obj1:
    #   print(tablesources)
    # print(tablesources.fromkeys('name'))
    # func1(obj1)


def func1(data):
    for key, value in data.items():
        print(str(key)+'->'+str(value))
        if type(value) == type(dict()):
            func1(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func1(val)


# test_ds()
# test_dst()
test_tb()
