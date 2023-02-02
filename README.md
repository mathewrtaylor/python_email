# python_email
A Class method to email. Meant to demonstrate an understading of the DRY method.<br>

## Prerequisite(s)
- I've made an assumption that you have an email address and access to SMTP server.  
- There is also an assumption that you have an environment file (.env) in the same working directory

## Installation
Clone to the directory of choice, then import for usage in your scripts.

## Usage Example
```bash
Args:
        emailto: Intended recipient list; emails separated by comma
        emailsubject: Subject of your email
        emailbody: The body of your email 
        mail_attachment: The file that you are attaching (optional)
        mail_attachment_name: The name of the file that you are attaching (optional)
        emaillcc: Intended cc recipient list; emails separated by comma (optional)
        mimemsg: The actual message. email method cares for creation of this object
        success: P / F . P indicates a Pass, F a Failure. Intended for auto generated emails
                 Failure will provide a date time stamp with an attachment. (optional)

    Usage:
        Instantiate the message object, then email() it.
    
    Example:
        message_example = Message('John.Doe@Example.com','Test','This is a test email.')
        message_example.email()
```

## Credits
Tutorials from:<br>
Python Simplified - https://www.youtube.com/@PythonSimplified<br>
and <br>
Tutorials from Corey Schafer - https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc<br>

## License
[MIT](https://choosealicense.com/licenses/mit/)
