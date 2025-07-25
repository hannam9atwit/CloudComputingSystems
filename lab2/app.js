const express = require('express');
const path = require('path');
const app = express();
const PORT = 8000;

// Serve static HTML pages
app.use(express.static('public'));

// About page
app.get('/about', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/about.html'));
});

// Recipe page by ID (1 or 2)
app.get('/recipe/:id', (req, res) => {
  const id = req.params.id;
  const file = id === '1' ? 'recipe1.html' :
               id === '2' ? 'recipe2.html' :
               null;
  if (file) {
    res.sendFile(path.join(__dirname, 'public', file));
  } else {
    res.status(404).send('Recipe not found');
  }
});

// Leave comment for recipe
app.get('/comment/:id', (req, res) => {
  res.send(`Leave a comment for recipe #${req.params.id}`);
});

// Greeting with query string
app.get('/greet', (req, res) => {
  const name = req.query.name || 'guest';
  res.send(`Hello, ${name}! Welcome to Michael's Cookbook`);
});

// Submit feedback via query string
app.get('/feedback', (req, res) => {
  const { dish, rating } = req.query;
  res.send(`Thanks for rating ${dish} with a ${rating}/5!`);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
