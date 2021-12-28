# surfs_up

## Analysis Overview
The purpose of this analysis is to determine if a desired location in Oahu, Hawaii for an icecream and surf shop called Surf n' Shake has ideal year-round weather conditions. We will analyze and review a dataset pertaining to the weather conditions of the area which has been stored in a SQLite database to provide critical and detailed information to convince an investor that opening up a Surf n' Shake shop in Oahu, Hawaii is a good business idea. The business plan is for this shop to sell surf boards and ice cream throughout the year, however, the investor is a bit hesitant because of a prior investment that was a similar concept with poor weather conditions. In order to convince our investor, we need to provide him with a statistical analysis on the weather conditions in Oahu, Hawaii that depicts how the location has ideal weather conditions for a successful icecream and surf shop  and convince him that this will be a successful investment.

We will explore the data in the SQLite database. In order to review the data in depth we used SQLAlchemy to connect and generate queries to pull the necessary information needed for our analysis. Jupiter notebook was used to import dependencies and create the commands to pull the data from the SQLite database.

## Results
- From our analysis of the dataset we were able to extract insights on the precipitation in the area over a one year timeframe. We reviewed the weather data from August 23, 2016 - August 23, 2017. Based on the Sumamry Statistics for precipitation, the average was ~18% based on 2,021 observations. We can infer that Oahu is mostly sunny throughout the day and experienced low rainfall.


  - Precipitation Summary Statistics:
  
  ![precipitation_summary_stats](https://github.com/Jflux05/surfs_up/blob/e3ba2a28d3443b677e2417f8219a9036137f3f13/Resources/precipitation%20summary%20stats.png)
  ![precipitation_bar_graph](https://github.com/Jflux05/surfs_up/blob/e3ba2a28d3443b677e2417f8219a9036137f3f13/Resources/precipitation%20bar%20graph.png)
  
  
 - In addition to looking at the annual precipitation levels, we looked at the number of weather stations that were actively collecting precipitation data and focused on one station that had the most observations recorded (station USC00519281 had 2,772 entries). We then used the information collected from this station to review the temperatures for the same time period. 
  - Our results showed: (and can be seen in the histogram below)
    - The average temperature throughout the year was 72°F 
    - A low temperature of 54°F 
    - A high temperature of 85°F

![12month_temp_observation_frequency](https://github.com/Jflux05/surfs_up/blob/e3ba2a28d3443b677e2417f8219a9036137f3f13/Resources/12month_temp_observation_frequency.png)


- Beyond our investors intial requests, we expanded our analysis to dive into observations recorded in the months of June and December regardless of year, the results showed:

  - The average temperature range is in the low 70's.
  - Both June and December showed similar min/max and average temperatures. 
  - The assumption is that the temperature does not have dramatic fluctuations throughout the year.

## Summary
From our analysis it is safe to say that the temperature of Oahu, Hawaii is relatively the same throughout the year and the chances of continuous rainfall is quite low. 

By creating two additional queries that gather the specific precipitation % in June and December we would have an even clearer picture of the weather conditions in Oahu, Hawaii in June or December. Utilizing the precipitation percentages and the average temperatures to derive valuable insights should prove to the investor that investing in Surf n' Shake is a good venture and that Oahu, Hawaii is the ideal location.



