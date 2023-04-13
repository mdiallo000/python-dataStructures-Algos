class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class Solution:

    def __init__(self, homepage) -> None:
        self.browser = Node(homepage)
        self.curr = self.browser

    def visit(self, url):
        #  visiting a new site is essentially creating a new node and attaching it to the previous node
        page = Node(url)
        self.curr.next = page
        page.prev = self.curr
        self.curr = page

    def back(self, steps):

        #  we need to move back to our previous nodes however many times the steps integer would like
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps):
        #  same thing as the above needs to happen but this time we need to use the next attribute
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
