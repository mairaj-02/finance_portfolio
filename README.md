# Finance Potfolio

A modern, responsive web application for managing stock portfolios, built with Flask and SQLite.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)

## Features

- User authentication (register, login, logout)
- Real-time stock quotes
- Buy and sell stocks
- Portfolio overview with current holdings
- Transaction history
- Modern, responsive design inspired by Apple's design language
- Mobile-friendly interface

## Technologies Used

- **Backend**: Python, Flask, SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **API**: IEX Cloud for stock data
- **Icons**: Font Awesome

## Database Schema

### Users Table

``` sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
);
```

### Transactions Table

``` sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    symbol TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

## API Endpoints

| Endpoint  | Method   | Description                 | Authentication Required |
|-----------|----------|-----------------------------|-------------------------|
| /         | GET      | Display Portfolio Dashboard | Yes                     |
| /register | GET/POST | Register New User           | No                      |
| /login    | GET/POST | Login User                  | No                      |
| /logout   | GET      | Logout User                 | Yes                     |
| /quote    | GET/POST | Get Stock Quote             | Yes                     |
| /buy      | GET/POST | Buy Stocks                  | Yes                     |
| /sell     | GET/POST | Sell Stocks                 | Yes                     |
| /history  | GET      | Stocks Transaction History  | Yes                     |

## Acknowldgements
- [CS50](https://www.edx.org/cs50) for the original Problem
- [Bootstrap](https://getbootstrap.com/) for UI framework
- [Font Awesome](https://fontawesome.com/) for Icons


## License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

