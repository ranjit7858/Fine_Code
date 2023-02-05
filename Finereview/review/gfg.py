import os
import difflib
import requests

def compare_file_to_geeksforgeeks(file_path, geeksforgeeks_code):
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
        similarity = difflib.SequenceMatcher(None, file_lines, geeksforgeeks_code).ratio()
        return similarity

def main():
    directory = 'D:/Hacathon/permisson less/finyash/Finereview/review/codes'
    geeksforgeeks_url = 'https://www.geeksforgeeks.org/merge-sort-using-python'
    response = requests.get(geeksforgeeks_url)
    geeksforgeeks_code = response.text.splitlines()

    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            file_path = os.path.join(directory, filename)
            similarity = compare_file_to_geeksforgeeks(file_path, geeksforgeeks_code)
            print(f'{filename}: {similarity:.2%} similarity with Geeks for Geeks code')

if __name__ == '__main__':
    main()