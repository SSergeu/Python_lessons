import re

def open_guide_dict(path):
    file = open(path,'r+',encoding='UTF-8')
    data = file.readlines()
    file.close()
    return data

def add(path, new_data):
    file = open(path,'r+',encoding='UTF-8')
    data = file.readlines()
    file.write('\n')  
    file.write(new_data)
    file.close()

