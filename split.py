def split_file(input_file, start_line, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for current_line, line in enumerate(infile, start=1):
                if current_line >= start_line:
                    outfile.write(line)

input_file = '60milto100hex2.txt'
start_line = 13057779
output_file = '60milto100hex3.txt'

split_file(input_file, start_line, output_file)
