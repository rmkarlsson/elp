import argparse
from fetcher.fetcher import get_price_blob

def main():
    parser = argparse.ArgumentParser(description="Process a string argument.")
    parser.add_argument('--price_source', type=str, required=False, default='https://www.vattenfall.se', help='Energy price source')
    parser.add_argument('--start-date', type=str, required=True, help='Start date')
    parser.add_argument('--end-date', type=str, required=True, help='End date')
    
    args = parser.parse_args()
    print(f'Eneregy price source: {args.price_source}')

    resp =  get_price_blob(args.price_source, args.start_date, args.end_date)
    print(resp)

if __name__ == "__main__":
    main()