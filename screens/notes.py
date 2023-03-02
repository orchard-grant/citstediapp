# Things that I learned this week
# Learned how to go in, copy the code from the other opening screens of the app, and was able to paste that on our login screen to make it look better.
# When we tried to logout the first time, it didn't work because it was trying to recall a funciton that didn't exist, so we have to code it with a function that does exist. However, you do lose your token that you created but you can't log out. We had to delete the token the token to be able to log out. If the token still exists, we cannot log out.
# Adding the session token keeps us logged in. When we first log in, it tries to find the token in storage. If not, it goes to the api to see if it is a good token. If it is good, we know that it's not expired, and it gets the information and gets us logged. 
# We have to add another screen. The token is getting deleted when we hit log out, but it is not logging out because it keeps us on the same screen, even though our token is deleted.


# Things that we did in class
# 1. We made the log in screen more usable, made it look better for the users. Also, we created a way to log out of the app, because before it wouldn't let us. We have a bunch of different javascript files, which all have different purposes. In class, we work together step by step through the code, and by updating the code we are updating the application. Logging in creates something called a token. That keeps our information in the system. We have to delete this token to be able to log out.