import pandas as pd
import numpy as np
import plotly.express as px

from roulette_board import import_board
board, payouts = import_board()

from play_roulette import play_roulette

from print_statistics import print_statistics


roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':12, '-1, 0': 2},
        1:{'1-12':24, '-1, 0': 4},
        2:{'1-12':36, '-1, 0': 6},
        3:{'1-12':48, '-1, 0': 8}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)


roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':24, '-1, 0':4},
        1:{'1-12':18, '-1, 0':3},
        2:{'1-12':36, '-1, 0':6},
        2:{'1-12':48, '-1, 0':8}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)

roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-3':1,  '4-6':1,  '7-9':1,  '10-12':1,  '13-15':1},
        1:{'1-3':4,  '4-6':4,  '7-9':4,  '10-12':4,  '13-15':4},
        2:{'1-3':8,  '4-6':8,  '7-9':8,  '10-12':8,  '13-15':8},
        3:{'1-3':12, '4-6':12, '7-9':12, '10-12':12, '13-15':12}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)

roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-3':1,  '4-6':1,  '7-9':1,  '10-12':1,  '13-15':1},
        1:{'1-3':6,  '4-6':6,  '7-9':6,  '10-12':6,  '13-15':6},
        2:{'1-3':12, '4-6':12, '7-9':12, '10-12':12, '13-15':12},
        3:{'1-3':18, '4-6':18, '7-9':18, '10-12':18, '13-15':18}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)

roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-3':1,  '4-6':1,  '7-9':1,  '10-12':1,  '13-15':1},
        1:{'1-3':7,  '4-6':7,  '7-9':7,  '10-12':7,  '13-15':7},
        2:{'1-3':14, '4-6':14, '7-9':14, '10-12':14, '13-15':14},
        3:{'1-3':21, '4-6':21, '7-9':21, '10-12':21, '13-15':21}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)


roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':5}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)





# Best strategy found
multiple = 4 # Where second round will start
start = 1 # Start should be no more than 1/8th of multiple
roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-3':start,      '4-6':start,  
           '7-9':start,      '10-12':start,      '13-15':start},
        1:{'1-3':multiple,   '4-6':multiple,  
           '7-9':multiple,   '10-12':multiple,   '13-15':multiple},
        2:{'1-3':multiple*2, '4-6':multiple*2, 
           '7-9':multiple*2, '10-12':multiple*2, '13-15':multiple*2},
        3:{'1-3':multiple*3, '4-6':multiple*3, 
           '7-9':multiple*3, '10-12':multiple*3, '13-15':multiple*3}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)


# crazy eights
roulette, bet_totals = play_roulette(
    bets = {
        0:{'1, 2, 4, 5':1, '7, 8, 10, 11':1, '13, 14, 16, 17':1},
        1:{'1, 2, 4, 5':2, '7, 8, 10, 11':2, '13, 14, 16, 17':2, '19, 20, 22, 23':2},
        2:{'1, 2, 4, 5':4, '7, 8, 10, 11':4, '13, 14, 16, 17':4, '19, 20, 22, 23':4, '25, 26, 28, 29':4},
        3:{'1, 2, 4, 5':10, '7, 8, 10, 11':10, '13, 14, 16, 17':10, '19, 20, 22, 23':10, '25, 26, 28, 29':10},
        3:{'1, 2, 4, 5':20, '7, 8, 10, 11':20, '13, 14, 16, 17':20, '19, 20, 22, 23':20, '25, 26, 28, 29':20}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)


roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':12, '-1, 0':2, '1, 2, 4, 5':1, '2, 3, 5, 6':1},
        1:{'1-12':12, '-1, 0':2, '1, 2, 4, 5':1, '2, 3, 5, 6':1},
        2:{'1-12':24, '-1, 0':4, '1, 2, 4, 5':2, '2, 3, 5, 6':2},
        3:{'1-12':48, '-1, 0':8, '1, 2, 4, 5':4, '2, 3, 5, 6':4},
        4:{'1-12':60, '-1, 0':10, '1, 2, 4, 5':6, '2, 3, 5, 6':6}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)

roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':36, '-1, 0':6},
        1:{'1-12':12, '-1, 0':2},
#         2:{'1-12':48, '-1, 0':8},
#         3:{'1-12':24, '-1, 0':4},
#         4:{'1-12':60, '-1, 0':10}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)


roulette, bet_totals = play_roulette(
    bets = {
        0:{'17':1,
           '13, 14, 16, 17':1, '14, 15, 17, 18':1, '16, 17, 19, 20':1, '17, 18, 20, 21':1,
           '14, 17':1, '16, 17':1, '17, 18':1, '17, 20':1},
        1:{'17':4,
           '13, 14, 16, 17':4, '14, 15, 17, 18':4, '16, 17, 19, 20':4, '17, 18, 20, 21':4,
           '14, 17':4, '16, 17':4, '17, 18':4, '17, 20':4},
        2:{'17':8,
           '13, 14, 16, 17':8, '14, 15, 17, 18':8, '16, 17, 19, 20':8, '17, 18, 20, 21':8,
           '14, 17':8, '16, 17':8, '17, 18':8, '17, 20':8},
        3:{'17':12,
           '13, 14, 16, 17':12, '14, 15, 17, 18':12, '16, 17, 19, 20':12, '17, 18, 20, 21':12,
           '14, 17':12, '16, 17':12, '17, 18':12, '17, 20':12}
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings)

roulette, bet_totals = play_roulette(
    bets = {
        0:{'1-12':12, '-1, 0':2},
        1:{'1-12':12, '-1, 0':2},
        2:{'1-12':24, '-1, 0':4},
        3:{'1-12':48, '-1, 0':8},
        4:{'1-12':48, '-1, 0':8},
    },
    board = board,
    payouts = payouts,
    nspins = 50000
)
cycle_winnings = print_statistics(roulette)
px.histogram(cycle_winnings, nbins = 50)
