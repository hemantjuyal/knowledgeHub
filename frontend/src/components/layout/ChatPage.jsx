import React, { useEffect, useRef } from 'react';
import ChatWindow from './ChatWindow';
import MessageInput from './MessageInput';
import { useChat } from '../../hooks/useChat';

const ChatPage = () => {
  const { messages, isLoading, addBotMessage, sendMessage } = useChat();
  const isInitialMessageAdded = useRef(false);

  useEffect(() => {
    if (!isInitialMessageAdded.current && messages.length === 0) {
      addBotMessage(
        "Welcome to KnowledgeHub! I'm your AI assistant. You can explore your documents by asking questions, or type 'help' for more options."
      );
      isInitialMessageAdded.current = true;
    }
  }, [messages, addBotMessage]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <ChatWindow messages={messages} isLoading={isLoading} />
      <MessageInput onSendMessage={sendMessage} isLoading={isLoading} />
    </div>
  );
};

export default ChatPage;
