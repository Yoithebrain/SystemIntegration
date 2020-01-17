const express = require('express');
const app = express();

app.use(express.json());

const index = require('./routes/index.js');
const login = require('./routes/login.js');

app.get('/', index);    
app.get('/login', login);   

// ############################################
const server = app.listen(8081, (err) => {
    if (err) { console.log(err); return; }
    console.log('BANK server listening on port...', server.address().port)
})