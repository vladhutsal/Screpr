import os

def user_asker():
    pass


def txt_creator():
    while True:
        message = 'What folder do you want to sort? (ex: /home/<username>/<folder>/): '
        sort_folder_path = input(message)
        if sort_folder_path[-1] == '/' and sort_folder_path[0] == '/':
            break
        else:
            print('Use "/" at the end of your path!')
    username = input('Type your PC username: ')

    document = open('screpr_ways.txt', 'w+')
    pictures_folder = f'/home/{username}/Pictures/\n'
    music_folder = f'/home/{username}/Music/\n'
    doc_folder = f'/home/{username}/Documents/'

    path = f'{sort_folder_path}\n' + pictures_folder + music_folder + doc_folder
    document.write(path)
    print('Txt was created!')
    return sort_folder_path


def folder_runer(folder_to_sort_path):
    files_to_move_list = []
    os.chdir(folder_to_sort_path)
    for path, folders, files in os.walk(os.getcwd()):
        for one_file in files:
            files_to_move_list.append(path + '/' + one_file)
    return files_to_move_list


def copy_paster():
    pass


def doc_exsist(doc):
    splited_doc = doc.read().split('\n')
    message = f'Your Search folder is: {splited_doc[0]}. Wanna change? [y/n]'
    answer = input(message)
    if answer == 'y':
        txt_creator()
    elif answer == 'n':
        user_folders = ', '.join(splited_doc[1:])        
        print(f'I will sort from {splited_doc[0]} to {user_folders}')
        
    else:
        doc_exsist(doc)
    return splited_doc


if __name__ == '__main__':
    try:
        document = open('screpr_ways.txt', 'r')
        doc_exsist(document)
    except FileNotFoundError:
        sort_folder_path = txt_creator()
    
    user_asker(sort_folder_path)




