# Trainee-Challenge
Project for the Trainee Challenge - LATAM Airlines

### Dataset
There are 22 columns for the dataset and corresponding column description are given below.  
    
1. Day of Month
2. Day of Week starting from Monday
3. Unique Carrier Code. 
4. An identification number assigned by US DOT to identify a unique airline (carrier). 
5. Code assigned by IATA and commonly used to identify a carrier. 
6. Tail Number
7. Flight Number
8. Origin Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport.
9. Origin Airport, Airport Sequence ID. 
10. Origin Airport
11. Destination Airport, Airport ID. An identification number assigned by US DOT to identify a unique airport.
12. Destination Airport, Airport Sequence ID. 
13. Destination Airport.
14. Actual Departure Time (local time: hhmm)
15. Departure Delay Indicator, 15 Minutes or More (1=Yes, 0=No)
16. Departure Time Block, Hourly Intervals
17. Actual Arrival Time (local time: hhmm)
18. Arrival Delay Indicator, 15 Minutes or More (1=Yes, 0=No)
19. Cancelled Flight Indicator (1=Yes, 0=No)
20. Diverted Flight Indicator (1=Yes, 0=No)
21. Distance between airports (miles)  
22. Unnamed: 21 - no description available  


# EDA
Performing Exploratory Data Analysis (EDA) helps to understand the main characteristics of a dataset. Here are several questions that might guide the EDA for the flight delay prediction problem:

1. **Univariate Analysis:**

   - How is the target variable (Departure Delay Indicator) distributed? What percentage of flights are delayed?
   - How are the numerical variables such as Day of Month, Day of Week, Distance between airports distributed?
   - What are the unique values for categorical variables like Unique Carrier Code, Origin Airport, Destination Airport, and Flight Number?
   - What are the top 10 carriers in terms of flight volume? The top 10 origin and destination airports?
   - How are departure times distributed throughout the day?

2. **Bivariate Analysis:**

   - How does the average departure delay change over days of the week/month? Are certain days more prone to delays?
   - What is the average departure delay for each carrier? Are there carriers that tend to have more delays than others?
   - What is the average departure delay for each origin and destination airport? Are there airports that tend to have more delays than others?
   - Is there a relationship between the distance of the flight and the departure delay?

3. **Multivariate Analysis:**

   - Do certain carriers have more delays at specific airports? Or on specific days?
   - Are there certain times of day when certain airports or carriers have more delays?
   - Are there certain flight numbers that are more prone to delays than others?

4. **Temporal Analysis:**

   - How does the number of delayed flights change over time? Are there certain months or seasons when delays are more common?
   - Is there any noticeable trend or pattern in the number of delays over time (increasing, decreasing)?

