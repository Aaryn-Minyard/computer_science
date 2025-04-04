const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1l0v3luffy',
    database: 'mydatabase'
});



app.get('/users', (req, res) => {
    connection.query('SELECT * FROM yourtable', (err, results) => {
        if (err) {
            res.send('Error fetching users');
            return;
        }
        let html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User List</title>
        <style>
            /* Evergreen Forest-Themed Styles */

            body {
                background: linear-gradient(to bottom, #2c5e1a, #1a3d10);
                color: #eae7dc;
                font-family: "Georgia", serif;
                margin: 0;
                padding: 0;
            }

            h1 {
                text-align: center;
                color: #a8df65;
                font-size: 2em;
                margin-top: 20px;
            }

            ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
                text-align: center;
            }

            li {
                background: rgba(26, 61, 16, 0.85);
                color: #eae7dc;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
                font-size: 1.2em;
            }

            li:hover {
                background: rgba(44, 94, 26, 0.9);
            }

        </style>
    </head>
    <body>
        <h1>User List</h1>
        <ul>
            ${results.map(user => `<li>${user.name} (Age: ${user.age})</li>`).join('')}
        </ul>
    </body>
    </html>
`;

res.send(html);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/users`);
});
