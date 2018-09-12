# Jimmy Wrangler, Data Explorer

It is a Data Science Project.


# What it Does?

  - It combines two datasets and gives some information
  - It visualizes the information in form of a graph.
# Datset Used
- Titanic Passenger Details : https://www.kaggle.com/c/titanic
-- It contains details related to 1309 passengers - Name, Age, Sex, Survived or Deceased etc.,
- Mortality Data - https://www.statista.com/statistics/241572/death-rate-by-age-and-sex-in-the-us/
-- It contains death rate by age and sex.

# Data Transformation
##### Titanic:
- Titanic Passenger details is first read from the data files.
- Converted the Passenger details into age groups and then **pivoted** the data
- Grouped data interms of Age and Gender.
##### Mortality:
- Retrieved data from csv
- Loaded into DataFrames.
##### Merge:
- Both the data sets are merged using the common key **Age Group**

# Analysis:
- After combining both the data, created **Death rate** for both Titanic and Mortality 
- Below graph shows the Mortality rate of **Average Humans in US VS Passengers in Titanic**
-![](https://raw.githubusercontent.com/nareshkumar66675/Wrangler/master/reports/AvgVsTitanic.png)

- Below table shows the merged results from both the datasets.

|          | female | male | Male   | Female | ag       | Avg Mortality Rate - Male | Titanic Mortality Rate - Male | Avg Mortality Rate - Female | Titanic Mortality Rate - Female |
|----------|--------|------|--------|--------|----------|---------------------------|-------------------------------|-----------------------------|---------------------------------|
| Age      |        |      |        |        |          |                           |                               |                             |                                 |
| (1, 4]   | 5.0    | 6.0  | 28.0   | 21.6   | (1, 4]   | 0.000280                  | 0.004584                      | 0.00216                     | 0.003820                        |
| (4, 9]   | 6.0    | 5.0  | 13.2   | 10.2   | (4, 9]   | 0.000132                  | 0.003820                      | 0.00102                     | 0.004584                        |
| (9, 14]  | 3.0    | 5.0  | 16.9   | 12.2   | (9, 14]  | 0.000169                  | 0.003820                      | 0.00122                     | 0.002292                        |
| (14, 19] | 8.0    | 45.0 | 66.6   | 29.1   | (14, 19] | 0.000666                  | 0.034377                      | 0.00291                     | 0.006112                        |
| (19, 24] | 10.0   | 64.0 | 129.9  | 46.5   | (19, 24] | 0.001299                  | 0.048892                      | 0.00465                     | 0.007639                        |
| (24, 29] | 10.0   | 59.0 | 150.5  | 60.8   | (24, 29] | 0.001505                  | 0.045073                      | 0.00608                     | 0.007639                        |
| (29, 34] | 6.0    | 48.0 | 170.9  | 83.5   | (29, 34] | 0.001709                  | 0.036669                      | 0.00835                     | 0.004584                        |
| (34, 39] | 4.0    | 36.0 | 198.5  | 110.1  | (34, 39] | 0.001985                  | 0.027502                      | 0.01101                     | 0.003056                        |
| (39, 44] | 5.0    | 25.0 | 254.0  | 159.0  | (39, 44] | 0.002540                  | 0.019099                      | 0.01590                     | 0.003820                        |
| (44, 49] | 5.0    | 20.0 | 375.5  | 243.1  | (44, 49] | 0.003755                  | 0.015279                      | 0.02431                     | 0.003820                        |
| (49, 54] | 1.0    | 17.0 | 608.7  | 381.5  | (49, 54] | 0.006087                  | 0.012987                      | 0.03815                     | 0.000764                        |
| (54, 59] | 1.0    | 9.0  | 916.9  | 556.8  | (54, 59] | 0.009169                  | 0.006875                      | 0.05568                     | 0.000764                        |
| (59, 64] | NaN    | 9.0  | 1321.2 | 781.1  | (59, 64] | 0.013212                  | 0.006875                      | 0.07811                     | NaN                             |
| (64, 69] | NaN    | 4.0  | 1811.8 | 1155.1 | (64, 69] | 0.018118                  | 0.003056                      | 0.11551                     | NaN                             |
| (69, 74] | NaN    | 6.0  | 2732.5 | 1855.8 | (69, 74] | 0.027325                  | 0.004584                      | 0.18558                     | NaN                             |




# Project Struture

##### Src
- Wrangler.py - python file exported from Jupyter
##### Notebooks
- Wrangler.ipynb - Jupyter notebook
##### Data
- External - Titanic & Mortality Data
##### Reports
- Html Table - Merged Final results
- Plot - Average vs Titanic Mortality


  
