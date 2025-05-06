const express = require('express');
const multer = require('multer');
const app = express();
const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('video'), (req, res) => {
  console.log(`Uploaded: ${req.file.originalname}`);
  res.status(200).send('Upload successful!');
});

app.listen(8080, () => console.log('Uploader running on port 8080'));
