const express = require("express");
const path = require("path");
const app = express();
const cors = require("cors"); 
require('dotenv').config();
const port = process.env.PORT;

app.use(cors());

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to serve environment variables
app.get('/env', (req, res) => {
  res.json({
    HOST: process.env.HOST,
    // Add other environment variables as needed
  });
});

// Route to serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post("/classify", async (req, res) => {
    try {
        // TO DO: implement image classification logic here
        const classificationResult = {
            message: "classification result",
        };

        res.json(classificationResult);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Internal Server Error" });
    }
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});