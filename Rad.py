import random
import matplotlib.pyplot as plt
import pandas as pd

def throw_dice(n):
    return [(random.randint(1, 6), random.randint(1, 6)) for _ in range(n)]

def count_odd_numbers(numbers):
    return sum(1 for number in numbers if sum(number) % 2 != 0)

def perform_trials(num_trials, num_throws):
    odd_counts = []
    all_sums = []
    all_rolls = []
    for i in range(num_trials):
        rolls = throw_dice(num_throws)
        sums = [sum(roll) for roll in rolls]
        all_rolls.extend(rolls)
        all_sums.extend(sums)
        odd_count = count_odd_numbers(rolls)
        odd_counts.append(odd_count)
        print(f'Trial {i+1}: {rolls}')
        print(f'Sums in trial {i+1}: {sums}')
        print(f'Number of odd sums in trial {i+1}: {odd_count}')
    return odd_counts, all_sums, all_rolls

def draw_graph(data, title, filename):
    plt.hist(data, bins=max(data)-min(data)+1, edgecolor='black')
    plt.title(title)
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.savefig(filename)
    plt.show()

# Perform the experiment with increasing number of trials
for num_trials in [10, 20, 30, 40, 50, 100, 200, 500, 1000]:
    print(f'\nPerforming {num_trials} trials...')
    odd_counts, all_sums, all_rolls = perform_trials(num_trials, 10)
    draw_graph(odd_counts, f'Count of Odd Sums vs Frequency for {num_trials} Trials', f'graph_{num_trials}.png')

    # Save the data to a CSV file
    df = pd.DataFrame({
        'Trial': list(range(1, num_trials + 1)),
        'Odd_Count': odd_counts,
    })
    df.to_csv(f'data_{num_trials}.csv', index=False)
