import React from 'react';

const ChatWindow = ({ messages, isLoading }) => {
  return (
    <div style={{ flex: 1, overflowY: 'auto', padding: '20px', backgroundColor: '#f0f0f0' }}>
      {messages.map((msg, index) => (
        <div key={index} style={{
          display: 'flex',
          justifyContent: msg.sender === 'user' ? 'flex-end' : 'flex-start',
          marginBottom: '10px',
        }}>
          <div style={{
            maxWidth: '70%',
            padding: '12px 16px',
            borderRadius: '18px',
            backgroundColor: msg.sender === 'user' ? '#dcf8c6' : '#ffffff',
            color: '#333',
            boxShadow: '0 1px 0.5px rgba(0, 0, 0, 0.13)',
            wordWrap: 'break-word',
            whiteSpace: 'pre-wrap',
          }}>
            {msg.text}
          </div>
        </div>
      ))}
      {isLoading && (
        <div style={{
          display: 'flex',
          justifyContent: 'flex-start',
          marginBottom: '10px',
        }}>
          <div style={{
            maxWidth: '70%',
            padding: '12px 16px',
            borderRadius: '18px',
            backgroundColor: '#ffffff',
            color: '#333',
            boxShadow: '0 1px 0.5px rgba(0, 0, 0, 0.13)',
            wordWrap: 'break-word',
            whiteSpace: 'pre-wrap',
          }}>
            ...
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatWindow;
