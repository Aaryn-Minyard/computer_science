def get_season(month, day):
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    
    seasons = {
        'Spring': ((3, 20), (6, 20)),
        'Summer': ((6, 21), (9, 21)),
        'Autumn': ((9, 22), (12, 20)),
        'Winter': ((12, 21), (3, 19))
    }
    
   
    if month not in months:
        return 'Invalid'
    
    
    if day < 1 or day > 31:
        return 'Invalid'
    
    
    month_num = months[month]
    
    
    for season, ((start_month, start_day), (end_month, end_day)) in seasons.items():
        if (month_num > start_month or (month_num == start_month and day >= start_day)) and \
           (month_num < end_month or (month_num == end_month and day <= end_day)):
            return season
    
    
    if (month_num == 12 and day >= 21) or (month_num == 1 or month_num == 2) or (month_num == 3 and day <= 19):
        return 'Winter'
    
    return 'Invalid'


def input_dates():
    while True:
        input_month = input("Type Month:").strip()
        input_day = int(input("Type Day:").strip())
        return input_month,input_day

input_month, input_day = input_dates()


print(get_season(input_month, input_day))
