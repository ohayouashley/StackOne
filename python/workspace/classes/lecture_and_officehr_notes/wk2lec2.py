
#todo CREATING A DATABASE

#*Will download mysql and mysql workbench 
#todo Table tab
#*Most of the time first thing you're going to create is a user
#*First thing you need when you create a user is an id. PK NN AI checked
#*Now we need first_name| las_name| and created_at updated_at
#* datatypes need to be changed to date time of they're dates and VARCHAR(45) IF THEY'RE variable
#*if you're doing a birthday make sure to pick DATE datatype. KEEP IN BACK POCKET FOR EXAM
#* created_at under default/expression put NOW() <----make sure always there
#* updated_at NOW() ON UPDATE NOW() <-- make sure always there (just more chances for error if you don't. Not catastrophic)

#?Relationships - one table can connect to another table. What is the relationship between user and book (bookclub) we're thinking about
#? database design. 

#todo columns tab

#* create id PK NN AI INT
#* date_of_thought DATE
#*my_thought TEXT
#*created_at DATETIME NOW()
#* updated_at DATETIME NOW() ON UPDATE NOW()

#todo USER to Thoughts
#* connect users to thoughts 
#!this is going to be on the exam in order to bass you need to create a mini to _____ 
# !1 - mini like this you'll have to associate them, add they're data type based on the wire diagram for the exam.
#* do many to many so that we can have mult mini to mini relationship .
#*users need separate entries in the database just in case someone moves out. Just because they hold the same data
#*doesn't mean they need to hold the same data in the database. 
#! requirements of the app - some companies only allow one thing per household (or one address per user) 
#!amazon you can have many addresses 1- many relationship but DMV you an have only 1 address 1-1 relationship

#*create a new addresses table column tab
#* do id city street_name, city_name, street_number 
#* create a separate list of states or countries that way we're not duplicated data. 
#* mysql work bench created all the code that we' would have needed 
#* read the error message go back try to fix it and if you dont' get it reach out. 
#* now his schows_schema - there won't be anything in it 

#! after you finish your data base, you need to save model as: save this in the same folder  as your assignment. If you
#!go back to make changes, SAVE THEM in the file with your assignment. Otherwise I'll get you old prd and SAVE EVERY TIME YOU EDIT
#! OR UPDATE YOUR ERD 

#*What can I do without this file? NOTHING

#? 8.9.85

#* NOTE ON mysql editor it's not great.

#? Point out a primary key - user id INT is the primary key
#? pink little one means it's associated with with a foreign table. 
#?Good way to see what you need is to refer to the form, that way you can figure out what you need for your user database. 
#? read the connection file so you can see what it returns to you and why. Especially when you get those comments don't chnage the 
#?file at all. Data in use cannot be encrypted data in storage can be encrypted. Our use is also going to be arbitrary anyway. 