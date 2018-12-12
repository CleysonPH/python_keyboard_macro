import pyxhook
import pyautogui


line_count = 0


def read_file(file_name='code.txt'):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    return lines


def read_line():
    global line_count
    lines = read_file()
    if lines:
        line = lines[line_count]
        line_count += 1
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