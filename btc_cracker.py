import bitcoin
import time
import csv
from multiprocessing import Pool
import random
import os

def generate_btc_address_from_private_key(private_key_hex):
    public_key =  bitcoin.privtopub(private_key_hex)
    
    btc_address = bitcoin.pubtoaddr(public_key)
    return btc_address

def generate_btc_address_range(args):
    from_int, to_int = args
    addresses = {}
    for i in range(from_int, to_int + 1):
        private_key_hex = format(i, 'x').zfill(64)
        btc_address = generate_btc_address_from_private_key(private_key_hex)
        addresses[private_key_hex] = btc_address
    return addresses

def read_addresses_from_csv(csv_file):
    addresses_set = set()
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            addresses_set.add(row[0])  # Assuming addresses are in the first column
    return addresses_set

def write_data_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data.items():
            writer.writerow(row)


def work(results):
    # Compare generated addresses with addresses from CSV file
    intersection = csv_addresses_set.intersection(results.values())
       # Print out the intersecting addresses   
    begin_time = time.time()
    intersection_dict = {}
    for address in intersection:
        intersection_dict[address] = [private_key for private_key, btc_address in results.items() if btc_address == address]
    if intersection_dict:

        file_name = random.randint(0, 1000000000)
        file_name = f"data/intersection_{file_name}.csv"

        print("Lucky you! Found some addresses! Writing to file...")
        
        for address, private_keys in intersection_dict.items():
            print(f"Address: {address} Private keys: {private_keys}")

        write_data_to_csv(intersection_dict, file_name)
    
def save_addresses_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data.items():
            writer.writerow(row)

def generate_addresses(from_hex, batches):
    
    from_int = int(from_hex, 16)
    to_int = from_int +  batches 
    to_generate = to_int - from_int 

    print(f"Generating {to_generate} addresses...")

    num_processes = os.cpu_count()
   
    chunk_size = (to_int - from_int + 1) // num_processes
    ranges = [(i, min(i + chunk_size, to_int)) for i in range(from_int, to_int + 1, chunk_size)]

    with Pool(num_processes) as pool:
        results = {}
        for result in pool.map(generate_btc_address_range, ranges):
            results.update(result)
        return results
   
csv_addresses_set = None

def csv_save(data, output_file):
    with open(output_file, 'w') as file:
        file.write(data)

def guess_where_to_look():

    total_addresses = 2 ** 256
    random_start = random.randint(0, total_addresses)
    result_hex = hex(random_start)[2:] 
    hex_start_padded =  result_hex.zfill(64)
    return hex_start_padded
    
            

if __name__ == "__main__":
    
    print("Starting...May the lords be with you! Reading BTC addresses from CSV file...")
    
    from_hex = guess_where_to_look()
    
    batch_size = 100000 # Number of addresses to generate in each batch and search.


    csv_file = 'data/btc_addresses_with_balance.csv'

    csv_addresses_set = read_addresses_from_csv(csv_file)
    
    name = str(batch_size)+'-'+str(int(from_hex, 16))+'.csv'

    try:
        
        while True:
           
            time_start  = time.time()
            results = generate_addresses(from_hex, batch_size)
            work(results)
            time_end = time.time()
            rate = batch_size/(time_end - time_start)
            rate = round(rate, 0)
            print(f"Rate: {rate}/s Time: {time_end - time_start} seconds.")
            last_key = list(results.keys())[-1]
            from_hex = guess_where_to_look()
            csv_save(str(from_hex), "tracker.csv")

    except KeyboardInterrupt:
         print("Found anything? Exiting...")
 






   


    
