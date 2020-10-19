import argparse


def arg_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        help='Path to work folder',
                        metavar='FOLDER_PATH',
                        type=str,
                        default='/home/rtdge/Documents/vscode/TESTFOLDER')

    parser.add_argument('config',
                        help='Path to *.json config file',
                        metavar='CONFIG_PATH',
                        type=str,
                        default='screpr_config.json')

    parser.add_argument('-s',
                        metavar='Safe mode, copying files',
                        help=argparse.SUPPRESS,
                        action='append',
                        nargs='?',
                        dest='mode',
                        const='safe',
                        required=False)

    parser.add_argument('-l',
                        metavar='[Log execution]',
                        help=argparse.SUPPRESS,
                        action='append',
                        dest='log',
                        nargs='?',
                        const=True,
                        required=False)

    return parser.parse_args()
