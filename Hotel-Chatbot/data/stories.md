## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

<!-- Room Booking -->
## book room
* book_room{"num_rooms":"3", "room_type":"Simple"}
  - utter_room_confirm

## book room + ask num rooms
* book_room{"room_type":"Deluxe"}
  - utter_how_many
* inform{"num_rooms":"2"}
  - utter_room_confirm

## book room + ask room type
* book_room{"num_rooms":"2"}
  - utter_which_room
* inform{"room_type":"Deluxe"}
  - utter_room_confirm

## book room + ask num rooms + ask room type
* book_room
  - utter_how_many
* inform{"num_rooms":"2"}
  - utter_which_room
* inform{"room_type":"Deluxe"}
  - utter_room_confirm

<!-- Room Cleaning -->
## room clean now
* clean_room{"clean_now":"asap"}
  - utter_clean_confirm_now

## room clean later
* clean_room{"clean_later":"6 PM"}
  - utter_clean_confirm_later

## room clean + ask time + now
* clean_room
  - utter_what_time
* inform{"clean_now":"now"}
  - utter_clean_confirm_now

## room clean + ask time + later
* clean_room
  - utter_what_time
* inform{"clean_time":"5 PM"}
  - utter_clean_confirm_later

## room clean descriptive + ask if time fine + affirm
* clean_room{"clean_later_descriptive":"after 3 hours"}
  - utter_is_time_fine
* affirm
  - utter_clean_confirm_later_2

## room clean descriptive + ask if time fine + deny
* clean_room{"clean_later_descriptive":"after 4 hours"}
  - utter_is_time_fine
* deny
  - utter_what_time
* inform{"clean_time":"5 PM"}
  - utter_clean_confirm_later

<!-- FAQs -->
## faq
* faq
  - respond_faq

<!-- Misc -->
## book room + ask num rooms + faq
* book_room{"room_type":"Deluxe"}
  - utter_how_many
* faq
  - respond_faq
  - utter_how_many
* inform{"num_rooms":"2"}
  - utter_room_confirm

## room clean + ask time + faq
* clean_room
  - utter_what_time
* faq
  - respond_faq
  - utter_what_time
* inform{"clean_time":"now"}
  - utter_clean_confirm_now

## room clean + ask time + faq 2
* clean_room{"clean_later_descriptive":"after 3 hours"}
  - utter_is_time_fine
* faq
  - respond_faq
  - utter_is_time_fine
* affirm
  - utter_clean_confirm_later_2

## room clean + ask time + faq 3
* clean_room{"clean_later_descriptive":"after 4 hours"}
  - utter_is_time_fine
* faq
  - respond_faq
* faq
  - respond_faq
  - utter_is_time_fine
* deny
  - utter_what_time
* inform{"clean_time":"5 PM"}
  - utter_clean_confirm_later