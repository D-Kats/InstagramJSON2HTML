# InstaJSON2HTML
A python script to parse the Instagram 'messages.json' file and create an HTML report with all the conversations of the account under examination. 

The InstagramJson2Html.exe is a small python tool that converts the "messages.json" file, downloaded by Instagram app when you retrieve a copy of your account and containing all the messages that have been exchanged on that particular Instagram account, to an HTML report.

## ACTIONS:
1. Download the exe file in a folder of your choice.

2. In this same folder copy the "messages.json" file and a jpg image file of your Department/Agency/Enterprise with name "department.jpg" (this is optional).

3. Run the exe file and give the Instagram name of the person under investigation (you can find the name in profile.json as the value for the "username" key).

4. The exe notifies you about the success and creates a report.html and a style.css file which are now ready to be added in your report with tables for each conversation, containing the sender, message and timestamp. 

## NOTES:
- User's account name should be passed into the entry box without the quotes "".

- Account under investigation messages are being highlightened with a light blue colour (the messages that the user sent to others).

- If you don't want to add an image of your Agency/Department/Enterprise then just delete line 9 of the created report.html file or modify the 'alt' attribute of the img tag accordingly.   
