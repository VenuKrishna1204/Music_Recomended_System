from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


with app.app_context():
    db.create_all()

    if not User.query.first():
        user1 = User(username="venu", password="123")
        user2 = User(username="vidya", password="123")
        db.session.add_all([user1, user2])
        db.session.commit()


SPOTIFY_CLIENT_ID = "3f77d1e5abc646468005e90a6df0776d"
SPOTIFY_CLIENT_SECRET = "dd833d2e654a4d93a3b96b100011c39c"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('recommend'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if 'username' not in session:
        return redirect(url_for('login'))

    moods = ['Happy', 'Sad', 'Romantic', 'Energetic', 'Relaxing']
    languages = ['Telugu', 'Kannada', 'Hindi']

    artist_db = {
        'Telugu': [
        'Sid Sriram', 'Anurag Kulkarni', 'Geetha Madhuri', 'Karthik', 'Chinmayi',
        'Devi Sri Prasad', 'Thaman', 'Mangli', 'SP Balasubrahmanyam', 'Kaala Bhairava',
        'Hemachandra', 'Shankar Mahadevan', 'Sunitha Upadrashta'
        ],
     'Kannada': [
        'Vijay Prakash', 'Sonu Nigam', 'Armaan Malik', 'Shreya Ghoshal', 'Rajesh Krishnan',
        'Chandan Shetty', 'Sanjith Hegde', 'Anuradha Bhat', 'Karthik', 'Hariharan'
        ],
        'Hindi': [
        'Arijit Singh', 'Shreya Ghoshal', 'Neha Kakkar', 'Sonu Nigam', 'A.R.Rahman',
        'Jubin Nautiyal', 'Armaan Malik', 'Sunidhi Chauhan', 'Atif Aslam', 'KK',
        'Badshah', 'Yo Yo Honey Singh', 'Udit Narayan', 'Alka Yagnik', 'Lata Mangeshkar'
    ]
    }


    songs = []
    if request.method == 'POST':
        selected_mood = request.form['mood']
        selected_language = request.form['language']
        selected_artist = request.form['artist']
        query = f"{selected_mood} {selected_language} {selected_artist}"

        results = sp.search(q=query, type='track', limit=5, market="IN")
        songs = [
            {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'url': track['preview_url'],
                'external': track['external_urls']['spotify']
            }
            for track in results['tracks']['items']
        ]
        return render_template('player.html', songs=songs, mood=selected_mood, language=selected_language, artist=selected_artist)

    return render_template('recommend.html', moods=moods, languages=languages, artist_db=artist_db)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
