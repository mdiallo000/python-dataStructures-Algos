class Solution:
    # Description
    # Netflix maintains a popularity score for each of its titles. This popularity score is derived from customer feedback, likes, dislikes, etc. This score is updated weekly and added to the end of the list containing previous scores for the same title. This score list helps Netflix identify titles that may be increasing or decreasing in popularity over time. Some titles may be steady in popularity, increasing, decreasing, and fluctuating. We want to identify and separate a title if it is gaining or losing popularity.

    # We’ll be provided with a list of integers representing the popularity scores of a movie collected over a number of weeks. We need to identify only those titles that are either increasing or decreasing in popularity, so we can separate them from the fluctuating ones for better analysis.

    #  so the input for this problem is a list of ints. I will assume that that the numbers are all positive and non floating point values

    #  a sample test case [34, 45 ,12,20]
    #  re-reading the prompt we know that our goal is to identify the titles that either increasing or decreasing in popularity. I will make the assumption that this is hinting to the fact that if a value changes it will either go up or down, in that regard we can say that it has
