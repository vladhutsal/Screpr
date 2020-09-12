#!/usr/bin/python3
import os

pictures = ['jpg', 'jpeg', 'png']
music = ['mp3', 'acc']

def asker():
    while True:
        folder_to_sort_path = input('Type folder path to sort (ex: /home/user/..., start/end with "/"): ')
        if folder_to_sort_path[-1] and folder_to_sort_path[0] == '/':
            break
        else:
            print('Use "/" at the end of your path!')
    username = input('Type your PC username: ')
    return [folder_to_sort_path, username]


def txt_creator(path, username):
    document = open('screpr_ways.txt', 'w+')
    pictures_folder_path = f'/home/{username}/Pictures/\n'
    music_folder_path = f'/home/{username}/Music/'
    path = f'{path}\n' + pictures_folder_path + music_folder_path
    document.write(path)
    document.close()
    print('Txt was created!')


def folder_runer(folder_to_sort_path):
    files_to_move_list = []
    os.chdir(folder_to_sort_path)
    for path, folders, files in os.walk(os.getcwd()):
        for one_file in files:
            files_to_move_list.append(path + '/' + one_file)
    return files_to_move_list


def copy_paster(path_list, format_dict):
    copy_paste_counter = 0
    for format_type in format_types:  
        for file_path in path_list:
            file_format = file_path.split('.')[-1]
            if file_format in format_dict[format_type][1:]:
                destination = format_dict[format_type][0] + file_path.split('/')[-1]
                os.rename(file_path, destination)
                copy_paste_counter += 1

    if copy_paste_counter > 0:
        print('All done, bitch!')
        copy_paste_counter = 0
    else:
        print('There are nothing in here')


if __name__ == '__main__':
    try:
        document = open('screpr_ways.txt', 'r')
    except FileNotFoundError:
        path, username = asker()
        txt_creator(path, username)
        document = open('screpr_ways.txt', 'r')
    splited_doc = document.read().split('\n')

    folder_to_sort_path = splited_doc[0]
    pictures_folder = splited_doc[1]
    music_folder = splited_doc[2]

    format_dict = {
        'pictures': [pictures_folder, 'jpg', 'jpeg', 'png'],
        'music': [music_folder, 'mp3', 'acc']
    }
    
    format_types = format_dict.keys() 
    path_list = folder_runer(folder_to_sort_path)
    copy_paster(path_list, format_dict)
