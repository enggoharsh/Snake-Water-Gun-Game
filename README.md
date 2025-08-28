# 🎮 Snake-Water-Gun Game (Flask)

This is a simple **Snake-Water-Gun game** built with **Flask** and deployed on **Render**.  
Play it online 👉 [Snake-Water-Gun Game](https://snake-water-gun-game-907x.onrender.com)

---

## 🐍 Rules of the Game
- **Snake vs Water → Snake drinks water → Snake wins 🐍**
- **Water vs Gun → Gun drowns in water → Water wins 💧**
- **Gun vs Snake → Gun shoots snake → Gun wins 🔫**

If both choose the same option → It's a **Draw** ⚖️

---

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/snake-water-gun-game.git
   cd snake-water-gun-game
2. Create a virtual environment & activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Flask app:
   ```bash
   python app.py
5. Open Your Browser
   ```bash
   http://127.0.0.1:5000/
## 🌍 Deployment

- **This project is deployed using Render.**
-**Procfile:**
 ```bash
web: gunicorn app:app
📂 Project Structure
├── app.py           # Flask app code
├── requirements.txt # Dependencies
├── Procfile         # For Render deployment
└── README.md        # Project documentation

-**🙌 Contribution

Feel free to fork this repo, add new features (like score tracking, styling, or multiplayer), and create a pull request 🚀

📜 License

This project is licensed under the MIT License.

