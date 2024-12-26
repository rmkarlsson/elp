import argparse
from fetcher.fetcher import get_price_blob
import configparser

def main():
    parser = argparse.ArgumentParser(description="Process a string argument.")
    parser.add_argument('--config-file', type=str, required=False, default='energy-price.ini', help='Energy price calculator configuration file')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    try:
        price_source = config['Source']['api']
        price_zone = config['Zone']['sn']
        start_time = config['Time']['start']
        end_time = config['Time']['end']
    except KeyError as e:
        print(f"Unable to read all needed attributes from config file {args.config_file} missing key {e}")
        return
    
    print(f'Energy price source: {price_source}')

    resp =  get_price_blob(price_source, start_time, end_time, 
                           price_zone)
    print(resp)

if __name__ == "__main__":
    main()