score = int(input('Please enter your score: '))

if score >= 80:
    gade ='A'
elif score < 80 and score >= 75:
    gade ='B+'
elif score < 75 and score >= 70:
    gade ='B'
elif score < 70 and score >= 65:
    gade ='C+'
elif score < 65 and score >= 60:
    gade ='C'
elif score < 60 and score >= 55:
    gade ='D+'
elif score < 55 and score >= 50:
    gade ='D'
elif score < 50:
    gade ='F'

print ("You got %s"%gade)