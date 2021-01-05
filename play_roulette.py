def play_roulette(bets, board, payouts, nspins = 10000):

    import pandas as pd
    import numpy as np
    import random

    from roulette_board import import_board
    board, payouts = import_board()
    
    allowed_losses = len(bets.keys())

    bet_totals = []
    for bet_key in bets.keys():
        cycle = bets[bet_key]
        bet_totals.append(np.sum(np.fromiter(cycle.values(), dtype = float)))
    cum_bet_totals = np.cumsum(bet_totals)
    bet_totals = dict(zip(bets.keys(), bet_totals))
    cum_bet_totals = dict(zip(bets.keys(), cum_bet_totals))

    round_numbers = {}
    for key in bets.keys():
        numbers = []
        round_bets = bets[key]

        for round_bet in round_bets.keys():
            for board_key in board.keys():
                if round_bet in board[board_key].keys():
                    if board_key == 'Straights':
                        numbers.append([board[board_key][round_bet]])
                    else:
                        numbers.append(board[board_key][round_bet])

        round_numbers[key] = np.unique(np.concatenate(numbers))


    spins = [random.choice(list(np.arange(-1,36))) for _ in range(nspins)]

    roulette = pd.DataFrame()
    roulette['WinningNum'] = spins

    dct = {True:'Win', False:'Loss'}
    results = []
    losses = []
    winnings = []

    for i in np.arange(nspins):
        if i == 0:
            loss = 0
            losses.append(loss)  
        else:
            if results[i-1] == 'Win' or loss == allowed_losses-1:
                loss = 0
                losses.append(loss)
            else:
                loss = losses[i-1] + 1
                losses.append(loss)

        winning_num = roulette.WinningNum[i]
        winning_bets = []
        for bet_type in board.keys():
            bet_type_combos = np.array(list(board[bet_type].values()))
            if bet_type == 'Straights':
                winning_combos = winning_num == bet_type_combos
            else:
                winning_combos = [winning_num in bet_type_combo for bet_type_combo in bet_type_combos]

            winning_bets.append(np.array(list(board[bet_type].keys()))[winning_combos])
        winning_bets = np.concatenate(winning_bets)

        our_winners = np.array(list(bets[loss].keys()))[[bet in winning_bets for bet in list(bets[loss].keys())]]
        if len(our_winners) > 0:
            results.append('Win')
            payout = 0
            for winner in our_winners:
                winner_bet = bets[loss][winner]
                winner_type = np.array(list(board.keys()))[[winner in board[key] for key in board.keys()]]
                type_payout = payouts[winner_type[0]]
                payout += winner_bet*type_payout

            winnings.append(payout)
        else:
            results.append('Loss')
            winnings.append(0)

    roulette['Result'] = results
    roulette['Losses'] = losses
    roulette['Winnings'] = winnings
    roulette['RoundBet'] = list(map(bet_totals.get, roulette.Losses))
    roulette['TotalBet'] = list(map(cum_bet_totals.get, roulette.Losses))
    roulette['RoundNet'] = roulette.Winnings - roulette.RoundBet
    roulette['TotalNet'] = roulette.Winnings - roulette.TotalBet

    cycle = 1
    cycles = []
    for i in np.arange(nspins):
        cycles.append('Cycle' + str(cycle))
        if roulette.Result[i] == 'Win' or roulette.Losses[i] == allowed_losses-1: 
            cycle += 1 
    roulette['Cycle'] = cycles  

    return roulette, cum_bet_totals;








# cycle_counts = roulette.Cycle.value_counts()
# px.histogram(cycle_counts)


