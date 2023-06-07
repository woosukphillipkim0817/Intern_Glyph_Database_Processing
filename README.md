# Intern_Glyph_Database_Processing

OVERVIEW
- Goal: processing a snapshot of Cloudlink's database for more effective data visualizations on Power BI
- Language and Library Used: Python, Pandas
- Modular Overview of Pipeline Implemented:
raw data extracts in CSV format --(Python scripts)--> processed data downloaded to local operating system in CSV format --(Power BI)--> visualized data for client

PROCESS Stage 1: experimenting with PowerBI and proposing a shift to using Python and the Pandas library
- initial work with PowerBI and research of its capabilities led me to realise the limitations of processing data using the built-in query editor as its inflexible data processing system was not suitable for the state of the raw data from the database
- proposed writing Python scripts to process the data first and then import that processed data into Power BI for visualisations (also in line with a supposed potential company-wide transition into more Python-oriented development)

Stage 2: writing Python scripts using the Pandas library to process the raw data
- Pandas is a dataframe-oriented library for the Python programming language for data manipulation and analysis. Dataframe-oriented means the library uses data structures and operators that can manipulate either tables containing various types and time series.
- Files without the FPBI label: these scripts read the CSV files extracted from the database and clean up the tables in order to get them ready for analysis. These scripts also perform the necessary merges (based on the ERD of Cloudlink's database) between data tables in order to match the details required when analyzing the data at certain scales. Comments have been made within the code in order to guide readers on the purpose of each code block and what it is analyzing within the ERD.
- Files with the FPBI label: these scripts take the semi-processed data from the scripts without the FPBI label (FPBI being a personal abbreviation of "For Power BI") and further process them into data tables that can be easily visualised on Power BI.

Reflection (things I believe that can be done to improve upon this pipeline, but were outside of my current skillset)
- scripts could be more efficient in terms of how they are taking in the raw data
