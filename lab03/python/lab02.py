def calculator(hour,rate):
    if  hour <= 40:
        pay = hour*rate
        return f"{pay}"
        
    else:
        up_hour = hour - 40
        pay = (40*rate)+(up_hour*1.5*rate)
        return f"{pay}"

hour_work = int(input('How many hours did you work last week? :'))
rate_per_hour = int(input('What is yor pay rate per hour(between 10-25) :'))

print(calculator(hour_work,rate_per_hour))