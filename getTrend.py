from pytrends.request import TrendReq

# Initialize a new Google Trends Request Object
pt = TrendReq(hl='en-US', tz=360)

# Set the keyword and timeframe
kw = "python"
timeframe = "today 12-m"

# Get the interest over time data
data = pt.interest_over_time(kw, timeframe)

# Print the data
print(data)