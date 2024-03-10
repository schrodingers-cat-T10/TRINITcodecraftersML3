// ImageUploader.js
import React, { useState } from 'react';
import './ImageUploader.css';

function ImageUploader({ onUpload }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);

    // Display the image to the user immediately after selection
    const url = URL.createObjectURL(file);
    setImageUrl(url);
  };

  const handleUpload = () => {
    if (!selectedFile) {
      console.error('No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedFile);

    fetch('/upload/', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        onUpload(data.caption);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div className="ImageUploader">
      <input type="file" onChange={handleFileChange} />
      {imageUrl && <img src={imageUrl} alt="Preview" />}
      <button onClick={handleUpload}>Upload Image</button>
    </div>
  );
}

export default ImageUploader;
