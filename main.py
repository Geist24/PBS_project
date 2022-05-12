from gui import *


def main():
    master = Tk()
    master.title = 'Boulder, Parchment, Shears'
    master.geometry('600x350')
    master.configure(bg='grey')
    center(master)
    master.resizable(False, False)
    widgets = Window(master)
    master.mainloop()


if __name__ == '__main__':
    main()
