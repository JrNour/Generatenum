import hashlib

def passphrase_to_private_key(passphrase):
    # Convert the passphrase to a SHA-256 hash
    sha256_hash = hashlib.sha256(passphrase.encode('utf-8')).hexdigest()
    return sha256_hash

def process_passphrases(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                passphrase = line.strip()  # Remove any leading/trailing whitespace
                if passphrase:  # Ensure the line is not empty
                    private_key = passphrase_to_private_key(passphrase)
                    outfile.write(f"{private_key}\n")
        print(f"Processed passphrases from {input_file} and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Specify the input and output file paths
input_file_path = '60to100mil.txt'
output_file_path = 'yahoo_hex.txt'

# Process the passphrases
process_passphrases(input_file_path, output_file_path)
