# 💸 PennyTrack - Personal Expense Tracker

PennyTrack is a minimal yet powerful web application designed to help you manage and visualize your daily expenses. Whether you're tracking bills, food, travel, or other costs, PennyTrack makes it effortless with a simple UI and powerful backend.

🔗 **Live App**: [https://pennytrack-production.up.railway.app/](https://pennytrack-production.up.railway.app/)

---

## 🚀 Features

- 🧾 Add, view, and categorize expenses
- 🗕️ Date-based tracking
- 📊 Expense history and insights
- 🔐 User authentication (login/register)
- 🎨 Clean & responsive UI (Bootstrap-powered)
- ☁️ Ready for deployment (Render/Heroku/GitHub Pages Backend)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, Jinja2
- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Deployment**: Render / Railway

---

## 💻 Local Setup Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/btmiamsujal/PennyTrack.git
   cd PennyTrack
   ```

2. **Create a virtual environment & activate it:**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB URI:**

   - Inside `app.py`, set your MongoDB URI.
   - You can use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for free hosting.

5. **Run the app:**

   ```bash
   python app.py
   ```

   > App will run on `http://localhost:5000`

---

## 📦 Versions

### 🧾 PennyTrack v1

- Core functionality to **add, view, and categorize expenses with login/register system**.

---

## ✨ Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📓 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Bootstrap 5
- Flask
- MongoDB
- FontAwesome Icons

---

### Made with ❤️ by Sujal

