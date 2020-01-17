const jwt = require('jsonwebtoken');

module.exports = (req, res) => {
    if (req.query.email) {
        const email = req.query.email;
        console.log('company email registered: ' + email);
        const card = jwt.sign(
            { 'status': 'OK', 'message': 'company registered', 'secretkey': 'secret' },
            'anotherSecret'
        );
        return res.status(200).send(card)
    } else {
        return res.status(404).send();
    }
}