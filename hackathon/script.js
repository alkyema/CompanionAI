// Speech recognition and chat functionality
let recognition;
let isRecording = false;
const chatInputField = document.getElementById("chat-input-field");
const sendButton = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");
const micButton = document.getElementById("mic-button");
const cloud = document.getElementById("cloud");
const cloudText = document.getElementById("cloud-text");
const video = document.querySelector(".background-video"); // Corrected selector for the video element

// Ensure video is paused on initial load
video.pause();

if ("webkitSpeechRecognition" in window || "SpeechRecognition" in window) {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.continuous = false;
  recognition.interimResults = false;

  // Speech recognition result handler
  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    chatInputField.value = transcript;
    sendMessage();
  };

  // Start recording indicator
  recognition.onstart = () => {
    micButton.classList.add("active");
  };

  // Stop recording indicator
  recognition.onend = () => {
    micButton.classList.remove("active");
    isRecording = false;
  };
}

// Toggle speech recognition
micButton.addEventListener("click", () => {
  if (isRecording) {
    recognition.stop();
  } else {
    recognition.start();
    isRecording = true;
  }
});

// Handle send button click
sendButton.addEventListener("click", sendMessage);

// Function to control video playback
function controlVideo(play) {
  if (play) {
    video.play();
  } else {
    video.pause();
    video.currentTime = 0;
  }
}

// Function to send and display message
async function sendMessage() {
  const userMessage = chatInputField.value.trim();

  if (userMessage) {
      addMessage(userMessage, "sent");
      chatInputField.value = "";

      let botResponse = "";
      if (userMessage.toLowerCase() === "hi" || userMessage.toLowerCase() === "hello") {
          botResponse = "Hello! How can I assist you today?";
      } else if (userMessage.toLowerCase() === "how are you") {
          botResponse = "I’m just a bot, but I’m here to help! How about you?";
      } else {
          botResponse = await toogle_appliance(userMessage); // Wait for the API response
      }

      setTimeout(() => {
          addMessage(botResponse, "received");
          speakText(botResponse);
      }, 500);
  }
}

// Function to add new message to chat area
function addMessage(message, type) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("chat-message", type);
  messageElement.innerText = message;
  chatMessages.appendChild(messageElement);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to speak the text and show cloud
function speakText(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "en-US";

  cloudText.innerText = text;
  cloud.style.display = "flex";

  utterance.onstart = () => {
    controlVideo(true);
  };

  utterance.onend = () => {
    controlVideo(false);
    setTimeout(() => {
      cloud.style.display = "none";
    }, 3000);
  };

  window.speechSynthesis.speak(utterance);
}

// Listen for Enter key to send message
chatInputField.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    sendMessage();
  }
});

var AppToogleAPI = 'http://127.0.0.1:8888/apptoogle';

async function toogle_appliance(Applicances_name) {
  try {
      const Feed = { Appliance_name: Applicances_name };

      // Fetch Authorization Token if not already available
      if (!Authorization_Token) {
          Authorization_Token = await fetchAndLogJson(jsonUrl);
      }

      if (!Authorization_Token) {
          throw new Error("Failed to retrieve authorization token.");
      }

      // Perform the API call
      const response = await fetch(AppToogleAPI, {
          method: "POST",
          headers: {
              'Authorization': `Bearer ${Authorization_Token['apptoogle_Token']}`,
              "Content-Type": "application/json",
          },
          body: JSON.stringify(Feed),
      });

      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Success:", data);

      // Return the response to be used by sendMessage
      return data;

  } catch (error) {
      console.error("Error:", error);
      return "An error occurred while processing your request.";
  }
}
const jsonUrl = 'data.json';
var Authorization_Token = "";

async function fetchAndLogJson(url) {
    try {
        const response = await fetch(url, { method: 'GET',headers: {'Content-Type': 'application/json'} } );
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        data = await response.json();
        return data
    } catch (error) {
        console.error('Error fetching JSON:', error);
    }
}