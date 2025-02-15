# Asymptotic Analysis
This project implements various sorting algorithms and provides an interface to interact with them. The program allows users to select different sorting methods and visualize their performance using graphical representations.

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Files and Structure](#files-and-structure)  
4. [Usage](#usage)  
5. [License](#license)  

---

## Project Overview

This project focuses on implementing various sorting algorithms and providing an interface to interact with them. The program allows users to select different sorting methods and visualize their performance using graphical representations.

---

## Features

- **Multiple Sorting Algorithms**: Implements various sorting techniques to handle different input cases.
- **Graphical Visualization**: Provides graphical representations of sorting performance.
- **Multi-Language Support**: Supports **English and Portuguese interfaces** for ease of use.
- **CSV Data Handling**: Uses structured data (ascending, descending, random) to demonstrate sorting behavior.
- **Modular Design**: Well-structured and documented codebase for easy modifications and enhancements.

## Files and Structure

```
project_root/
│-- data/
│   │-- ascending.csv
│   │-- descending.csv
│   │-- graphics.py
│   │-- random.csv
│-- interfaces/
│   │-- english_interface.py
│   │-- portuguese_interface.py
│-- .gitignore
│-- LICENSE
│-- README.md
│-- __init__.py
│-- main.py
│-- setup.py
│-- sorting_algorithms.py
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To execute the program, simply run:
```sh
python main.py
```

The program will prompt you to choose between different interfaces (English or Portuguese) and sorting options.

## Features

- Various sorting algorithms implemented in `sorting_algorithms.py`
- CSV data files for testing different cases (ascending, descending, random)
- Graphical representation of sorting performance in `graphics.py`
- Support for English and Portuguese interfaces

## License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.
