#!/usr/bin/python3
import os

formats = ['pictures', 'music']

pictures = ['jpg', 'jpeg']
music = ['mp3', 'acc']

def folder_runer(search_folder_path):
    files_to_move_dictionary = {
        'music': [],
        'pictures': []
    }
    def pathmaker(type):  # adding path of file to dictionary
        file_path = path + '/' + file
        files_to_move_dictionary[f'{type}'].append(file_path)
    os.chdir(search_folder_path)
    for path, folders, files in os.walk(os.getcwd()):
        for file in files:
            file_format = file.split('.')[-1]
            if file_format in pictures:
                pathmaker('pictures')
            elif file_format in music:
                pathmaker('music')
    return files_to_move_dictionary

def copy_paster(file_path, destination):
    os.rename(file_path, destination)


def super_asker():
    while True:
        search_folder_path = input('Type folder path to sort (start/end with "/"): ')
        if search_folder_path[-1] and search_folder_path[0] == '/':
            break
        else:
            print('Use "/" at the end of your path!')
    username = input('Type your PC username: ')
    return [search_folder_path, username]

def txt_creator(path, username):
    document = open('screpr_ways.txt', 'w+')
    document.write(f'{path}\n' + f'/home/{username}/Pictures/\n' + f'/home/{username}/Music/')
    document.close()
    print('Txt was created!')

def run():
    try:
        document = open('screpr_ways.txt', 'r')
    except FileNotFoundError:
        path, username = super_asker()
        txt_creator(path, username)
        document = open('screpr_ways.txt', 'r')
    splited_doc = document.read().split('\n')

    search_folder_path = splited_doc[0]
    pictures_folder = splited_doc[1]
    music_folder = splited_doc[2]

    dictionary_of_file_pathes = folder_runer(search_folder_path)
    for format in formats:
        for file_path in dictionary_of_file_pathes[format]:
            if format == 'pictures':
                destination = pictures_folder + file_path.split('/')[-1]
                copy_paster(file_path, destination)
            if format == 'music':
                destination = music_folder + file_path.split('/')[-1]
                copy_paster(file_path, destination)




if __name__ == '__main__':
    run()
