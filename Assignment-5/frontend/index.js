const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Form UI
app.get('/', (req, res) => {
    res.send(`
        <h2>Simple Form</h2>
        <form method="POST" action="/submit">
            Name: <input name="name" /><br/><br/>
            Email: <input name="email" /><br/><br/>
            <button type="submit">Submit</button>
        </form>
    `);
});

// Send data to Flask backend
app.post('/submit', async (req, res) => {
    const { name, email } = req.body;

    try {
        const response = await axios.post('http://backend:5000/api', {
            name: name,
            email: email
        });

        res.send(`<h3>${response.data.message}</h3>`);
    } catch (error) {
        res.send("Error connecting to backend");
    }
});

app.listen(3000, () => console.log("Frontend running on port 3000"));