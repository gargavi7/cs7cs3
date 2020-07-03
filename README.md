# Technical Stack
![Technical stack](https://github.com/gargavi7/cs7cs3/blob/master/Tech%20stack.jpg)

# Technical Architecture
![Technical Architecture](https://github.com/gargavi7/cs7cs3/blob/master/techArchitecture.PNG)


# Use-Case Description
Develop a tool which would help the city planners to make decisions for local mobility services.
The user should have credentials to access the dashboard. After a successful login, the user will be redirected to the dashboard. 
The end-user can customize the dashboard according to the preferences. A higher-level abstraction is also possible when it comes to accessing the data, for e.g. city managers can have access to a wide range of data to take into account a variety of factors to support the final decision.
Push notifications/Alerts enable the user to get notified when there is an anomaly in the requested data which can be customized too.
Our system will be fault-tolerant, similar data can be fetched from multiple sources, for e.g. information about the Dublin bus can be provided by the Google Maps and Dublin Bus API itself. 
The user will select the dataset consecutively and then our system will be able to find the correlation in the selected data and provide visualizations to the decision-maker for e.g. congestion and quality of the air in the area.  
The data can be presented in various meaningful visualizations to the decision maker.  Also, the visualizations can be customized like selecting the frequency or range of data. The threshold can be set manually by dragging the bar in the graphs.
The problem of missing data can be addressed by applying various techniques like Real-time predictions using low-latency Predict API (Amazon ML). Also, based on historical data the predictions can be made to facilitate the decision-maker. 
The user will be provided with a high-level interpreted information using Artificial Intelligence models that would help in decision making. 
