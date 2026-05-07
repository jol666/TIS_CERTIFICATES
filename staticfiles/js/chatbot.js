document.addEventListener("DOMContentLoaded", () => {
  const chatbotToggle = document.getElementById("chatbot-toggle");
  const chatbotContainer = document.getElementById("chatbot-container");
  const chatbotClose = document.getElementById("chatbot-close");
  const sendBtn = document.getElementById("send-btn");
  const userInput = document.getElementById("user-input");
  const messages = document.getElementById("chatbot-messages");

  chatbotToggle.onclick = () => chatbotContainer.style.display = "block";
  chatbotClose.onclick = () => chatbotContainer.style.display = "none";

  sendBtn.onclick = sendMessage;
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  function sendMessage() {
    const text = userInput.value.trim();
    if (text === "") return;

    // Display user message
    const userMsg = document.createElement("div");
    userMsg.classList.add("user-message");
    userMsg.textContent = text;
    messages.appendChild(userMsg);
    userInput.value = "";

    // Scroll down
    messages.scrollTop = messages.scrollHeight;

    // Bot reply (basic keywords)
    setTimeout(() => {
      const botMsg = document.createElement("div");
      botMsg.classList.add("bot-message");
      botMsg.textContent = getBotReply(text);
      messages.appendChild(botMsg);
      messages.scrollTop = messages.scrollHeight;
    }, 600);
  }

  function getBotReply(input) {
    input = input.toLowerCase();

    if (input.includes("hello") || input.includes("hi"))
      return "Hello! 👋 How can I help you today?";
    if (input.includes("accreditation"))
      return "Accreditation ensures our certifications meet global standards. You can learn more on our Accreditation page.";
    if (input.includes("contact"))
      return "You can reach us through the Contact page or email us at info@tis-cert.com.";
    if (input.includes("iso"))
      return "We offer certification for various ISO standards such as ISO 9001, 14001, and 45001.";
    if (input.includes("thank"))
      return "You're very welcome! 😊";
    return "I'm not sure about that yet, but you can explore our website for more info.";
  }
});
