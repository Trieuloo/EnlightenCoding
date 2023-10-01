import random
# uses python 3.10
def generate_grid(rows, cols):
    '''Generates the grid with Dimensions filling with random letters'''
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Gets a random choice of 26 letters
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = random.choice(letters)
    return grid

def check_horizontal(grid, word, rows, cols):
    '''Check horizontal right and backwards string'''
    word_len = len(word)
    # gets the rows and columns
    for row in range(rows):
        # Makes sure you don't go above the beyond the boundaries, and read stuff twice
        for col in range(cols - word_len + 1):
            # Gets the row,specifies the range of columns that are inside the row. Starts at col, ends at col + word_len
            if grid[row][col:col + word_len] == list(word):
                # Returns the word, row, column, and when the word ends.
                return f'{word} {row}:{col} {row}:{col + word_len - 1}'
            # Checking everything in reverse
            if grid[row][col:col + word_len] == list(word[::-1]):
                return f'{word}  {row}:{col + word_len - 1} {row}:{col}'
    # returns none if it doesn't return the word
    return None

def check_vertical(grid, word, rows, cols):
    '''Check vertical down and backwards string | check_horizontal for deciphering code'''
    word_len = len(word)
    for col in range(cols):
        for row in range(rows - word_len + 1):
            if [grid[row + i][col] for i in range(word_len)] == list(word):
                return f'{word} {row}:{col} {row + word_len - 1}:{col}'
            if [grid[row + i][col] for i in range(word_len)] == list(word[::-1]):
                return f'{word} {row + word_len - 1}:{col} {row}:{col}'
    return None

def check_diagonal_down_right(grid, word, rows, cols):
    '''Check diagonal down-right and backwards string | check_horizontal for deciphering code'''
    word_len = len(word)
    for row in range(rows - word_len + 1):
        for col in range(cols - word_len + 1):
            if all(grid[row + i][col + i] == word[i] for i in range(word_len)):
                return f'{word} {row}:{col} {row + word_len - 1}:{col + word_len - 1}'
            if all(grid[row + i][col + i] == word[i] for i in range(word_len)):
                return f'{word}  {row + word_len - 1}:{col + word_len - 1} {row}:{col}'
    return None

def check_diagonal_down_left(grid, word, rows, cols):
    '''Check diagonal down-left and backwards string | check_horizontal for deciphering code'''
    word_len = len(word)
    for row in range(rows - word_len + 1):
        for col in range(word_len - 1, cols):
            if all(grid[row + i][col - i] == word[i] for i in range(word_len)):
                return f'{word} {row}:{col} {row + word_len - 1}:{col - word_len + 1}'
            if all(grid[row + i][col - i] == word[i] for i in range(word_len)):
                return f'{word}  {row + word_len - 1}:{col - word_len + 1} {row}:{col}'
    return None

def find_word(grid, word):
    '''Finding the word in all four directions. Also checks the reverse for every single direction'''
    rows, cols = len(grid), len(grid[0])
    # Checks all the results from all directions
    result = check_horizontal(grid, word, rows, cols)
    # if it is not none we get the result value
    if result:
        return result

    result = check_vertical(grid, word, rows, cols)
    if result:
        return result

    result = check_diagonal_down_right(grid, word, rows, cols)
    if result:
        return result

    result = check_diagonal_down_left(grid, word, rows, cols)
    if result:
        return result
    # if it is not found in any of the checks, we just return it is not found
    return f'{word} not found'

# Main function
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    # Makes it so that if you can't find the file it shows an error message
    try:
        # Opens the file, makes sure it is in read-only mode
        with open(file_name, 'r') as file:
            # Read the first line to get the dimensions
            dimensions = file.readline().strip().split('x')
            rows, cols = int(dimensions[0]), int(dimensions[1])

            # Read the grid, removes the empty spaces, splits everything by spaces.
            grid = [list(file.readline().strip().split(' ')) for _ in range(rows)]
            # Read the words to be found
            words = [word.strip() for word in file.readlines()]

        # Prints out the results for however many words we have
        for word in words:
            result = find_word(grid, word)
            print(result)
    # Putting in the except to show an error when it's not properly found
    except FileNotFoundError:
        print("File not found.")
