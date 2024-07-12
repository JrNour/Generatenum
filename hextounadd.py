import hashlib
import ecdsa
import base58
import sys

def sha256(data):
    return hashlib.sha256(data).digest()

def ripemd160(data):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(data)
    return ripemd160.digest()

def private_key_to_public_key(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key_bytes = b'\x04' + vk.to_string()  # Add prefix 0x04 for uncompressed keys
    return public_key_bytes

def public_key_to_address(public_key_bytes):
    # SHA-256 and RIPEMD-160
    sha256_hash = sha256(public_key_bytes)
    ripemd160_hash = ripemd160(sha256_hash)
    
    # Add version byte (0x00 for mainnet)
    versioned_payload = b'\x00' + ripemd160_hash
    
    # Double SHA-256
    checksum = sha256(sha256(versioned_payload))[:4]
    
    # Append checksum
    address_bytes = versioned_payload + checksum
    
    # Convert to Base58
    return base58.b58encode(address_bytes).decode()

def process_private_keys(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        line_count = 0
        progress_interval = 100000
        for line in infile:
            private_key_hex = line.strip()  # Remove any leading/trailing whitespace
            if private_key_hex:  # Ensure the line is not empty
                # Generate public key
                public_key_bytes = private_key_to_public_key(private_key_hex)
                # Generate Bitcoin address
                bitcoin_address = public_key_to_address(public_key_bytes)
                # Write the Bitcoin address to the output file
                outfile.write(f"{bitcoin_address}\n")
                line_count += 1
                # Print progress every 100,000 lines
                if line_count % progress_interval == 0:
                    print(f"Processed {line_count} lines.")
                    # Check memory usage
                    memory_usage = sys.getsizeof(outfile)
                    print(f"Current memory usage: {memory_usage} bytes.")
    print(f"Processed private keys from {input_file} and saved addresses to {output_file}.")

# Specify the input and output file paths
input_file_path = '60milto100hex3.txt'
output_file_path = '60milto100add.txt'

# Process the private keys
process_private_keys(input_file_path, output_file_path)
