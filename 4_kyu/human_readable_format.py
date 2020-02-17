# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, 
# in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". 
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

#The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid 
# units of time, separated by a space.The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", 
# just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, 
# but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, 
# but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 
# 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


def format_duration(seconds):
    if not seconds:
        return "now"
    else:
        y,d,h,m,s = " year", " day", " hour"," minute", " second"
        data,response = [], ""
        years,days,hours,minutes = 0,0,0,0
        
        while seconds >= 60: 
            minutes += 1
            seconds -= 60
        
        while minutes >= 60:
            hours += 1
            minutes -= 60
        
        while hours >= 24:
            days += 1
            hours -= 24
        
        while days >= 365:
            years += 1
            days -= 365
        
        if years > 1: 
            y += 's'
            data.append(str(years)+y)
            
        if years == 1:
            data.append(str(years)+y)   
            
        if days > 1:
            d += 's'
            data.append(str(days)+d)
            
        if days == 1:
            data.append(str(days)+d)
            
        if hours> 1:
            h += 's'
            data.append(str(hours)+h)
            
        if hours == 1:
            data.append(str(hours)+h)
            
        if minutes > 1:
            m += 's'
            data.append(str(minutes)+m)
        
        if minutes == 1:
            data.append(str(minutes)+m)
        
        if seconds > 1:
            s += 's'
            data.append(str(seconds)+s)
            
        if seconds == 1:
            data.append(str(seconds)+s)
            
        if len(data) == 1:
            response += data[0]
            return response
        
        for i in range(len(data)):
            if i == len(data)-1:
                response += ' and ' + data[i]
            elif i == 0:
                response +=  data[i]
            else:
                response += ', ' + data[i]
        return response
