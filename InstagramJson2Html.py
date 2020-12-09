import json
from tkinter import *
from tkinter import messagebox


def exit():
    root.destroy()

def run():
    if entryName.get() == '':
        messagebox.showwarning('Warning', 'No name input was given! Is it a Monday morning? :P')
        root.mainloop()
    else:
        with open('messages.json', 'r', encoding='utf8') as fin:
            data = json.load(fin)
            if entryName.get() != data[0]['participants'][0] and entryName.get() != data[0]['participants'][1]:
                messagebox.showwarning('Warning', "This name is not the user's account! Go grab a cup of coffee :P")
                root.mainloop()
            else:
                with open('style.css', 'w', encoding= 'utf8') as cssout:
                    cssout.write('table{width: 75%;border-collapse:collapse;}\n th{text-align:left;background-color:#ddd;}\n table,th,td{border:1px solid #000;}')                
                with open('report.html', 'a', encoding='utf8') as fout:
                    fout.write('''<!DOCTYPE html>
                        <html>
                        <head>
                        <meta charset="utf-8" />
                        <title> Report </title>
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="stylesheet" type="text/css" media="screen" href="style.css" />
                        <body>
                        <img src="department.jpg" alt="Department or Agency name" style="width:164px;height:218px;"> ''')
                    for chat in data:
                        if chat['participants'][0] == entryName.get():
                            caption = chat['participants'][1]
                        else:
                            caption = chat['participants'][0]
                        fout.write('\n<table> \n <caption><h2><b> conversation with {}</b></h2></caption>'.format(caption))
                        fout.write('\n<tr> \n <th>sender</th> \n <th>message<th> \n <th>time</th>')
                        for messages in chat['conversation']:
                            if messages['sender'] == entryName.get():
                                if 'text' in messages:
                                    fout.write('\n<tr style="background-color:LightBlue"> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['text'],messages['created_at']))
                                elif 'video_call_action' in messages:
                                    fout.write('\n<tr style="background-color:LightBlue"> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['video_call_action'],messages['created_at']))
                                elif 'media' in messages:
                                    fout.write('\n<tr style="background-color:LightBlue"> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['media'],messages['created_at']))
                                elif 'media_share_url' in messages:
                                    fout.write('\n<tr style="background-color:LightBlue"> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['media_share_url'],messages['created_at']))
                                elif 'animated_media_images' in messages:
                                    fout.write('\n<tr style="background-color:LightBlue"> \n <td>{}</td> \n <td>animated media image - cannot be displayed<td> \n <td>{}</td>'.format(messages['sender'],messages['created_at']))
                            else:
                                if 'text' in messages:
                                    fout.write('\n<tr> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['text'],messages['created_at']))
                                elif 'video_call_action' in messages:
                                    fout.write('\n<tr> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['video_call_action'],messages['created_at']))
                                elif 'media' in messages:
                                    fout.write('\n<tr> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['media'],messages['created_at']))
                                elif 'media_share_url' in messages:
                                    fout.write('\n<tr> \n <td>{}</td> \n <td>{}<td> \n <td>{}</td>'.format(messages['sender'],messages['media_share_url'],messages['created_at']))
                                elif 'animated_media_images' in messages:
                                    fout.write('\n<tr> \n <td>{}</td> \n <td>animated media image - cannot be displayed<td> \n <td>{}</td>'.format(messages['sender'],messages['created_at']))

                    endHtml = '\n </body> \n </head> \n </html>'
                    fout.write(endHtml)
                messagebox.showinfo('successful run', 'Success! An html report with {} message tables was created.'.format(len(data)))
                root.destroy()
               

root = Tk()
root.title('INSTA MESSAGES TO HTML')
root.geometry('550x250')
# root.iconbitmap('app.ico')
root.config(bg= 'powder blue')
frame = Frame(root, bg='powder blue')
frame.pack()

lblTitle = Label(frame, text ='Run the program to get the html report from the Instagram JSON file', font=('arial', 12, 'bold'), bg='powder blue', fg='black')
lblTitle.grid(row=0, column=0, columnspan=2, pady=10)
#----------------------------------------------------------------------------------------------------------------------------------
MainFrame1= LabelFrame(frame, width=400, height=200, font=('arial',10, 'bold'), relief='ridge', bg='cadet blue', bd=10)
MainFrame1.grid(row=1, column=0)
#-----------------------------------------------------------------------------------------------------------------------------------
labelName = Label(MainFrame1, text='Give the name of the Instagram\n user account under investigation', width=25)
labelName.grid(row=2, column=0, pady=10)

entryName = Entry(MainFrame1, width=25)
entryName.grid(row=2, column=1, pady=10)
#-----------------------------------------------------------------------------------------------------------------------------------
btnRun = Button(MainFrame1, text='Run', width=25, command=run)
btnRun.grid(row=3, column=0, pady=10)

btnExit = Button(MainFrame1, text='Exit', width=25, command=exit)
btnExit.grid(row=3, column=1, pady=10)

emptylabel = Label(frame, text='------------------------------------------------------------------------', bg='powder blue', anchor=E)
emptylabel.grid(row=2,column=0)
poweredlabel = Label(frame, text='Created by DEE/ 7o  -DKats 2020', bg='powder blue', anchor=E)
poweredlabel.grid(row=3,column=0)


root.mainloop()