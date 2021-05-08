from ics import Calendar, Event, Attendee


def readfile(filename):
    data = open(filename, 'rb')
    c = Calendar(data.read().decode())
    for _event in c.events:
        for _attendee in _event.attendees:
            print(str(_attendee.email))
        print(str(_event.organizer))
        print(str(_event.description))
        print(str(_event.created))
        print(str(_event.begin))
        print(str(_event.end))
        print(str(_event.location))
        print(str(_event.duration))
        print(str(_event.uid))

readfile("invite.ics")
