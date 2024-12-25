import argparse
from fetcher.fetcher import fetch_json

def main():
    parser = argparse.ArgumentParser(description="Process a string argument.")
    parser.add_argument('--url', type=str, required=True, help='Energy price source')
    
    args = parser.parse_args()
    print(f'Eneregy price source: {args.url}')

    resp = fetch_json(args.url)
    print(resp)

if __name__ == "__main__":
    main()