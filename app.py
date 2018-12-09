import time
import pyxhook
import pyautogui


def read_file(file_name='code.txt'):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    return lines


def write_files(lines, file_name='code.txt'):
    file = open(file_name, 'w')
    file.writelines(lines)
    file.close()


def read_line():
    lines = read_file()
    if lines:
        line = lines[0]
        lines.pop(0)
        write_files(lines)
        return line
    return False


def on_key_press(event):
    # Se pressionar <F7>
    if event.Ascii == 196:
        line = read_line()
        if line:
            print(line)
            pyautogui.typewrite(line, interval=0.07)
        else:
            print('Fim do arquivo')
            exit(0)

    # Se pressionar <F8>
    elif event.Ascii == 197:
        exit(0)


hm = pyxhook.HookManager()
hm.KeyDown = on_key_press

hm.HookKeyboard()

hm.start()