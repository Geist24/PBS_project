from tkinter import *
import bps


class Window:
    def __init__(self, window):
        self.__comp_wins = 0
        self.__player_wins = 0
        self.master = window
        self.player_frame = Frame(self.master)
        self.choice = StringVar()
        self.computer_wins = Label(self.player_frame, text=f'player wins: {self.__player_wins}')
        self.player_label = Label(self.player_frame, text='Your Choice')
        self.player_label.pack(side=TOP)
        self.player = Entry(self.player_frame, textvariable=self.choice)
        self.player.pack(side=BOTTOM)
        self.player_frame.place(x=75, y=150)

        self.bottom = Frame(self.master)
        self.begin = Button(self.bottom, text='Choose', command=self.game_start)
        self.begin.pack(side=LEFT)
        self.bottom.place(x=275, y=300)

        self.computer_frame = Frame(self.master)
        self.comp_choice = StringVar()
        self.computer_label = Label(self.computer_frame, text='Computer\'s Choice')
        self.computer_entry = Entry(self.computer_frame, textvariable=self.comp_choice)
        self.computer_wins = Label(self.computer_frame, text=f'Computer wins: {self.__comp_wins}')
        self.computer_label.pack(side=TOP)
        self.computer_entry.pack(side=BOTTOM)
        self.computer_frame.place(x=395, y=150)

        self.win = Frame(self.master)
        self.winner = StringVar()
        self.win_counter = Label(self.win, textvariable=self.winner)
        self.win.pack()

        self.error_message = Label(self.master, text='Please type Boulder, Parchment, or Shears ')

    def game_start(self):
        self.error_message.forget()
        self.win_counter.forget()
        try:
            player_choice = self.player.get().strip().lower()
            if player_choice != 'boulder' and player_choice != 'parchment' and player_choice != 'shears':
                raise ValueError
        except ValueError:
            self.error_message.pack()
        else:
            self.comp_choice.set(bps.comp_choice())
            comp = self.computer_entry.get()
            comp = comp.strip().lower()
            test = bps.game(player_choice, comp)
            self.win_counter.pack(side=TOP)
            if test == 6:
                self.winner.set('Computer Wins')
                self.__comp_wins += 1
            elif test == 5:
                self.winner.set('Player Wins')
                self.__player_wins += 1
            elif test == 4:
                self.winner.set('It is a Tie')


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
