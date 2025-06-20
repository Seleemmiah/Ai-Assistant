
## 📘 `README.md` — AI Assistant App

```markdown
# 🧠 AI Assistant App (Voice + Text Chat)

An intelligent assistant app built with **Flutter** and **Django**, supporting both **voice and text interaction**. This app uses a custom Django backend to generate responses and authenticate users with dynamically generated API keys.

---

## 🚀 Features

- 🎙️ Voice-to-Text interaction using `speech_to_text`
- 💬 Real-time conversational UI
- 🔐 API Key authentication
- 📡 Custom Django backend (no OpenAI)
- 📱 Modern Flutter frontend (dark theme)
- 💾 Local API key storage with `SharedPreferences`

---

## 📸 Screenshots

> _Add your app screenshots here_

---

## 🛠️ Tech Stack

| Technology       | Usage                         |
|------------------|-------------------------------|
| Flutter          | Mobile frontend               |
| Dart             | Flutter app logic             |
| speech_to_text   | Voice input integration       |
| HTTP             | REST API requests             |
| SharedPreferences | Local API key storage         |
| Django           | Backend framework             |
| Django REST Framework | API creation and handling |
| UUID             | API key generation            |

---

## 📂 Project Structure

```

ai\_assistant\_project/
├── backend/            # Django API
│   ├── chatbotapi/     # Django project settings
│   ├── core/            # App with views and models
│   └── manage.py
│
└── frontend/           # Flutter app
├── lib/
│   ├── main.dart
│   ├── screens/
│   └── services/
└── pubspec.yaml

````

---

## 🔧 Getting Started

### ✨ 1. Backend (Django)

#### ✅ Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
````

#### ✅ Run Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### 🔐 API Endpoints

| URL                  | Method | Description                                      |
| -------------------- | ------ | ------------------------------------------------ |
| `/api/generate-key/` | POST   | Generate new API key                             |
| `/api/chat/`         | POST   | Send message (API key in `Authorization` header) |

---

### ✨ 2. Frontend (Flutter)

#### ✅ Setup

```bash
cd frontend
flutter pub get
flutter run
```

> Ensure the base URL in `api_service.dart` matches your backend server (e.g., `http://10.0.2.2:8000` for emulator or `http://192.168.x.x:8000` for real device)

---

## 📱 How It Works

1. On app launch, Flutter checks if an API key exists in storage.
2. If not, it calls the Django `/generate-key/` endpoint and saves the key.
3. Users can:

   * Speak to the mic 🎙️ (converts voice to text)
   * Type a message 🧑‍💻
4. Messages are sent via HTTP to `/chat/` with the API key in the header.
5. Django validates the key and returns a response.
6. Flutter displays the response in a chat-style UI.

---

## 🔐 Security

* Each API key is unique (UUID).
* Only valid API keys can use the `/chat/` endpoint.
* You can enhance security by adding:

  * Key expiration
  * Device fingerprinting
  * Authentication layer

---

## 🌍 Deployment Tips

* Use platforms like [Render](https://render.com), [Railway](https://railway.app), or [Heroku](https://heroku.com) for free backend hosting.
* Replace `http://localhost:8000` in your Flutter app with your deployed URL.

---

## 📦 Future Improvements

* Chat history (local or remote DB)
* Firebase authentication
* Integration with real AI models (HuggingFace, custom ML)
* Push notifications
* Light/Dark theme toggle

---

## ✨ Contributors

* **Developer:** \[Your Name]
* **Design:** \[Optional if you use Figma]

---

## 📄 License

This project is open-source under the MIT License.

---

```

---

Would you like me to:
- Export this as a file?
- Add Figma link/screenshots?
- Generate the `requirements.txt` for your backend?

Let me know and I’ll help you complete the polish!
```
