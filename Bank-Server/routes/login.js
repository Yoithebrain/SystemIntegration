const jwt = require('jsonwebtoken');
const fs = require('fs');
const xml = require('xml');

module.exports = (req, res) => {

    var token = req.query.token

    jwt.verify(token, 'secret', function (err, tokenData) {
        if (err) { return res.status(404).send('Invalid token') }

        const tokenEmail = tokenData.email;
        const tokenStatus = tokenData.status;

        fs.readFile('./database/accounts.json', (err, accountData) => {
            if (err) console.log(err);

            const accounts = JSON.parse(accountData);
            const account = accounts[tokenEmail];

            if (account) {
                if ('Authenticated' === tokenStatus) {
                    console.log('request from:', tokenEmail)
                    res.set('Content-Type', 'text/xml')
                    return res.send(xml('<AccountBalance='+account.balance+"/>"));


                    //return res.status(200).json(account.balance)
                } else {
                    return res.status(404).send('Password is wrong')
                }
            } else {
                return res.status(404).send('Account does not exist')
            }
        })
    })
}
