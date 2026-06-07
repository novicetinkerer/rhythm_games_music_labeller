import argparse
import os
import json

from .fetchers import get_fetcher_for_url

SONGS_FOLDER_PATH = 'songs/'
SONGS_BINDER_FILE = 'songs_binder.json'

song_files = []
binder_data = {}
unbinded_songs = []

TEMP_URLS = [
    "https://remywiki.com/Black_Out",
    "https://remywiki.com/Massive_Strength",
    "https://remywiki.com/Plan_8",
    "https://remywiki.com/Help_me,_ERINNNNNN!!",
    "https://remywiki.com/KISKIL-LILLA",
    "https://remywiki.com/ULTRACHARGE",
    "https://remywiki.com/Mermaid_girl",
    "https://remywiki.com/GOLD_RUSH_(Legendary_jubeat_%22GOLDEN_ERA%22_Limited-Epic_Edition)",
    "https://remywiki.com/Good_Vibrations",
]

# Only run this function only after songs have to been added to song_files list
def validate_binders():

    if not os.path.exists(SONGS_BINDER_FILE):
        print(f"Binder file '{SONGS_BINDER_FILE}' does not exist.")
        print("Created the binder file.")
        with open(SONGS_BINDER_FILE, 'w') as f:
            f.write("{}")
    with open(SONGS_BINDER_FILE, 'r') as f:
        binder_data = json.load(f)
    for song_file in song_files:
        if song_file not in binder_data.keys():
            unbinded_songs.append(song_file)

    print(f"{len(unbinded_songs)} unbinded songs found.")

def scan_folder_for_songs():
    if not os.path.exists(SONGS_FOLDER_PATH):
        print(f"Songs folder '{SONGS_FOLDER_PATH}' does not exist.")
        print("Created the folder. Please add song files to it and run the program again.")
        os.makedirs(SONGS_FOLDER_PATH)
        input("Press Enter to exit...")
        return -1
    else:
        for f in os.listdir(SONGS_FOLDER_PATH):
            if os.path.isfile(os.path.join(SONGS_FOLDER_PATH, f)):
                song_files.append(f)
        print(f"Found {len(song_files)} song files in '{SONGS_FOLDER_PATH}'.")
        
        
        return 0
    
def main():    
    while True:

        result = scan_folder_for_songs()
        if result == -1:
            return

        result = validate_binders()
        if result == -1:
            return
        print("##### Menu #####")
        print("1. Bind unbinded songs with their data url.\n",
              "2. Fetch & Attach metadata for all songs in the binder.\n",
              "0. Exit."
              )
        choice = input("Enter your choice: ")

        if choice == '1':
            for song in unbinded_songs:
                song_name = os.path.splitext(song)[0]
                url = input(f"Song name: {song_name}\nEnter the URL for this song: ")
                if url.strip() == "":
                    print("URL cannot be empty. Skipping this song.")
                    continue
                binder_data[song] = url

            with open(SONGS_BINDER_FILE, 'w') as f:
                json.dump(binder_data, f)
        
        elif choice == '0':
            print("Exiting the program.")
            return

    for url in TEMP_URLS:
        fetcher = get_fetcher_for_url(url)
        if fetcher:
            metadata = fetcher(url)
            print(url)
            print(metadata)
            print()
        else:
            print(f'No fetcher found for URL: {url}')


if __name__ == '__main__':
    main()
