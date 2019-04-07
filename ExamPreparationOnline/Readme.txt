
 Data analysis on 'Automatic email content store.csv' file.
	Validating Date Format:
 - Firstly all the Dates in 'Date' column of data are converted into valid format and the invalid date is removed from the column.
	
	Unique Email-ids:
 - 'unique()' method of pandas dataframe is used to obtain all the unique email addresses from the 'to' column of the data and 
	then the email addresses are stored in a list "unique".
 - 'sort()' method is used to sort all email adresses in alphabetical order.
	
	Last conversation date:
 - Then last_convo list is used to store the last date of conversation with each of the email addresses.
 - Then 'date()' method is used to remove time from the last_convo list and just keep the date.
	
	Time elapsed calculation:
 - 'time_elapsed_calculator' function is used to calculate the time elapsed between the last conversation date with each email and today.
 - Then the email and time elapsed since conversation with it is printed.
 
	Search keyword:
 - 'keyword' column is created with each entry in column initialized to "no keyword"
 - 'search()' function is used to search a keyword in 'raw' column.
 - The function stores the searched keyword in front of the row where it is found.
 - If more than one keyword is found in a row then they are stored with a comma between them. 