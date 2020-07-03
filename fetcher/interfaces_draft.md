- Login controller
  - Responsible for managing user permissions, user authentication.
  - External
    - `get_permissions(userId)` ↦ permissions of that user
    - `authenticate(userId, password)` ↦ authenticate, return authentication token
    - `is_request_permitted(auth token, request)` ↦ check request is permitted
  - References
    - DB controller, user permissions table

- Visualization builder
  - Generally, the visualization builder returns output format
    suitable for passing to the client-side visualization library,
    such as json that can be interpreted by the client-side code to
    show the user a visualization
  - External:
    - `get_default_visualization(dataset)` ↦ return default visualization 
    - `get_visualization(dataset, type of visualisation)` ↦ return json for view controller to be able to plot
    - `get_available_visualizations(dataset)` ↦ return available visualization options
  - References:
    - DB controller, metadata of existing datasets

- Dashboard manager
  - Responsible for handling users' dashboards by the dashboards'individual tokens
  - External:
    - `get_dashboard(token)` ↦ get json for the client to display (interpreted by client-side code)
    - `change_dashboard_layout(token)` ↦ update user preference on dashboard layout
    - `add_visualization(token, visualization description)` ↦ add visualization to dashboard
    - `add_alert(token, alert rule)` ↦ add alert to dashboard
    - `get_active_alerts(token)` ↦ check if any alerts have fired relevant for this dashboard
    - `get_active_alerts_since_time(token, time)` ↦ check if any alerts have fired relevant for this dashboard since the given time
    - `create(token)` ↦ create a new dashboard for the user
    - `delete(token)` ↦ delete the given dashbaord
  - References:
    - DB controller, dashboard table, dashboards stored with tokens for id and json descriptions as above

- Correlation engine / Rule manager:
  - Responsible for data analytics and managing alert rules and triggers
  - External:
    - `get_all_active_rules(time)` ↦ get all rules that were active at the given time
    - `is_rule_active(time, rule)` ↦ check if rule is active at the given time
  - References:
    - data manager
    - user-defined and system-defined alert rules

- Predictions engine:
  - Responsible for predicting data into the future and filling in missing data
  - External:
    - `get_data_prediction(dataset name, date, function)` ↦ return the predicted
      data for the given dataset at the given date/time with the selected functin (linear, polynomyal). If time is in
      the future, this is prediction, otherwise it's filling in the missing data.
  - References:
    - data formatter
    - data manager

- External fetcher:
  - Responsible for dealing with requests for external data,
  - External:
    - `fetch_current_response(dataset)` ↦ get current API response, cache it, format data via Data Formatter, save to DB and return it
    - fail-over to a different server if one fails
  - References:
    - External client
    - Data Formatter
    - DB controller
    - Dataset metadata

- External client
  - Responsible for communicating with remote API for transportation statistics
  - External:
    - `fetch_response_async(API request, continuation)` ↦
      - validate request
      - determine proper remote server for request
      - send request
      - call continuation (asynchronously) with response when done      
    - `fetch_response(API request, continuation)` ↦ as above, but synchronous
  - References:
    - Dataset metadata

- Data formatter
  - Responsible for converting data in its native format to formats
    suitable for storing in the database
  - External:
    - `format_data(dataset, API response (json/csv/xml), format
       description)` ↦ return processed, formatted data
    - `format_data_for_visualization(dataset name, visualization
      request)` ↦ return data formatted in the right way for the given
      visualization request  --> ??? Should this be part of Visualisation Builder?
  - References:
    - hard-coded rules for how to format data in a suitable way

- Rule monitor (continuous process)
  - Responsible for continuous monitoring of rules and alerts,
    triggering actions when rules are fired.
  - External:
    - `run()` ↦ check rules at regular intervals
  - References:
    - Notification manager (calls it when rules are triggered)
    - Correlations engine / Rule manager
    - Notifications

- Notifications
  - Responsible for tracking and managing notifications.
  - External:
    - `notify_all_users(rule)` ↦ push notification/alert to the
      clients

- Data manager
  - Responsible for abstracting the sources and representations of
    data from the rest of the architecture, retrieving data for requests.
  - External:
    - `process_request(request)` ↦ forward request to the relevant
      data components
    - `is_data_available(dataset, time)` ↦ check if it is available?
    - `get_data(data, time interval)` ↦ return the requested data from
      the relevant data component (external/internal DB/computed) - this is probably more specific, i.e. getUserDashboardPreference,
      getBusData etc 
  - References
    - DB controller, data responses
    - External fetcher

- Main controller
  - The is the facade for the application. Co-ordinating between Data Manager, Visualisation Builder, View Controller, Notifications, Dashboard Manage, etc
  - External
    - `process_request(request)` ↦ forward request to relevant
      component (check authentication with login manager, pick the
      right component, forward the request, send the response back)
  - References:
    - Data Manager
    - Visualisation Builder
    - View Controller
    - Notifications
    - Dashboard Manager
    - Correlations Engine/ Rule Manager
    - Prediction Engine
    
- View Controller
  - The only component aware of html, css, javascript implementation for the pages. Takes JSON configuration for the pages and converts to browser code
  - External
    - has a method for each page that can be shown to the user
  
- DB controller
  - Responsible for abstracting the database implementation
  - External:
    - `get_data(data, time interval)` ↦ return the requested data from the database - this is probably many methods in practice, i.e.
      getUserDashboardPreference, getBusData etc 
    
    
