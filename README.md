# imagereader
RSS images parser

# Task description:
- support of user registration (by e-mail)
- after registration, the user can add the sites he needs (or RSS - choose what is easier to implement) into his “subscription”
 - when a user selects one of his sites from the “Subscriptions” list, the latest pictures / photos from publications are displayed in the “feed” starting from the current ones and winding back to the moment when the site was added to the subscription.
 
 
# Thus, Python code will
- generate a page returned from the server to the user,
- work with data in the database (registration and saved url for images)
- according to the schedule (once a day for example), bypass the sites from the Subscription to save new published pictures in the database (only links)
