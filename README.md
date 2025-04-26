 # Rexsy Flask Microservices

 A collection of Flask microservices demonstrating:
 - Password generation and validation
 - Sentiment analysis using TextBlob
 - Fear and Greed index emailer
 - Top US news headlines via NewsAPI
 - Bitcoin price retrieval and emailer

 ## Table of Contents
 - [Features](#features)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
 - [Configuration](#configuration)
 - [Running the Application](#running-the-application)
 - [Microservice Endpoints](#microservice-endpoints)
   - [1. Homepage](#1-homepage)
   - [2. Password Service](#2-password-service)
   - [3. Sentiment Analysis Service](#3-sentiment-analysis-service)
   - [4. Fear and Greed Index Service](#4-fear-and-greed-index-service)
   - [5. News API Service](#5-news-api-service)
   - [6. Bitcoin Price Service](#6-bitcoin-price-service)
 - [Example Usage](#example-usage)
 - [Project Structure](#project-structure)
 - [Contributing](#contributing)
 - [License](#license)
 - [Contact](#contact)

 ## Features
 - **Password Service**: Generate secure passwords, assess strength, and check against common passwords.
 - **Sentiment Analysis**: Classify text as positive, negative, or neutral.
 - **Fear and Greed Index**: Fetch current index and send via email.
 - **News API**: Retrieve top US headlines and email summaries.
 - **Bitcoin Price**: Get current BTC price in USD and optionally email updates.

 ## Prerequisites
 - Python 3.8 or higher
 - `pip` package manager
 - SMTP-capable email account (e.g., Gmail) for email services
 - API keys for:
   - [NewsAPI.org](https://newsapi.org/) (`NEWS_API_KEY`)
   - [CoinGecko](https://www.coingecko.com/) (`COINGECKO_API_KEY`)

 ## Installation
 Download or clone this repository, then:
 ```bash
 cd <project-directory>
 python3 -m venv venv
 source venv/bin/activate
 pip install --upgrade pip
 pip install -r requirements.txt
 ```

 ## Configuration
 1. Create a `.env` file in the project root:
    ```
    EMAIL=<your_email@example.com>
    EMAIL_PASSWORD=<your_email_password>
    NEWS_API_KEY=<your_newsapi_org_key>
    COINGECKO_API_KEY=<your_coingecko_api_key>
    ```
 2. Optionally adjust Flask settings or mail server configuration in `app/__init__.py`.

 ## Running the Application
 ```bash
 python main.py
 ```
 By default, the app runs on `http://127.0.0.1:5000/`.

 ## Microservice Endpoints

 ### 1. Homepage
 - **URL:** `/`
 - **Method:** GET
 - **Response:** HTML landing page with links to all services.

 ### 2. Password Service
 - **URL Prefix:** `/password`
 - **GET** `/password/`  
   Returns a simple HTML page for the password microservice.
 - **GET** `/password/get_random_password`  
   Generates and returns a random secure password in JSON:
   ```json
   {
     "output": { "password": "<pwd>", "length": <n> },
     "status": 200
   }
   ```
 - **POST** `/password/check_password`  
   Checks password strength.  
   **Form Data:** `password=<your_password>`  
   **Response:**  
   ```json
   { "password": "strong"|"medium"|"weak"|"very weak" }
   ```
 - **POST** `/password/password_common_checker`  
   Checks if password is among common passwords.  
   **Form Data:** `password=<your_password>`  
   **Response:**  
   ```json
   { "is_password_common": true|false }
   ```

 ### 3. Sentiment Analysis Service
 - **URL Prefix:** `/sentiment_analysis`
 - **GET** `/sentiment_analysis/`  
   Test endpoint returning a greeting string.
 - **POST** `/sentiment_analysis/do_analysis`  
   Analyzes text sentiment.  
   **Form Data:** `text=<your_text>`  
   **Response:**  
   ```json
   { "sentiment": "positive"|"negative"|"neutral" }
   ```

 ### 4. Fear and Greed Index Service
 - **URL Prefix:** `/fng_bp`
 - **GET** `/fng_bp/`  
   Test endpoint returning a greeting string.
 - **GET** `/fng_bp/get_fng/<email>`  
   Fetches current fear and greed index and emails the result to `<email>`.  
   **Response:**  
   ```json
   { "status_code": 200 }
   ```

 ### 5. News API Service
 - **URL Prefix:** `/newsapi`
 - **GET** `/newsapi/`  
   Test endpoint returning a greeting string.
 - **POST** `/newsapi/get_news`  
   Retrieves top US headlines, compiles a summary, and emails it.  
   **Form Data (optional):** `email=<recipient@example.com>`  
   Defaults to the configured sender email if omitted.  
   **Response:**  
   ```json
   { "status_code": 200 }
   ```

 ### 6. Bitcoin Price Service
 - **URL Prefix:** `/btc_getter`
 - **GET** `/btc_getter/`  
   Test endpoint returning a greeting string.
 - **POST** `/btc_getter/get_btc`  
   Fetches current Bitcoin price in USD.  
   **Form Data (optional):** `EMAIL=<recipient@example.com>`  
   **Response:**  
   ```json
   {
     "status_code": 200,
     "coin": "btc",
     "usd": <price>,
     "last_updated": "<timestamp>"
   }
   ```

 ## Example Usage
 **Fetch a random password**  
 ```bash
 curl http://127.0.0.1:5000/password/get_random_password
 ```

 **Analyze sentiment**  
 ```bash
 curl -X POST -F "text=I love using Flask!" http://127.0.0.1:5000/sentiment_analysis/do_analysis
 ```

 **Get Bitcoin price and email**  
 ```bash
 curl -X POST -F "EMAIL=you@example.com" http://127.0.0.1:5000/btc_getter/get_btc
 ```

 ## Project Structure

 .
 ├── app
 │   ├── __init__.py
 │   ├── routes.py               # Blueprint registration & homepage
 │   ├── utils.py                # Shared utility functions
 │   └── blueprints
 │       ├── btc_getter_bp       # Bitcoin price microservice
 │       │   ├── bp.py
 │       │   └── routes.py
 │       ├── fng_bp              # Fear and Greed index microservice
 │       │   ├── bp.py
 │       │   └── routes.py
 │       ├── newsapi_bp          # News API microservice
 │       │   ├── bp.py
 │       │   ├── models.py
 │       │   └── routes.py
 │       ├── password_bp         # Password generation & validation microservice
 │       │   ├── __init__.py
 │       │   ├── bp.py
 │       │   ├── routes.py
 │       │   └── templates
 │       └── sentiment_analysis_bp # Sentiment analysis microservice
 │           ├── bp.py
 │           └── routes.py
 ├── main.py                     # Entry point: runs the Flask app
 ├── requirements.txt            # Python dependencies
 └── password.txt                # Common passwords list for Password Service

 ## Contributing
 Contributions are welcome! Feel free to open issues or submit pull requests.

 ## License
 This project does not have a specific open-source license.

 ## Contact
 GitHub: https://github.com/rexsybima