from plyer import notification

i = 16
if i > 15:
    title = 'Warning!'
    message= 'Fraud has occured since i is greater than 15!' 
    notification.notify(title= title, message= message, app_icon = None, timeout= 10, toast=False)
else:
    exit()