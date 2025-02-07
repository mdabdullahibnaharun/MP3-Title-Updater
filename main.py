from mutagen.id3 import ID3, TIT2
import os

def update_title_to_filename(mp3_path):
    try:
        # Load the MP3 file
        audio = ID3(mp3_path)
        
        # Extract the filename without extension
        filename = os.path.splitext(os.path.basename(mp3_path))[0]
        
        # Update the title tag
        if TIT2 in audio:
            audio[TIT2].text = filename
        else:
            audio.add(TIT2(encoding=3, text=filename))
        
        # Save the changes
        audio.save()
        print(f"Title of '{mp3_path}' has been updated to '{filename}'")
    
    except Exception as e:
        print(f"An error occurred with '{mp3_path}': {e}")

def update_titles_for_all_mp3_files(directory_path):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.mp3'):
            full_path = os.path.join(directory_path, filename)
            update_title_to_filename(full_path)

# Get the current directory
current_directory = os.getcwd()

# Update titles of all MP3 files in the current directory
update_titles_for_all_mp3_files(current_directory)
