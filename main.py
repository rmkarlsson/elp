import argparse
from fetcher.fetcher import get_price_blob
import configparser
from price_parser.price_parser import read_json_string, get_day_avergare
import logging

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
        debug_level = config['Logging']['log_level']

    except KeyError as e:
        print(f"Unable to read all needed attributes from config file {args.config_file} missing key {e}")
        return
    
    if debug_level.upper() == 'DEBUG':
        log_level = logging.DEBUG
    elif debug_level.upper() == 'INFO':
        log_level = logging.INFO
    elif debug_level.upper() == 'WARNING':
        log_level = logging.WARNING
    elif debug_level.upper() == 'ERROR':
        log_level = logging.ERROR
    elif debug_level.upper() == 'CRITICAL':
        log_level = logging.CRITICAL
    else:
        print(f"Invalid log level: {debug_level}")
        return
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)

    print(f'Energy price source: {price_source}')

    resp =  get_price_blob(price_source, start_time, end_time, 
                           price_zone)

    avg = get_day_avergare(resp)
    print(f'Average price: {avg}')

if __name__ == "__main__":
    main()