## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- see ya

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- okay

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

<!-- Misc -->
## intent:inform
- [Simple](room_type)
- [Deluxe](room_type)
- [simple](room_type)
- [deluxe](room_type)
- [1](num_rooms)
- [2](num_rooms)
- [10](num_rooms)
- [6](num_rooms)
- [now](clean_now)
- [right now](clean_now)
- [soon](clean_now)
- [as soon as possible](clean_now)
- [asap](clean_now)
- [10 AM](clean_later)
- [5 P.M.](clean_later)
- [6:30 P.M](clean_later)
- [8 pm](clean_later)
- [11 am](clean_later)
- [after 2 hours](clean_later_descriptive)
- [after half an hour](clean_later_descriptive)
- [later](clean_later_descriptive)
- [evening](clean_later_descriptive)


<!-- Room Booking -->
## intent:book_room
- I want to book a room
- book a room for my stay
- can I book a [simple](room_type) room?
- can I get a room?
- can you book a room for me?
- I would like to book [3](num_rooms) [Deluxe](room_type) rooms
- I would like to book [Simple](room_type) rooms for [4](num_rooms) people
- I want to book [2](num_rooms) rooms

<!-- Room Cleaning -->
## intent:clean_room
- I want to have my room cleaned
- could you send someone to clean my room [asap](clean_now)?
- clean the room [right now](clean_now)
- I need room cleaning
- can you send room service?
- can someone clean my room tonight?
- can someone clean my room at [9 PM](clean_later) tonight?
- I want to have my room cleaned [later](clean_later_descriptive) tonight
- can someone clean my room in the [evening](clean_later_descriptive)?

<!-- FAQs -->
## intent:faq/check_in_timings
- what are your check-in timings?
- can I get the check-in details?
- can I get the check in  timing details?
- could you tell me the check in procedure?
- what do I need to know about check-in?
- what is the minimum age for checking in?
- can you tell me about your check in policy?

## intent:faq/check_out_timings
- what are your check-out timings?
- can I get the check out details?
- can I get the check-out timing details?
- could you tell me the check out procedure?
- what do I need to know about check out?
- can you tell me about your check out policy?

## intent:faq/cancel_reservation
- how do I cancel a reservation?
- what is the cancellation procedure?
- can I cancel my reservation?
- cancel my reservation
- can I know the process to cancel my reservation?
- how to cancel room booking?

## intent:faq/cancellation_policy
- what is your cancellation policy?
- can you explain the cancellation policy?
- what all do I need to keep in mind while cancellation?
- is the booking deposit refunded on cancellation?
- can I get details about your cancellation policy?

## intent:faq/restaurant
- does the hotel have a restaurant?
- is there a restaurant?
- where can we have lunch?
- does the hotel have a restaurant to have dinner?
- can you share the restaurant details with me?
- does the restaurant have a bar?

## intent:faq/breakfast_availibility
- does the hotel offer breakfast?
- is breakfast available?
- do you provide breakfast?
- is the breakfast free?
- how does the breakfast facility work?

## intent:faq/breakfast_timings
- what are the breakfast timings?
- till what time do you serve breakfast?
- when is the breakfast served?

## intent:faq/restaurant_timings
- what are the timings of your restaurant?
- what are the restaurant timings?
- till when is the restaurant open?
- till what time will the restaurant serve?