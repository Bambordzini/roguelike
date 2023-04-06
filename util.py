import sys
import os
def get_move(key):
    if key == 'w':
        return (0, -1)
    elif key == 'a':
        return (-1, 0)
    elif key == 's':
        return (0, 1)
    elif key == 'd':
        return (1, 0)
    else:
        return (0, 0)


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
