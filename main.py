import tkinter as tk
from tkinter import messagebox
import webbrowser

def clear():
    t_text.delete(1.0, tk.END)
    l_result.config(text=team_list_2.get())

def analyze():
    if len(t_text.get(1.0, tk.END)) == 1:
        messagebox.showinfo(title='Error', message='No text was added')
    else:
        full_list = ['76ers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Golden State Warriors', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets', 'Spurs', 'Suns', 'Thunder', 'Timberwolves', 'Trail Blazers', 'Wizards']
        team_count = {}
        for team in full_list:
            result = t_text.get(1.0, tk.END).count(team)
            team_count[team] = result
        team_list.set('\n'.join(f'{team}: {count}' for team, count in team_count.items()))

def link():
    webbrowser.open_new_tab('https://www.krepsinis.net/menedzeris')

def show_help():
    help_window = tk.Toplevel(window)
    help_window.iconbitmap('nba.ico')
    help_window.title('Help')
    help_window.geometry('290x190')
    help_window.resizable(width=False, height=False)
    l_help = tk.Label(help_window, wraplength='250', pady=10, justify=tk.LEFT, text='Program is adapted for krepsinis.net NBA manager. It may not work properly with other NBA managers.\nHow it works? Just add (copy-paste text) NBA teams schedule of a single tour to analyze it. You will get the number of games played per team, which will help to make better player substitutes for the NBA manager.')
    b_exit_help = tk.Button(help_window, text='Exit', command=help_window.destroy)
    l_help.pack(padx=10)
    b_exit_help.pack()

# Main application
window = tk.Tk()
window.iconbitmap('nba.ico')
window.title('NBA manager helper 2022/2023 season')
window.geometry('700x540')
window.resizable(width=False, height=False)

team_list = tk.StringVar()
team_list.set('76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

team_list_2 = tk.StringVar()
team_list_2.set('76ers: \nBucks: \nBulls: \nCavaliers: \nCeltics: \nClippers: \nGolden State Warriors: \nGrizzlies: \nHawks: \nHeat: \nHornets: \nJazz: \nKings: \nKnicks: \nLakers: \nMagic: \nMavericks: \nNets: \nNuggets: \nPacers: \nPelicans: \nPistons: \nRaptors: \nRockets: \nSpurs: \nSuns: \nThunder: \nTimberwolves: \nTrail Blazers: \nWizards: ')

f_main = tk.Frame(window)
l_text = tk.Label(f_main, text='Add tour schedule to analyze', font=14)
t_text = tk.Text(f_main, width=60)
text_scroll = tk.Scrollbar(f_main, command=t_text.yview)
t_text.config(yscrollcommand=text_scroll.set)

f_buttons = tk.Frame(window)
b_link = tk.Button(f_buttons, text='Link to website', command=link)
b_analyze = tk.Button(f_buttons, text='Analyze text', command=analyze)
b_help = tk.Button(f_buttons, text='Help', command=show_help)
b_clean = tk.Button(f_buttons, text='Clear', command=clear)
b_exit = tk.Button(f_buttons, text='Exit', command=window.destroy)

f_teams = tk.Frame(window)
l_info = tk.Label(f_teams, text='Games played on tour', font=14)
l_result = tk.Label(f_teams, width=20, justify=tk.LEFT, textvariable=team_list)

f_main.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)
l_text.pack()
t_text.pack(side=tk.LEFT)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

f_buttons.grid(row=1, column=1, sticky=tk.EW, padx=10)
b_analyze.pack(pady=20)
b_exit.pack(side=tk.RIGHT)
b_help.pack(side=tk.RIGHT, padx=10)
b_link.pack(side=tk.RIGHT)
b_clean.pack(side=tk.RIGHT, padx=10)

f_teams.grid(row=0, column=0, rowspan=2, sticky=tk.NW, padx=10, pady=10)
l_info.pack()
l_result.pack()

window.mainloop()
