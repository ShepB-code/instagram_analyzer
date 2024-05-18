import json

def parse_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def analyze_follows(followers_data, following_data):
    followers = set(follower['string_list_data'][0]['value'] for follower in followers_data)
    followings = set(following['string_list_data'][0]['value'] for following in following_data['relationships_following'])

    not_following_back = followings - followers
    return not_following_back



from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        followers_file = request.files['followers_file']
        following_file = request.files['following_file']

        followers_data = json.load(followers_file)
        following_data = json.load(following_file)

        result = analyze_follows(followers_data, following_data)
        return jsonify(list(result))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)