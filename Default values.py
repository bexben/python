def getGender(sex = 'Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)
    
getGender('m')
getGender('f')
getGender()