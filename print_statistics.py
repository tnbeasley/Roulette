def print_statistics(roulette):
    import numpy as np
    
    def as_currency(amount):
        if amount >= 0:
            return '${:,.2f}'.format(amount)
        else:
            return '-${:,.2f}'.format(-amount)
    
    cycle_winnings = roulette\
        .groupby('Cycle')['RoundNet']\
        .sum()

    perc_no_bust = np.mean(cycle_winnings > cycle_winnings.min()) * 100
    perc_bust = np.mean(cycle_winnings == cycle_winnings.min()) * 100
    print("% Winning Cycles: {:.1f}%".format(perc_no_bust))
    print("% Bust Cycles: {:.1f}%".format(perc_bust))
    no_bust_winnings_med = np.median(cycle_winnings[cycle_winnings > cycle_winnings.min()])
    no_bust_winnings_avg = np.mean(cycle_winnings[cycle_winnings > cycle_winnings.min()])
    print("Med. Winnings If No Bust: {}".format(as_currency(no_bust_winnings_med)))
    print("Avg. Winnings If No Bust: {}".format(as_currency(no_bust_winnings_avg)))
    print("Bust Loss: {}\n".format(as_currency(cycle_winnings.min())))

    print("WINNING COMBINATION: {}".format(no_bust_winnings_avg*(perc_no_bust/100) > np.absolute(cycle_winnings.min())*(perc_bust/100)))
    print("Long-Run Med. Winnings If No Bust: {}".format(as_currency(no_bust_winnings_med*(perc_no_bust/100))))
    print("Long-Run Avg. Winnings If No Bust: {}".format(as_currency(no_bust_winnings_avg*(perc_no_bust/100))))
    print("Long-Run Losses If Bust: {}\n".format(as_currency(cycle_winnings.min()*(perc_bust/100))))

    print("Avg. Cycle Winnings: {}".format(as_currency(cycle_winnings.mean())))
    print("Med. Cycle Winnings: {}".format(as_currency(cycle_winnings.median())))
    print("Min. Cycle Winnings: {}".format(as_currency(cycle_winnings.min())))
    print("Max. Cycle Winnings: {}".format(as_currency(cycle_winnings.max())))
    
    return cycle_winnings