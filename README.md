## 🎶 **VenuSwar**

VenuSwar is a **music recommendation web application** that uses the **Spotify Web API** to generate personalized playlists based on user mood and genre preferences.

---

## 📌 **Features**

- 🔑 User authentication via Spotify OAuth
- 🎧 Fetch user profile data securely
- 🎶 Generate mood-based or genre-based song recommendations
- 🎵 Create and save playlists dynamically
- 🌐 Responsive web interface

---

## 🛠️ **Tech Stack**

- **Python**
- **Spotipy** (Spotify Web API library)
- **Flask** or **Streamlit** (for web framework)
- **HTML/CSS** (frontend templates)
- **Spotify Developer Dashboard** (for API credentials)

---

## 📁 **Project Structure**

![image](https://github.com/user-attachments/assets/20fb14a8-bf63-4e60-8cd5-3016b83a7acf)


---

## 🚀 **Setup and Execution**

1. **Clone the repository**
2. **Create a Spotify Developer App**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create an app with:
     - App Name: vibewave
     - Redirect URI: `http://localhost:8888/callback` (or your production HTTPS URL)
   - Copy **Client ID** and **Client Secret**
3. **Set environment variables**
   - Create a `.env` file with:
     ```
     SPOTIFY_CLIENT_ID=your_client_id_here
     SPOTIFY_CLIENT_SECRET=your_client_secret_here
     SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
     ```

4. **Create a virtual environment** and activate it

5. **Install dependencies**
   - `pip install -r requirements.txt`

6. **Run the app locally**
   - For Flask: `python app.py`
   - For Streamlit: `streamlit run app.py`

7. **Open in browser**
   - Navigate to `http://localhost:8888` or Streamlit’s provided URL

---

## 🔒 **Security Notes**

- **Never share your Client Secret publicly**
- **Use environment variables** for sensitive credentials

---

## 🌟 **Future Enhancements**

- AI-powered mood detection from text or images
- Integration with YouTube Music or Apple Music
- Enhanced UI with advanced visualizations

---

## 🙌 **Contributing**

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 **License**

This project is licensed under the [MIT License](LICENSE).

---

## 👤 **Author**

**vibewave by [GADDAM VENU]**

---

> Made with ❤️ and 🎶 for Spotify music lovers.

**OUTPUT:**

![1](https://github.com/user-attachments/assets/782429c8-4aa8-463d-b96b-11731ceeddcd)

![2](https://github.com/user-attachments/assets/3bb089b6-931d-4ea9-969c-1c55074428a6)

![3](https://github.com/user-attachments/assets/7e13e262-5b1a-49df-bca7-e70d17ef7bdd)

![4](https://github.com/user-attachments/assets/817cfb02-325e-4719-b13f-deb008863ab4)

Open The Spotify APP

![5](https://github.com/user-attachments/assets/d5ef8530-679f-4443-9e3b-b3484a454f8f)







