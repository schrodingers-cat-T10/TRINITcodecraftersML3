// CaptionDisplay.js
import React from 'react';

function CaptionDisplay({ caption }) {
  return (
    <div>
      <h2>Caption:</h2>
      <p>{caption}</p>
    </div>
  );
}

export default CaptionDisplay;
