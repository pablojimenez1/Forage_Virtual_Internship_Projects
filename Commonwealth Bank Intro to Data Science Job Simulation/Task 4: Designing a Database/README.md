# Here is the background information on your task
In the previous task, you learnt the benefits of unstructured data! Now, you need to determine how this information can be structured for storage in a database. 

To design a database, we first need to understand the principles of what makes a suitable database! A database should limit duplicate information since redundant data takes additional memory and provides opportunities for inconsistent data. Additionally, the data and the relationships between them should be as complete as possible and, most importantly, correct.

Microsoft’s database design basics suggest that an effective database should adhere to the following guidelines:

Divides your information into subject-based tables to reduce redundant data.
Provides Access with the information it requires to join the information in the tables together as needed.
Helps support and ensure the accuracy and integrity of your information.
Accommodates your data processing and reporting needs.
With those guidelines in mind, you’re ready to get started planning a database design for InsightSpark!

# Here is your task
Your task is to propose a database structure that allows us to store tweets from the CommBank Twitter account, as well as user replies, user quote retweets, and direct mentions.

To design a database that stores this information, start by reviewing the resources below. Then, walk through the steps covered in Microsoft’s <ins>“Database Design Basics”</ins> to design a database that stores tweet data.

1. Start by determining the specific fields to include in your tables. A bank’s database, for example, might include information like account numbers, transaction dates, and transaction amounts.
2. Divide your information into separate tables. For a bank, one table might focus on Customers, while another focused on Transactions.
3. Decide which items will be stored in each table. Each item will be a column in the table. For example, a Customers table might include items like name, address, and customer ID.
4. Decide on each table’s primary key. This is the column that uniquely identifies each row. For a Customers table, the primary key might be the customer ID.
5. Define table relationships to show how one table is linked to another, and add fields if necessary. For example, a Transaction table might contain a customer ID for each row, which can then be linked back to the Customer table.

Once you’re happy with your database structure, complete the text submission below. Your submission should include the following:

- The list of tables to include in your data set.
- The items to include in each data set. This should include a variable name and a brief description of each field.
- The primary key for each data set.
- The relationships between your tables.
