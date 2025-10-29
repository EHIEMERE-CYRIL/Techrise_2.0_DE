def validate_password(password):

    #check for minimum length
    if len(password) < 8:
        return False
        

    lowercase = False
    uppercase = False
    digit = False
  
    
    #check for atleast one uppercase
    #check for lowercase
    #check for atleast one digit

        
    for character in password:
        if character.isupper(): 
            present_uppercase = True
        elif character.islower():
            present_lowercase = True
        elif character.isdigit():
            present_digit = True

    return present_uppercase and present_lowercase and present_digit





    
    
    
    

