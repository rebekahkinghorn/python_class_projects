# Python Class Projects

Python assignments I completed for IS 303 at Brigham Young University in Fall 2024. This collection shows my work with user input, dictionaries, loops, functions, exception handling, object-oriented programming, data analysis, and databases.

Each folder contains a separate assignment. These are learning projects, and some retain the assumptions and limitations of the original coursework.

## Assignments

- [A02: Submitting to GitHub](a02_submitting_to_github/) — Basic user input, arithmetic, and printed output.
- [A03: BMI Calculator](a03_bmi_calculator/) — Calculates BMI and a classification from user input.
- [A04: Friend Tracker](a04_friend_tracker/) — Stores friends and hobbies in a dictionary and provides a menu for adding and finding entries.
- [A05: Soccer Teams](a05_soccer_teams/) — Simulates soccer results and tracks wins and losses.
- [A06: Function Smorgasbord](a06_function_smorgasbord/) — Defines reusable functions in a separate module and calls them from a main program.
- [A07: Currency Converter](a07_currency_converter/) — Converts US dollars using a provided exchange-rate dictionary and practices exception handling.
- [A08: Pokémon](a08_pokemon/) — Defines Pokémon and move classes, with attributes and methods.
- [A09: Soccer Teams with Inheritance](a09_soccer_teams/) — Uses team and game classes, inheritance, and season statistics.
- [A10: Pandas](a10_pandas/) — Reads a CSV, updates and filters data, calculates summaries, and exports results to Excel.
- [A11: Movie Tracker](a11_movie_tracker/) — Uses Peewee and SQLite to save a watchlist, record ratings, and retrieve or delete movies.

## Requirements

Install Python 3 before running these programs. A02–A09 use Python's standard library and local assignment files; they do not need additional packages.

A10 and A11 need these packages:

- **[pandas](https://pandas.pydata.org/):** Reads and processes tabular data in A10.
- **[openpyxl](https://openpyxl.readthedocs.io/):** Supports writing A10's results to an Excel `.xlsx` file.
- **[Peewee](https://docs.peewee-orm.com/):** Connects A11's Python model to its SQLite database.

Install all three from a terminal:

```bash
python -m pip install pandas openpyxl peewee
```

If you have downloaded the accompanying `requirements.txt`, you can instead run this from the repository's main folder:

```bash
python -m pip install -r requirements.txt
```

On systems where Python is called `python3` or `py`, use that command instead of `python`.

## Running an Assignment

Download and extract this repository, or clone it with Git. Open a terminal in the assignment's folder and run its main Python file. Each assignment runs independently; there is no single program that launches the whole collection.

For example, from the repository's main folder:

```bash
cd a04_friend_tracker
python a4_friend_tracker.py
```

Follow the prompts in the terminal. Viewing a file on GitHub displays its source code; it does not run the program.

### A06: Keep Both Python Files Together

`a6_function_smorgasbord.py` imports functions from `a6_my_functions.py`. Keep both files in the same folder with their original names. From `a06_function_smorgasbord`, run:

```bash
python a6_function_smorgasbord.py
```

### A10: Include the Input Data

Keep `practice_names.csv` alongside `a10_pandas_basics.py`. From `a10_pandas`, run:

```bash
python a10_pandas_basics.py
```

Run the command from that folder so the program can find the CSV. It creates `mean_salary_by_city.xlsx` in the current folder; that output file is not required to start the program. Running the program again can overwrite the previous export.

### A11: A Local Movie Database

From `a11_movie_tracker`, run:

```bash
python a11_movie_tracker.py
```

The program creates `movies.db` in the current folder and saves your movie list there between sessions. No database file or separate database server is needed beforehand. Run it from the same folder each time to keep using the same database.

## Credits and Authorship

I wrote the assignment implementations as a student in IS 303. The assignment designs, requirements, prompts, and course-provided materials belong to the instructor/course, and I do not claim them as my original work.

The original GitHub Classroom repositories include course-material updates by [jacobsteffenBYU](https://github.com/jacobsteffenBYU). Specific provided material includes:

- **A07:** The `conversion_rates` dictionary, including the currency codes, rates, and explanatory comments, was supplied in the starter file. I implemented the conversion and input-handling logic around it.
- **A10:** `practice_names.csv` was supplied with the assignment. I wrote the Python data-processing steps using that dataset.
- **A08:** The assignment instructions supplied example Pokémon and move values to use when creating objects. I implemented the classes and their methods to meet those instructions.
- **Assignment templates:** The original Python starter files for A02–A06 and A08–A11 contained placeholder comments. Some template comments remain in this collection.
- **Course infrastructure:** The original repositories supplied assignment instructions, tests, grading configuration, and, where applicable, rubrics and test-case descriptions. Those materials were part of the course setup, not my implementations.

pandas, openpyxl, and Peewee are third-party libraries used by these projects; I did not create them.

## Limitations

- A07 uses fixed rates supplied for the assignment, not current exchange rates.
- A11 retains the original release-year range of 1889–2024. Invalid numeric input or a movie ID that does not exist may stop the program.
- A05 uses the Windows `cls` command to clear the terminal; that command may produce an error on other operating systems.
- These are coursework examples and have not been comprehensively tested across operating systems or dependency versions.
