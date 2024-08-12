from flask import Flask, jsonify, request

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

video_titles.sort()

def binary_search(titles, target):
    low = 0
    high = len(titles) - 1
    
    while low <= high:
        mid = (low + high) // 2
        title = titles[mid]
        if title == target:
            return mid
        elif title > target:
            high = mid - 1
        else: 
            low = mid + 1
        
    return None  

@app.route('/search_video', methods=["GET"])
def search_video():
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Please provide a video title to search"}), 400
    
    result_index = binary_search(video_titles, title)
    if result_index is not None:
        return jsonify({"message": f"'{title}' found at index {result_index}"}), 200
    else:
        return jsonify({"message": "Film not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
