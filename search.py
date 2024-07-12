import os

def search_large_file(small_file_path, large_file_path, output_file_path):
    if not os.path.isfile(small_file_path):
        print(f"Error: {small_file_path} does not exist.")
        return
    if not os.path.isfile(large_file_path):
        print(f"Error: {large_file_path} does not exist.")
        return
    
    print(f"Reading small file: {small_file_path}")
    with open(small_file_path, 'r') as small_file:
        small_lines = set(small_file.read().splitlines())

    matches = []
    line_count = 0
    print(f"Searching in large file: {large_file_path}")
    with open(large_file_path, 'r') as large_file:
        for line in large_file:
            line_count += 1
            if line.strip() in small_lines:
                matches.append(line.strip())
            if line_count % 500000 == 0:
                print(f"Processed {line_count} lines...")
    
    print(f"Writing matches to output file: {output_file_path}")
    with open(output_file_path, 'w') as output_file:
        for match in matches:
            output_file.write(match + '\n')

    print(f"Search completed. Found {len(matches)} matches.")


search_large_file('newww.txt', 'latest1.txt', 'Match.txt')
