import json

def load_data():
    try:
        with open('youtube_videos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        print("Data loading attempt finished.")
        
def save_data_helper(videos):
    with open('youtube_videos.json', 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    # we are using enumerate to get index along with video details
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")
        
def add_video(videos):
    name = input("Enter video title: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    
def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter new video title: ")
        time = input("Enter new video time: ")
        videos[index] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index.")
        
def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data_helper(videos)
    else:
        print("Invalid index.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List all youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting Youtube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()