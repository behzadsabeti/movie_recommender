# Movie Recommender

A simple movie recommender system built with Python and FastAPI.

## Description

This project is a web-based application that recommends movies based on user input. It utilizes a dataset of movies and user ratings to provide personalized recommendations. The dataset is sourced from a custom web crawler created by myself [LetterboxdCrawler](https://github.com/behzadsabeti/LetterboxdCrawler)

## Features

- **Movie Recommendations:** Users can input their favorite movies, and the system will recommend similar movies.
- **User Interface:** A simple and intuitive web interface built with HTML and FastAPI.
- **Deployment Ready:** Configured to be deployed on platforms like Railway.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/behzadsabeti/movie_recommender.git
    cd movie_recommender
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Open a web browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

3. **Input your favorite movies to get recommendations.**

## Project Structure

- **data/**: Contains the dataset used for recommendations.
- **services/**: Contains the logic for processing data and generating recommendations.
- **templates/**: Contains the HTML templates for the web interface.
- **views/**: Contains the Flask routes and views for the web application.
- **main.py**: The main entry point for the application.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **Procfile**: Configuration for deploying the app on platforms like Railway.

## Data Source

The data used in this project is collected using a custom web crawler. You can find the crawler at [LetterboxdCrawler](https://github.com/behzadsabeti/LetterboxdCrawler).

## Deployment

The application is configured to be deployed on Railway. Ensure you have a Railway account and follow their deployment documentation to get the app running.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries, please contact the repository owner.
