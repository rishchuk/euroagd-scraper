# Euro.com.pl Laptop Scraper

This is a Python project for scraping laptop information from Euro.com.pl.

I created this project to practice Python, web scraping, Selenium, BeautifulSoup, and working with CSV files.


## What this project does

The scraper gets laptop information from the euro.com.pl website.

It collects:

* Product title
* Price
* Image URL
* Technical specifications

The scraper can also go through different pages of the laptop catalog.

The collected data is saved to a CSV file.

## Technologies

This project uses:

* Python
* Selenium
* BeautifulSoup
* CSV
* Chrome WebDriver

## Project structure

```text
euroagd-scraper/
│
├── data/
│   └── laptops.csv
│
├── src/
│   ├── browser.py
│   ├── csv_writer.py
│   ├── logger.py
│   ├── main.py
│   ├── models.py
│   ├── parser.py
│   └── scraper.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## How to install

First, clone the repository:

```bash
git clone https://github.com/rishchuk/euroagd-scraper.git
```

Go to the project folder:

```bash
cd euroagd-scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Activate the virtual environment on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to run

Run the main file:

```bash
python src/main.py
```

The program opens Chrome and starts scraping the laptop pages.

After scraping is finished, the data is saved to:

```text
data/laptops.csv
```

## CSV data

The CSV file contains four columns:

| Column           | Description                            |
| ---------------- | -------------------------------------- |
| `Title`          | Laptop name                            |
| `Price`          | Laptop price                           |
| `Image URL`      | Link to the laptop image               |
| `Specifications` | Technical information about the laptop |

Example:

```text
Title,Price,Image URL,Specifications
"Laptop HP OmniBook 3 16-by0028nwx 16"" R5 40 8GB RAM 256GB Dysk SSD Win11 Czarny",1 999.00 zł,"https://f00.esfr.pl/foto/4/192315626929/e8ea62a98903f1f989ccaeb45c2c1582/hp-laptop-hp-ob-3-16-r5-8-256-w11,192315626929_7.webp","{'Ekran': '16 "",  1920 x 1200 pikseli', 'Procesor': 'AMD Ryzen™ 5 40', 'Pamięć': '8 GB  LPDDR5 5500 Mhz RAM', 'Grafika': 'AMD  Radeon™ 610M Graphics', 'Dysk': '256 GB SSD', 'System operacyjny': 'Windows 11 Home Edition'}"
```

## How the project works

The project has several Python files.

### `browser.py`

This file creates the Selenium Chrome driver and opens web pages.

### `parser.py`

This file gets information from the HTML page.

For example, it gets:

* laptop title
* price
* image
* specifications

### `models.py`

This file contains the `Product` class.

The class describes one laptop product.

### `scraper.py`

This is the main scraper logic.

It:

1. Opens the page.
2. Finds products.
3. Parses the products.
4. Goes to the next page.
5. Repeats the process.

### `csv_writer.py`

This file saves the products to a CSV file.

### `logger.py`

This file configures logging for the project.

### `main.py`

This is the starting point of the program.

It creates the scraper, starts scraping, and saves the results.

## What I want to improve

This project is still in development.

In the future, I want to improve:

* Error handling
* Tests
* CSV export

## Important

This project is created for learning purposes.

## Author

This is a personal learning project.
