from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Your actual credentials
YOUTUBE_API_KEY = "AIzaSyBo3xxAjitrnOOzN6GI8uBvEs_nTwL6lbs"
CHANNEL_ID = "UCHZ5ShzneP6hEVYc9CKe2Jg"

@app.route('/check-live')
def check_live():
    url = (
        f"https://www.googleapis.com/youtube/v3/search?"
        f"part=snippet&channelId={CHANNEL_ID}&type=video&eventType=live&key={YOUTUBE_API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()
        is_live = len(data.get("items", [])) > 0
        return jsonify(is_live)
    except Exception as e:
        print("Error checking live status:", e)
        return jsonify(False)

if __name__ == '__main__':
    app.run(debug=True)