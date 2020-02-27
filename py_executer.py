import PySimpleGUI as gui
import easygui
import signal


def keyboardInterruptHandler():
    exit()


signal.signal(signal.SIGINT, keyboardInterruptHandler)


def easy_gui():
    filepath = easygui.fileopenbox()
    if len(filepath) >= 0:
        return filepath


layout = [[gui.Text('Select file which you want execute')],
           [gui.Button('choose file')],
           [gui.Text('', key='_filepath')]]

root = gui.Window('PY EXECUTER', layout)
gui.ChangeLookAndFeel('Black')
while True:
    event, values = root.read()
    try:
        if event in ('choose file'):
            filepath = easy_gui()
            print(filepath)
#           gui.Print(filepath)
#           root['_filepath'].update(filepath)
            with open(filepath, "r") as f:
                try:
                    exec(f.read())
                except:
                    pass
    except:
        break
root.close()