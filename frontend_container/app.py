import os, datetime
import pandas as pd
from flask import Flask, request, jsonify


app = Flask(__name__)
association_rules = None


def recommend_songs(rules, song_list):
    recommendations = set()
    for song in song_list:
        matching_rules = rules[rules['antecedents'].apply(lambda x: all(song in x for song in song_list))]
        for _, row in matching_rules.iterrows():
            recommendations.update(row['consequents'])
    recommendations = list(recommendations - set(song_list))
    return recommendations


@app.route('/api/recommend', methods=['POST'])
def recommendation():
    global association_rules

    if association_rules is None:
        association_rules = pd.read_pickle('/models/model.pkl')

    data = request.json
    liked_songs = data.get('songs')

    recommended_songs = recommend_songs(association_rules, liked_songs)
    
    version = os.getenv("VERSION")
    if version is None:
        version = '0.0.1'

    return jsonify({
        'songs': recommended_songs,
        'version': version,
        'model_date': datetime.datetime.fromtimestamp((os.stat('model.pkl')).st_ctime)
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)