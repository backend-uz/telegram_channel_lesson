from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    msgs = data ['messages']
    month_post = 0
    for msg in msgs:
        day  = msg['date'].split('T')[0]
        current_mont = day.split('-')[1]

        if int(current_mont) == month:
            month_post += 1

    return month_post

print(get_post_month(fromJson('data/result.json'), 10))