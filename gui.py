from tkinter import *
from tkinter import ttk
import bps

player_wins = 0
comp_wins = 0


class Window:
    def __init__(self, window):
        self.master = window
        self.game_frame = Frame(window)
        self.player_frame = Frame(self.game_frame, bg='grey')
        self.choice = StringVar()
        self.player_winner = StringVar()
        self.total_player_wins = Label(self.player_frame, textvariable=self.player_winner)
        self.player_label = Label(self.player_frame, text='Your Choice')
        self.player_winner.set('Player wins: 0')
        self.player_label.pack(side=TOP)
        self.total_player_wins.pack(side=BOTTOM)

        self.button_frame = Frame(self.game_frame, bg='grey')
        self.boulder = Button(self.button_frame, text="Boulder", command=self.boulder_choice)
        self.parchment = Button(self.button_frame, text='Parchment', command=self.parchment_choice)
        self.shears = Button(self.button_frame, text='Shears', command=self.shears_choice)
        self.boulder.pack(side=LEFT, padx=5)
        self.parchment.pack(side=LEFT, padx=5)
        self.shears.pack(side=LEFT, padx=5)
        self.player = Entry(self.player_frame, textvariable=self.choice)
        self.player.pack(side=BOTTOM, pady=5)
        self.button_frame.pack(pady=10)
        self.player_frame.pack(pady=20)

        self.bottom = Frame(self.game_frame)
        self.begin = Button(self.bottom, text='Choose', command=self.game_start)
        self.begin.pack(side=LEFT)
        self.bottom.pack(pady=10)

        self.computer_frame = Frame(self.game_frame)
        self.comp_choice = StringVar()
        self.computer_label = Label(self.computer_frame, text='Computer\'s Choice')
        self.computer_entry = ttk.Combobox(self.computer_frame, textvariable=self.comp_choice)
        self.comp_winner = StringVar()
        self.computer_wins = Label(self.computer_frame, textvariable=self.comp_winner)
        self.comp_winner.set('Computer wins: 0')
        self.computer_wins.pack(side=BOTTOM)
        self.computer_label.pack(side=TOP)
        self.computer_entry.pack(side=BOTTOM)
        self.computer_frame.pack(pady=20)

        self.win = Frame(self.game_frame)
        self.winner = StringVar()
        self.win_counter = Label(self.win, textvariable=self.winner)
        self.win.pack()
        self.win.configure(bg='grey')
        self.win_counter.configure(bg='grey')

        # Win Frame
        self.win_frame = Frame(window)
        self.win_frame.configure(bg='grey')
        self.win_main_button = Button(self.win_frame, text='Start Over', command=self.start_over)
        self.win_label = Label(self.win_frame, text='You Win!', font=14)
        self.win_label.pack(pady=75)
        self.win_main_button.pack(pady=50)

        # Loss Frame
        self.loss_frame = Frame(window)
        self.loss_frame.configure(bg='grey')
        self.loss_main_button = Button(self.loss_frame, text='Start Over', command=self.start_over)
        self.loss_label = Label(self.loss_frame, text='You Lose!', font=14)
        self.loss_label.pack(pady=75)
        self.loss_main_button.pack(pady=50)

        # Start Frame
        self.start_frame = Frame(window)
        self.start_frame.configure(bg='grey')
        self.game_label = Label(self.start_frame, text='Boulder, Parchment, Shears', font=14, relief='raised')
        self.start_button = Button(self.start_frame, text='Start', command=self.start)
        self.rule_button = Button(self.start_frame, text='Rules', command=self.rules)
        self.game_label.pack(side=TOP, pady=10)
        self.start_button.pack(side=LEFT, padx=125,  pady=140)
        self.rule_button.pack(side=RIGHT, padx=125, pady=140)

        # Rules Frame
        self.rules_frame = Frame(window)
        self.rules_frame.configure(bg='grey')
        self.main_button = Button(self.rules_frame, text='Main Menu', command=self.start_over)
        self.rules_label = Label(self.rules_frame, text='Type in Boulder, Parchment, or Shears, in the player entry box'
                                                        '\n'
                                                        'the computer will randomly choose one and output it. First one'
                                                        '\n'
                                                        'to three wins, is the winner. Boulder beats Shears, Parchment'
                                                        '\n'
                                                        'beats Boulder, and Shears beats Parchment, if the choice is\n'
                                                        'the same it is a tie.', font=14)
        self.rules_label.pack(pady=50)
        self.main_button.pack(pady=50)

        self.error_message = Label(self.master, text='Please type Boulder, Parchment, or Shears ')
        self.error_message.configure(bg='grey')
        self.start_frame.pack(fill='both')

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
            test = bps.logic(comp, player_choice)
            self.win_counter.pack(side=TOP)
            if test == 6:
                self.winner.set('Computer Wins')
                global comp_wins
                comp_wins += 1
                self.comp_winner.set(f'Computer wins: {comp_wins}')
                if comp_wins >= 3:
                    self.game_frame.forget()
                    self.loss_frame.pack()
            elif test == 5:
                self.winner.set('Player Wins')
                global player_wins
                player_wins += 1
                self.player_winner.set(f'player wins: {player_wins}')
                if player_wins >= 3:
                    self.game_frame.forget()
                    self.win_frame.pack()
            elif test == 4:
                self.winner.set('It is a Tie')

    def start(self):
        self.start_frame.forget()
        self.game_frame.pack(fill='both')
        self.game_frame.configure(bg='grey')

    def rules(self):
        self.start_frame.forget()
        self.rules_frame.pack()

    def start_over(self):
        global player_wins
        global comp_wins
        player_wins = 0
        comp_wins = 0
        self.win_frame.forget()
        self.rules_frame.forget()
        self.loss_frame.forget()
        self.comp_winner.set(f'Computer wins: {comp_wins}')
        self.player_winner.set(f'Player wins: {player_wins}')
        self.choice.set('')
        self.comp_choice.set('')
        self.start_frame.pack()

    def boulder_choice(self):
        self.choice.set('Boulder')

    def parchment_choice(self):
        self.choice.set('Parchment')

    def shears_choice(self):
        self.choice.set('Shears')


# Got this code from https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
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
