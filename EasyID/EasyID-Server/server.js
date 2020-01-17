const express = require('express');
const app = express();

// allow body parsing req.body
app.use(express.json()); 

// multiple route requires
const index = require('./routes/index.js');
const signup = require('./routes/signup.js');
const login = require('./routes/login.js');

// routes 
app.get('/', index);    
app.post('/signup', signup);    // post new company account to db
app.get('/login', login);       // get token to login as easyID account

// ############################################
const server = app.listen(80, (err) => {
    if (err) { console.log(err); return; }
    console.log('EASYID server listening on port...', server.address().port)
})