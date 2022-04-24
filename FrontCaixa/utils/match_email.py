from .string_strip import string_strip

def match_email(email,matchs=['@gmail.com','@hotmail.com']):
    email = string_strip(email)
    if email:
        for match in matchs:
            if match in email:
                return True,email
        else:
            return False,email
    else:
        return None,'email'
    