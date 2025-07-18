# 🤖 Companion AI

**Companion AI** is a mental wellness chatbot powered by cutting-edge AI designed to assist individuals in overcoming **depression**, **anxiety**, and feelings of **loneliness**. More than just a chatbot, Companion AI is your **digital friend** — always available, empathetic, and ready to listen. It provides healthcare tips, mental wellness guidance, and even allows users to **book doctor appointments** directly from the platform.

---
## 👥 Team Members

- **Neeharika Joshi**  
- **Satwik Kishore**
---

## 🌟 Features

- 🧠 **AI-Powered Conversations**: Interact with an intelligent chatbot trained to provide emotional support and empathetic responses.
- 💬 **24/7 Mental Health Companion**: Always by your side, anytime, anywhere.
- ❤️ **Anxiety and Depression Management**: Offers tools, techniques, and conversations to reduce stress and promote mental clarity.
- 🧘‍♂️ **Personalized Wellness Tips**: Get custom healthcare advice and daily tips to maintain mental and physical well-being.
- 👩‍⚕️ **Doctor Booking System**: Book appointments with licensed healthcare professionals.
- 🔐 **Secure Login/Signup**: Modern, secure authentication flow with Firebase.
- 🧾 **Real-time Chat Interface**: Smooth and responsive messaging interface built with React.

---

## 🛠 Tech Stack

| Component       | Technology                |
|----------------|---------------------------|
| Frontend       | React.js                  |
| Backend        | Python                    |
| AI Model       | LLaMA 3.1B                |
| Database       | Firebase                  |
| Authentication | Python oAuth              |


---

## 🎥 Demo Videos

### 🔐 Login & Signup Flow

[!Login and Signup](https://github.com/user-attachments/assets/e833cf27-996c-4dfa-ab71-ff7d6c58ad29)

📍 *This video demonstrates the secure login and registration process.*

---

### 💬 Chatting with Companion AI


[](https://github.com/user-attachments/assets/631ef023-8050-49af-bdd8-ac5a84a08e89)



📍 *This video shows real-time interaction with the AI-based mental health assistant.*

---



Together, we aimed to build a safe and helpful environment where AI supports emotional well-being and personal growth.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/alkyema/CompanionAI.git
cd CompanionAI
````

### 2. Install Dependencies

#### Frontend

```bash
cd FrontEnd
npm install
npm start
```

#### Backend

```bash
cd ../Backend
pip install -r requirements.txt
uvicorn mainapi:app --reload --port 8888
```

### 3. Firebase Setup

* Create a Firebase project
* Enable Authentication (Email/Password)
* Set up Firestore Database
* Update the Firebase configuration in the Backend in .env file
---

## 🧠 AI Model (LLaMA 3 1.3B)

We use the **LLaMA 3 1.3B** model for generating context-aware, empathetic responses. The model has been fine-tuned with conversational data focused on mental wellness and user engagement.

---

## 💡 Future Enhancements

* Sentiment analysis for better emotional understanding
* Voice-based interaction and speech recognition
* Multi-language support
* Integration with wearable health devices (e.g., smartwatches)

---


> 🌈 *Companion AI is not a replacement for professional medical advice. Always consult a healthcare provider if you are in crisis or need urgent medical support.*



