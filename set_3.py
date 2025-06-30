'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def following_var(from_member, to_member, social_graph):
        if to_member in social_graph[from_member]["following"]:
            return True
        else:
            return False
    following_status = following_var(from_member, to_member, social_graph)

    def follower_var(from_member, to_member, social_graph):
        if from_member in social_graph[to_member]["following"]:
            return True
        else:
            return False
    follower_status = follower_var(from_member, to_member, social_graph)
    
    if following_status and follower_status:
        return("friends")
    elif following_status:
        return("follower")
    elif follower_status:
        return("followed by")
    else:
        return("no relationship")

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)
    for row in board:
        row_symbol = row[0]
        if row_symbol != "" and row.count(row_symbol) == size:
            return row_symbol
    for col in range(size):
        column = []
        for row in range(size):
            column.append(board[row][col])
        col_symbol = column[0]
        if col_symbol != "" and column.count(col_symbol) == size:
            return col_symbol
    ngtv_diagl = []
    for i in range(size):
        ngtv_diagl.append(board[i][i])
    ngtv_symbol = ngtv_diagl[0]
    if ngtv_symbol != "" and ngtv_diagl.count(ngtv_symbol) == size:
        return ngtv_symbol
    pstv_diagl = []
    for i in range(size):
        pstv_diagl.append(board[i][size - 1 - i])
    pstv_symbol = pstv_diagl[0]
    if pstv_symbol != "" and pstv_diagl.count(pstv_symbol) == size:
        return pstv_symbol

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time_mins = 0
    in_stop = first_stop
    while in_stop != second_stop:
        leg = (in_stop, second_stop)
        if leg in route_map:
            total_time_mins += route_map[leg]["travel_time_mins"]
            in_stop = second_stop
        else:
            found_next_leg = False
            for (start, end), info in route_map.items():
                if start == in_stop:
                    total_time_mins += info["travel_time_mins"]
                    in_stop = end
                    found_next_leg = True
                    break
            if not found_next_leg:
                raise ValueError(f"Cannot find {in_stop} in route_map")
    return total_time_mins