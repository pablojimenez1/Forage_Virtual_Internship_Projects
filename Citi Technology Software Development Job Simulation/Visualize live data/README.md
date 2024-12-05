# Here is the background information on your task
Your application that queries the Dow Jones Industrial Average stock price is working great! Now, your team lead would like you to make this application more accessible to the nontechnical employees at the company. They would like you to build a visual dashboard that displays the live stock data as it's queried. This visualization will make it even easier for internal employees at Citi to monitor risk in real-time.

With this visual dashboard, employees will eventually be able to view live stock data across multiple time periods, such as hourly, by day, and by month. For this first prototype, your team lead wants you to start small. All you need to do is create a line graph that contains a time tick on the x-axis and the stock price on the y-axis. This plot should update each time your application queries a stock price. On refresh, it should display all the currently stored stock prices.

Although this is a simple visualization tool, it will set the stage for building more robust visualization tools for internal employees at Citi! Your development team will be able to further build out this application to provide Citi employees with a diverse array of data visualization options. At the end of this task, you'll have an application that queries the Dow Jones Industrial Average stock price from Yahoo Finance every five seconds and then displays an updated line graph to the user.

# Here is your task
In this task, you'll update your existing application so that it displays a line graph that contains recorded stock prices every time Yahoo Finance is queried. Here are your instructions:

1. Ensure that you've completed all the steps included in Task 3. This includes installing the Gradle package and the Yahoo Finance API, as well as building an application that queries the Dow Jones Industrial Average stock price from Yahoo Finance every five seconds and then stores the data in a queue.

2. Update the gradle.build file in your package as described in the resource link **"Getting Started with JavaFX using Gradle".**

3. Update the App.java file for your existing application to add a feature that displays a line graph every time Yahoo Finance is queried. This line graph should have a time tick on the x-axis and the stock price on the y-axis. This plot should update each time your application queries a stock price. On refresh, it should display all the currently stored stock prices.

4. Compile your application by running the command "gradle build".

5. Run your application by running the command "gradle run".

6. Test your application and debug as needed.

When you're satisfied with your application, submit your App.java file below.
