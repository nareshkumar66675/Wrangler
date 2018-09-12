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

|  | female | male | Age | Male | Female | Avg Mortality Rate - Male | Titanic Mortality Rate - Male | Avg Mortality Rate - Female | Titanic Mortality Rate - Female |
|----|--------|------|----------|--------|--------|---------------------------|-------------------------------|-----------------------------|---------------------------------|
| 0 | 5.0 | 6.0 | (1, 4] | 28.0 | 21.6 | 0.027999999999999997 | 0.6734006734006733 | 0.216 | 0.5611672278338945 |
| 1 | 6.0 | 5.0 | (4, 9] | 13.2 | 10.2 | 0.013199999999999998 | 0.5611672278338945 | 0.10199999999999998 | 0.6734006734006733 |
| 2 | 3.0 | 5.0 | (9, 14] | 16.9 | 12.2 | 0.0169 | 0.5611672278338945 | 0.122 | 0.33670033670033667 |
| 3 | 8.0 | 45.0 | (14, 19] | 66.6 | 29.1 | 0.06659999999999999 | 5.05050505050505 | 0.29100000000000004 | 0.8978675645342313 |
| 4 | 10.0 | 64.0 | (19, 24] | 129.9 | 46.5 | 0.12990000000000002 | 7.182940516273851 | 0.46499999999999997 | 1.122334455667789 |
| 5 | 10.0 | 59.0 | (24, 29] | 150.5 | 60.8 | 0.1505 | 6.621773288439956 | 0.608 | 1.122334455667789 |
| 6 | 6.0 | 48.0 | (29, 34] | 170.9 | 83.5 | 0.1709 | 5.387205387205387 | 0.835 | 0.6734006734006733 |
| 7 | 4.0 | 36.0 | (34, 39] | 198.5 | 110.1 | 0.19849999999999998 | 4.040404040404041 | 1.101 | 0.44893378226711567 |
| 8 | 5.0 | 25.0 | (39, 44] | 254.0 | 159.0 | 0.254 | 2.8058361391694726 | 1.59 | 0.5611672278338945 |
| 9 | 5.0 | 20.0 | (44, 49] | 375.5 | 243.1 | 0.3755 | 2.244668911335578 | 2.431 | 0.5611672278338945 |
| 10 | 1.0 | 17.0 | (49, 54] | 608.7 | 381.5 | 0.6087 | 1.9079685746352413 | 3.8150000000000004 | 0.11223344556677892 |
| 11 | 1.0 | 9.0 | (54, 59] | 916.9 | 556.8 | 0.9169 | 1.0101010101010102 | 5.568 | 0.11223344556677892 |
| 12 |  | 9.0 | (59, 64] | 1321.2 | 781.1 | 1.3212 | 1.0101010101010102 | 7.811 |  |
| 13 |  | 4.0 | (64, 69] | 1811.8 | 1155.1 | 1.8117999999999999 | 0.44893378226711567 | 11.550999999999998 |  |
| 14 |  | 6.0 | (69, 74] | 2732.5 | 1855.8 | 2.7325 | 0.6734006734006733 | 18.558 |  |


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


  
