# Here is the background information on your task
Your team lead appreciated your proposal for credit risk modeling, and they have shared it with the relevant stakeholders at the company. While you wait for feedback, your team lead has a new task for you. So far, you've primarily worked with loan management services at the company. However, as an intern at Citi, that's not the only department you'll work with! For your next task, your team lead would like you to develop another tool for risk assessment.

You've learned about the importance of risk assessment in finance, but it isn't always enough to check risk just once. When it comes to the stock market, things are constantly changing! This means that employees constantly need fresh data in order to make the most up-to-date decisions. 

This is where you come in! Your team lead has asked you to build an internal tool to assist employees in monitoring the stock market in real time. The tool should be able to retrieve live stock data from a reliable source and store it in a database for easy access. This tool is essential for employees at Citi, who need up-to-date information to ensure they're making informed decisions with regard to risk management.

At the end of this task, you'll have an application that queries the Dow Jones Industrial Average stock price from Yahoo Finance every five seconds and stores the stock value and timestamp in a queue. 


# Here is your task
In this task, you'll build an application that queries the Dow Jones Industrial Average stock price from Yahoo Finance every five seconds and stores the stock value and timestamp in a queue. Here are your instructions:

1. Start by installing the Gradle package manager, linked in the Resources section below.

2. Install an application programming interface (API) of your choice for querying stock prices. We recommend the Yahoo Finance API, linked in the Resources section below.

3. Create a new folder for your application. Navigate to this folder in the terminal and run the command "gradle init" to create a new Java application. You'll be prompted through a series of selections to generate your project. When asked about the type of project to generate, select “Application”, and for the implementation language, select “Java.” For all other prompts, we suggest the default option. For example, we created our application using the following responses:

  a. Select type of project to generate: Application

  b. Select implementation language: Java

  c. Split functionality across multiple subprojects: No — Only one application project

  d. Select build script DSL: GroovyGenerate build using new APIs and behavior (some features may change in the next minor release)? No

  e. Select test framework: JUnit Jupiter

4. Locate the gradle.build file in your project. This will be found in the app directory, located in the root of your project. Update the gradle.build file to include the dependency for the Yahoo Finance API:

dependencies {
implementation group: 'com.yahoofinance-api', name: 'YahooFinanceAPI', version: '3.17.0'
}

5. Locate the AppTest.java file in your project. This will be found in the directory app/src/test/java/project_name. Remove the default tests from the AppTest.java file so that your changes will compile. Feel free to add your own tests if you'd like!

6. Locate the App.java file in your project. This will be found in the directory app/src/main/java/project_name. Update the App.java file to create an application that queries the Dow Jones Industrial Average stock price from Yahoo Finance every five seconds and stores the stock value and timestamp in a queue.

7. Compile your application by running the command "gradle build".

8. Run your application by running the command "gradle run".

9. Test your application and debug as needed.

**When you're satisfied with your application, submit your App.java file below.**
