## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## intropath
* introduction
  - utter_bot

## enterprojpath
* enterproj
  - action_enterproj

## lasas
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help

##unix monitor subscription
* subscribe_unix_monitor
  - action_subscribe_unix_monitor

##notification_yes
* yes
  - action_yes

##notification_no
* no
  - action_no
