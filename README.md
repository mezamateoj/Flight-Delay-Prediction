# Trainee-Challenge
Project for the Trainee Challenge - LATAM Airlines by Mateo Meza

### Data

The data can be found on kaggle:
* source: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv

### Predicting flight delays can contribute to the reduction of carbon emissions.

Aircraft burn fuel during all phases of a flight - taxiing, takeoff, cruising, and landing. However, certain phases like taxiing and takeoff are particularly fuel-intensive. When a flight is delayed, aircraft often spend extra time in these fuel-intensive phases. For example, an aircraft might need to taxi for a longer time or might need to wait on the runway with its engines running. This extra time burns additional fuel, leading to increased carbon emissions.

* By accurately predicting flight delays, an airline like LATAM can take proactive measures to minimize the extra fuel burn and thus reduce carbon emissions. Here are a few examples:

1. **Optimized Scheduling**: If a delay is predicted due to factors like bad weather or air traffic congestion, the airline could reschedule the flight to a time when such issues are not expected. This would help avoid long waiting times on the runway or in the air, reducing unnecessary fuel burn.

2. **Improved Resource Allocation**: If a delay is expected due to operational issues like aircraft maintenance or crew availability, the airline could reallocate resources to prevent the delay. For example, if maintenance is expected to take longer than usual, a backup aircraft could be prepared. This would prevent the aircraft from having to wait for extended periods with its engines running.

3. **Enhanced Route Planning**: If a delay is predicted due to air traffic, the airline could adjust the flight path to avoid congested areas. This would help reduce the time the aircraft spends in holding patterns, which are fuel-intensive.

4. **Passenger Communication**: If a delay is unavoidable, the airline could inform passengers in advance. This would reduce the time passengers spend on the aircraft while it's not moving, which in turn could reduce the use of auxiliary power units (which provide power to the aircraft on the ground and also burn fuel).

In summary, by predicting and proactively managing flight delays, an airline can significantly reduce unnecessary fuel burn and thus lower its carbon emissions. This not only contributes to the airline's sustainability goals but also can result in cost savings and improved passenger satisfaction.

### Dataset
* Original Dataset can be found in the datasets folder => archive.zip
* There are 21 columns for the dataset and corresponding column description are given below.  
    
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