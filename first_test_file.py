import requests
import json

from pprint import pprint

def main():
    response = requests.get("https://research.vu.nl/ws/api/59/persons?q=harmelen&apiKey=1aecc9b3-0b58-4e00-b757-c1a8026cbbfd")
    pure = response.json()
    # pprint(pure)
    pprint(pure)

if __name__ == "__main__":
    main()