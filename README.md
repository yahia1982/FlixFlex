# FlixFlex - Movie and Series Web Application

FlixFlex is a web application that caters to movie and series enthusiasts. It offers a range of features to enhance your movie and series-watching experience.

## Technologies Used

- **Python**: The primary programming language for the project.
- **Flask**: A micro web framework for building web applications in Python.
- **SQLite**: A lightweight, serverless, and self-contained database used for storing user data and movie/series information.

## Features

FlixFlex comes equipped with a variety of exciting features, including:

- **User Registration**: Create an account with a unique username and secure password to access personalized content and features.

- **Browse Movies and Series**: Explore a diverse collection of movies and TV series, organized into different pages for your convenience.

- **Top 5 Recommendations**: Discover the top 5 movies and series showcased in a dedicated section on the movies and series pages.

- **Pagination**: To make navigation smoother, movies and series are available in batches of 10 per page.

- **Favorites List**: Add your favorite movies or series to your list and manage them effortlessly.

- **Remove from Favorites**: Don't want a movie or series in your favorites anymore? You can delete it from your list with ease.

- **View Favorite Content**: Access and view your curated list of favorite movies and series, ensuring you never miss a great show.

- **Search Functionality**: Use the search feature to look for specific movies and series based on keywords or titles.

- **View Details**: Get in-depth information about a selected movie or series, including cast, ratings, and synopsis.

- **Watch Trailers**: Watch trailers of your favorite movies and series right on the platform.

## Running the Project

To run FlixFlex, you can follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flixflex.git
   cd flixflex
2. Build docker image
    ```bash
    docker build -t flixflex-app .
3. Run Container
    ```bash
   docker run -p 5000:5000 flixflex-app
