# Ticket Severity Forecasting
The solution provides 24 hours of future forecast of tickets of varying severity levels using historic data.

## Product Overview
Ticket Severity Forecasting helps businesses to predict the number of tickets of varying severity levels. This helps businesses assess the automation levels and human resources required to resolve the issues. It uses VAR algorithm which is useful in predicing multiple timeseries.

## Highlights
1. This solution will take in hourly data of tickets generated at different priority levels as input and provides 24 hours of future forecast.

2. This solution can be applied for forecasting number of ticket generated across varying priorities.

### Data Dictionary

- The input has to be a '.csv' file with 'utf-8' encoding. PLEASE NOTE: If your input .csv file is not 'utf-8' encoded, model   will not perform as expected
1. Have an unique identifier column called 'maskedsku'. eg. 'maskedsku' can be shipmentid
2. The date format of the columns should be: 'YYYY-MM-DD'