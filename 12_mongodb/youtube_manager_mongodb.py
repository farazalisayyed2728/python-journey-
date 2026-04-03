# from pymongo import MongoClient
# from bson import ObjectId

# client = MongoClient("mongodb+srv://db_youtubepy:Youtube%2Epy@cluster0.znfzimj.mongodb.net/ytmanager")
# print(client)

# db = client["ytmanager"]
# video_collection = db["videos"]

# # print(video_collection)

# def add_video(name, time):
#     video_collection.insert_one({"name": name , "time": time})

# def list_video():
#     for video in video_collection.find():
#         print(f"ID : {video['_id']} , Name : {video['name']} and Time : {video['time']}")

# def update_video(video_id, new_name, new_time):
#     video_collection.update_one({'_id': video_id},
#                                  {"$set": {"name": new_name, "time": new_time}})
  
# def delete_video(video_id):
#     video_collection.delete_one({"_id": video_id})

# def main():
#     while True:
#         print("\n Youtube manager app")
#         print("\n Youtube manager app with DB")
#         print("1. List videos")
#         print("2. add video")
#         print("3. update video ")
#         print("4. delete  video")
#         print("5. Exit the app")
#         choice = input("enter your choice : ")

#         if choice =='1':
#             list_video()

#         elif choice == '2':
#             name = input("Enter video name : ")
#             time = input("Enter the new video time : ")
#             add_video(name, time)


        
#         elif choice == '3':
#             video_id = input("Enter video ID to update : ")
#             name = input("Enter the new video name : ")
#             time = input("Enter the new video time : ")
#             update_video(video_id,name, time)
    
#         elif choice == '4':
#             video_id = input("Enter video ID to update : ")

#             delete_video(video_id)

#         elif choice == '5':
#             break

#         else:
#             print("Invalid choice")

# if __name__ == "__main__":
#     main()


from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://ytuser:ytpass123@cluster0.znfzimj.mongodb.net/?retryWrites=true&w=majority"
)

# Test connection
try:
    client.admin.command("ping")
    print("✅ MongoDB connected successfully")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("✅ Video added")

def list_video():
    print("\n--- Video List ---")
    for video in video_collection.find():
        print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )
        if result.matched_count:
            print("✅ Video updated")
        else:
            print("❌ Video ID not found")
    except Exception:
        print("❌ Invalid ObjectId format")

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("✅ Video deleted")
        else:
            print("❌ Video ID not found")
    except Exception:
        print("❌ Invalid ObjectId format")

def main():
    while True:
        print("\n📺 Youtube Manager App (MongoDB)")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == '5':
            print("👋 Exiting app")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
