import json

with open('jurusan.json', 'r') as file:
    data = json.load(file)

cepat_kode_list = [item["cepat_kode"] for item in data]

print(cepat_kode_list)