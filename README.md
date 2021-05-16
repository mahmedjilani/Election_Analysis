# Election Audit with Python
---
## Overview of Election Audit
The purpose of this project is to conduct an election audit of different counties. The project comprises of the following tasks. 

1. Calculation of the total number of the votes casted. 
2. List of candidates who received votes.
3. Calculation of the total number of votes each candidate received.
4. Calculation of the percentage of votes for the candidate who won.
5. Determine the winner of the election.

### Data Set
The data is given in the form of the flat file (CSV File) which consists of Ballot ID, County & Candidate Name.

## Election Audit Results
~~~
Election Results
-------------------------
Total Votes: 369,711
-------------------------

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

----------------------------------------
Largest County Turnout: Denver
----------------------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
~~~

**Summary:**
1. The Denver countrt the most voetes 82.8%
2. Diana DeGette won the election and secured 78.3% votes.

## Election Audit Summary
The code can be modified to find the most number of the votes for different filters other than the candidates and county. If the data included other characterstics, such as demographics and geography, the scripts can be modified to include these characterstics and the analysis can be done likewise.

The code can also be modified to determine the patterns among the characterstics. Moroever, we can also test the percentage of voters by county against the each candidate. This would enable us to see which candidate was the most popular with the county or the geographical area.
