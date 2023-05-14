class Solution:
    def checkRecord(self, s: str) -> bool:
        #  we get a string
        #  the string is composed of several Letters ALP each character represents the attendance status of the student on that day
        #  we return True if the student is eligibale of an attendance award or False is not
        #  we determine all of this based on the rules that has been given
        #  a student can only get an award if the fufill both criteria
        #  they can only have A <=2
        #  and an L for 3<=
        #  so now we have a general idea of the metrics we need to keep track of
        #  i am thinking of using two variables
        #  one for the total number of absences
        #  the other for the number of latenesses

        #  i will convert the string into a list of chars to iterate over them
