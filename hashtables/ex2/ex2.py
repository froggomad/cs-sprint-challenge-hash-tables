#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

tickets = [
    Ticket(source="PIT", destination="ORD"),
    Ticket(source="XNA", destination="CID"),
    Ticket(source="SFO", destination="BHM"),
    Ticket(source="FLG", destination="XNA"),
    Ticket(source="NONE", destination="LAX"),
    Ticket(source="LAX", destination="SFO"),
    Ticket(source="CID", destination="SLC"),
    Ticket(source="ORD", destination="NONE"),
    Ticket(source="SLC", destination="PIT"),
    Ticket(source="BHM", destination="FLG")
]

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    stops = {}
    route = []
    for ticket in tickets:
        stops[ticket.source] = ticket.destination

    source = stops["NONE"]
    route.append(source)
    for i in range(len(stops)):
        if i != 0:
            route.append(stops[route[i-1]])    

    print(route)

    return route

reconstruct_trip(tickets, len(tickets))