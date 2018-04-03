import pygal
from die import Die

# Create a D8
die = Die(8)

while True:
    # Make some rolls and store the results in a list.
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # Analyze the results.
    freqs = []
    for value in range(die.smallest, die.num_sides+1):
        freq = results.count(value)
        freqs.append(freq)

    # Visualize the results.
    hist = pygal.Bar()

    hist.title = "Results of rolling one die."
    hist.x_labels = ['1','2','3','4','5','6','7','8']
    hist.x_title = "Results"
    hist.y_title = "Frequency of Result for 1000 rolls of an 8-sided die"

    hist.add('D8', freqs)
    hist.render_to_file('die_visual.svg')

    print(hist.y_title)
    print(hist.x_labels)
    print(freqs)

    # Set shutdown flag, default: off.
    run_again = input("Would you like to run another set? (y/n): ")
    if run_again == 'n':
        break
