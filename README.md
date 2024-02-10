# BTC Cracker. 

Generate random private keys and compare them with known addresses with balance

This Python script generates Bitcoin (BTC) addresses from private keys and checks them against a CSV file of BTC addresses to find intersections. It utilizes multiprocessing for faster address generation.

## Features

- Generates BTC addresses from random private keys
- Reads known BTC addresses from a CSV file
- Compares generated addresses with addresses from the CSV file
- Writes intersecting addresses and their private keys to a new CSV file
- Utilizes multiprocessing for efficient address generation

## How can this help me?
- If you are lucky and actually find any matching address, import the private keys to any wallet and Congratulations, you have made it. Send me a coffee. 

- Contact me at https://t.me/team0n1s for any help


## Prerequisites

- Python 3.x
- `bitcoin` library (Install using `pip install bitcoin`)

## Usage

Install python 



1. Clone the repository or download the script.
2. Install the required dependencies listed in `requirements.txt`.
3. Download btc addresses here.
    https://drive.google.com/file/d/12yqg42kiOl9KBZP5YhPCI9oda70SUE6E/view?usp=drive_link
4. Run the script using Python:

    ```bash
    python btc_cracker.py
    ```

5. Follow the on-screen instructions.
6. Press `Ctrl + C` to exit the script.


## Note

- Ensure you have a CSV file containing BTC addresses in the specified format.
- Make sure you have proper permissions to write files to the directory.

## Facts

The probability of finding a matching BTC address depends on various factors such as the number of addresses in the CSV file, the range of private keys generated, and the randomness of private key generation. Due to the sheer size of the BTC address space, the likelihood of finding a matching address is generally low, but with enough computational resources and time, it's possible to discover matches.


##  "May the lords be with you! Remember, in the world of cryptocurrencies, fortune favors the bold!"

## Donate

If you find this script useful and it helps you in any way, consider sending a donation to support further development:

- BTC: bc1q3vgh9wjr4qhk84h0dhq624tcsxwlapqd3cmgck

