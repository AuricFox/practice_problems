# Decode a txt file

def decode(file) -> str:
    words = {}              # Init dict where numbers are keys and words are values

    with open(file) as f:   # Opens the txt file
        for line in f:      # Iterate thru each line in the file
            
            # Strip newline characters
            line = line.strip()
            # Split the string at the spaces
            num_word = line.split(' ')
            # Add elements where numbers are keys and words are values
            words[num_word[0]] = num_word[1]

    message = []
    edge_num = 1
    row_num = 1
    # Continue until there are no words on the edge of the pyramid
    while str(edge_num) in words:
        # Add the edge word to the message list
        message.append(words[str(edge_num)])
        # Increment the row count
        row_num += 1
        # Increment the edge number to the next step's edge number
        edge_num += row_num
    
    # Join the words with a space and return the string
    return ' '.join(message)

if __name__ == '__main__':
    print(decode(file='../input/coding_qual_input.txt'))