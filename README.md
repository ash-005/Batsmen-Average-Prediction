# Batsmen Average Prediction

This project implements a batsmen average prediction system using web scraping, data preprocessing, data visualization, machine learning, and a Flask-based website for visualization.

## Overview

The project follows these major steps:

1. **Data Collection**: Web scraping gathers cricket data from various online sources.
2. **Data Preprocessing**: The collected data is cleaned and preprocessed to ensure data quality and consistency.
3. **Data Visualization**: Visualizations are created to explore the data and identify correlations between the batting average and other features.
4. **Machine Learning**: Machine learning models are trained on the preprocessed data to predict batting averages.
5. **Web Interface**: A Flask-based web application is developed with a simple HTML template to showcase the prediction results.

## Requirements

- Python 3.11.6
- Flask
- Pandas
- Matplotlib
- Scikit-learn
- BeautifulSoup (for web scraping)
- Joblib (for model persistence)
- HTML/CSS (for web interface)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/batsmen-average-prediction.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the web interface at [http://localhost:5000](http://localhost:5000) in your web browser.

## Usage

1. Navigate to the web interface and input the required data or upload a dataset.
2. Explore the visualizations to understand the data correlations.
3. Use the prediction feature to predict batsmen averages based on selected features.

## Files Included

- `app.py`: Flask application for the web interface.
- `crick_analysis.ipynb`: Data preprocessing and visualization scripts.
- `webscrap_site.ipynb`: Webscraping the website to collect data script.
- `templates/`: HTML templates for the web interface.
- `requirements.txt`: List of required Python libraries.

## Contributing

Contributions are welcome! Feel free to submit a pull request if you have any suggestions, bug fixes, or improvements.

