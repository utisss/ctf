# It's Password Time
# Difficulty: Easy/Medium

This challenge is a remote timing challenge. Using browser devtools, we can 
discover that the timing in which the /checkPassword endpoint returns is 
dependent on the number of correct characters in our guess.

From there, we can guess the first character by trying every possible 
character and keeping the one that takes the longest amount of time for the
server to process, then guess the second character, etc.