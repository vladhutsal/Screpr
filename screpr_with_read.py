#!/usr/bin/python3
import os

pictures = ['jpg', 'jpeg']
music = ['mp3', 'acc']


def copy_paster(list_of_paths, dictionary):
    copy_paste_counter = 0
    for type in dictionary.keys():  # type - 'pictures', 'music', 'documents'
        for file_path in list_of_paths:
            file_format = file_path.split('.')[-1]
            if file_format in dictionary[type][1:]:
                destination = dictionary[type][0] + file_path.split('/')[-1]
                os.rename(file_path, destination)
                copy_paste_counter += 1

    if copy_paste_counter > 0:
        print('All done, bitch!')
        copy_paste_counter = 0
    else:
        print('There are nothing in here')


def folder_runer(search_folder_path):
    files_to_move_list = []
    os.chdir(search_folder_path)
    for path, folders, files in os.walk(os.getcwd()):
        for file in files:
            files_to_move_list.append(path + '/' + file)
    return files_to_move_list


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


def main():
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

    formats = {
        'pictures': [pictures_folder, 'jpg', 'jpeg'],
        'music': [music_folder, 'mp3', 'acc']
    }

    list_of_file_paths = folder_runer(search_folder_path)
    copy_paster(list_of_file_paths, formats)

if __name__ == '__main__':
    main()
