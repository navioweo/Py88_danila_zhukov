import json


dictionary = {

    987654: ('danila', 19),
    876543: ('misha', 20),
    776542: ('zhenia', 21),
    654321: ('ilya', 18),
    543210: ('nikita', 22)

}


with open('datafile.json', 'w', newline='') as f:
    json.dump(dictionary, f)
