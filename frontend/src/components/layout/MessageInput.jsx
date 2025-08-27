import React, { useState } from 'react';

const MessageInput = ({ onSendMessage, isLoading }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSend = () => {
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue);
      setInputValue('');
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey && !isLoading) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div style={{ display: 'flex', padding: '15px', borderTop: '1px solid #e0e0e0', backgroundColor: '#f7f7f8' }}>
      <textarea
        rows="1"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder={isLoading ? "Processing..." : "Message KnowledgeHub..."}
        disabled={isLoading}
        style={{
          flex: 1,
          padding: '12px 15px',
          borderRadius: '20px',
          border: '1px solid #ccc',
          resize: 'none',
          overflowY: 'hidden',
          fontSize: '16px',
          lineHeight: '24px',
          maxHeight: '120px',
          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.05)',
          transition: 'height 0.2s ease-out',
          cursor: isLoading ? 'not-allowed' : 'text',
          backgroundColor: isLoading ? '#e9e9e9' : 'white',
        }}
      />
      <button
        onClick={handleSend}
        disabled={isLoading}
        style={{
          marginLeft: '10px',
          padding: '12px 20px',
          borderRadius: '20px',
          border: 'none',
          backgroundColor: isLoading ? '#a0a0a0' : '#10a37f',
          color: 'white',
          fontSize: '16px',
          cursor: isLoading ? 'not-allowed' : 'pointer',
          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
          transition: 'background-color 0.2s ease-in-out',
        }}
      >
        Send
      </button>
    </div>
  );
};

export default MessageInput;
