const jwt = require('jsonwebtoken');
const fs = require('fs');

module.exports = (req, res) => {

    const enteredEmail = req.query.email;
    const enteredPassword = req.query.password;

    fs.readFile('./database/accounts.json', (err, data) => {
        if (err) console.log(err);

        const accounts = JSON.parse(data);
        const account = accounts[enteredEmail];

        if (account) {
            const accountPassword = account.password;

            if (enteredPassword === accountPassword) {
                const card = jwt.sign(
                    {'email': enteredEmail, 'status': 'Authenticated'},
                    'secret'
                ); //'status': 'Authenticated'
                console.log('accessing: ', enteredEmail);
                return res.status(200).send(card)
            } else {
                return res.status(404).send("Wrong password")
            }
        } else {
            return res.status(404).send("Email does not exist")
        }
    })
}

