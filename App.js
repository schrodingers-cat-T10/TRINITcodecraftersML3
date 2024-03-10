// App.js
import React, { useState } from 'react';
import './App.css';  // Import your main CSS file
import ImageUploader from './ImageUploader';
import CaptionDisplay from './CaptionDisplay';

function App() {
  const [caption, setCaption] = useState(null);

  const handleUpload = (newCaption) => {
    setCaption(newCaption);
  };

  return (
    <div className="App">
      <h1 style={{ textAlign: 'center' }}>Image Captioner</h1>
      <ImageUploader onUpload={handleUpload} />
      {caption && <CaptionDisplay caption={caption} />}
    </div>
  );
}

export default App;
