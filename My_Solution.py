#a function for opening the file we want to review taking in the "day" number associated with the file
def open_file(day):
    '''This function takes in the day correlated to the delivery file day
    and returns the correct file name to open. This will only work if the file names of delivery logs
    are consistent with the current formatting'''
    #change the int input from user to a string
    day = str(day)
    #use an f string to allow the correct file name to be opened and returned
    return open(f"um-deliveries-day-{day}.txt")

#a function that will take 1 parameter - the day number referenced in the file name
def produce_summary_report(date):
    #call the open_file function to get the correct file open referencing the day we are reviewing
    daily_log = open_file(date)
    """This function will allow us to input the daily delivery log and date in which 
    we would like to see a full daily deliveries report and will return to us a printed line by line 
    log formatted in an easy to read layout showing the amount and type of melons delivered 
    and the total $ of the delivery."""

    #Print out the date or day of daily delivery log we are referencing
    print(f"Day: {date}")
    #initialize a loop to read the delivery file line by line
    for line in daily_log: 
        #remove any trailing whitespace from lines so we are only getting text
        line = line.rstrip()
        #split the line into words (will return a new list = words) 
        #and use the "|" symbol to dictate where to split the lines
        words = line.split('|')

        #assign the approriate reference names as variables to 
        # the corresponding value in the words list
        melon, count, amount = words

        #print the requested format to review each delivery for the specified day line by line
        print(f"Delivered {count} {melon}s for total of ${amount}")
    #add an empy print space in case of reviewing one file after the other. Eases readability
    print()
    #close the file we opened once we have received the line by line output from the current file
    daily_log.close()

#function call for existing reports
produce_summary_report(date = 1)
produce_summary_report(date = 2)
produce_summary_report(date = 3)