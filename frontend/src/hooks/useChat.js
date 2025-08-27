import { useState } from 'react';
import { sendMessage as sendApiMessage } from '../api/chatService'; // Alias the imported function

export const useChat = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const addUserMessage = (message) => {
    setMessages(prev => [...prev, { text: message, sender: 'user' }]);
  };

  const addBotMessage = (message) => {
    setMessages(prev => [...prev, { text: message, sender: 'bot' }]);
  };

  const sendMessage = async (message) => { // New function to handle sending messages
    addUserMessage(message); // Add user message to display immediately
    setIsLoading(true); // Set loading to true

    try {
      const botResponse = await sendApiMessage(message); // Call the aliased function
      addBotMessage(botResponse.message); // Access the message property
    } catch (error) {
      console.error("Error sending message:", error);
      addBotMessage("Sorry, I encountered an error. Please try again."); // Display error message
    } finally {
      setIsLoading(false); // Set loading to false regardless of success or failure
    }
  };

  return { messages, isLoading, addUserMessage, addBotMessage, sendMessage };
};
