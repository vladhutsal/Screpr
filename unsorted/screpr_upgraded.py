#!/usr/bin/python3
import os

pictures = ['jpg', 'jpeg']
music = ['mp3', 'acc']


def super_asker(status):
    if status == 'start':
        answer = input('What you want to do?:\n'
                       '(A)dd new formats\n'
                       '(S)ort my files\n')
        if answer == 'A':
            super_adder()
        elif answer == 'S':
            pass
        else:
            print('Wrong answer')
            super_asker('start')
    elif status == 'add':
        print('You already have:')


def super_adder():
    super_asker('add')


def copy_paster(list_of_paths, dictionary):
    copy_paste_counter = 0
    for format_type in dictionary.keys():  # type - 'pictures', 'music', 'documents'
        for file_path in list_of_paths:
            file_format = file_path.split('.')[-1]
            if file_format in dictionary[format_type][1:]:
                destination = dictionary[format_type][0] + file_path.split('/')[-1]
                os.rename(file_path, destination)
                copy_paste_counter += 1

    if copy_paste_counter > 0:
        print('All done.')
    else:
        print('There are nothing in there.')


def folder_runer(search_folder_path):
    files_to_move_list = []
    os.chdir(search_folder_path)
    for path, folders, files in os.walk(os.getcwd()):
        for file in files:
            files_to_move_list.append(path + '/' + file)
    return files_to_move_list


def txt_builder(status):
    if status is False:
        while True:
            searched_folder_path = input('Type folder path to sort (start/end with "/"): ')
            if searched_folder_path[-1] and searched_folder_path[0] == '/':
                break
            else:
                print('Use "/" at the end of your path!')
        username = input('Type your PC username: ')

        document = open('screpr_ways.txt', 'w+')
        document.write(f'{searched_folder_path}\n' +
                       f'/home/{username}/Pictures/\n' +
                       f'/home/{username}/Music/'
                       )
        document.close()
        print('screpr_ways.txt was created!')

    if status is True:
        kek = input('You already have doc with paths. Want to create newone? (Y/N): ')
        if kek == 'Y':
            txt_builder(False)
        elif kek == 'N':
            pass
        else:
            print('Wrong answer, kek')
            txt_builder(True)


def opener():
    try:
        document = open('screpr_ways.txt', 'r')
        txt_builder(True)
    except FileNotFoundError:
        txt_builder(False)
        document = open('screpr_ways.txt', 'r')
    return document


def main():
    super_asker('start')
    splited_doc = opener().read().split('\n')

    searched_folder_path = splited_doc[0]
    pictures_folder = splited_doc[1]
    music_folder = splited_doc[2]

    formats = {
        'Pictures': [pictures_folder, 'jpg', 'jpeg', 'png'],
        'Music': [music_folder, 'mp3', 'acc']
    }

    list_of_file_paths = folder_runer(searched_folder_path)
    copy_paster(list_of_file_paths, formats)


if __name__ == '__main__':
    main()
