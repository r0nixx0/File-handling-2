# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    # Write your code here
    pass

# Exercise 3
def filter_passed(source, destination, pass_mark):
    # Write your code here
    pass

# Exercise 4
def replace_word(filename, old_word, new_word):
    # Write your code here
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
