-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description
  FROM crime_scene_reports
  WHERE day = 28 AND month = 7 AND street = "Humphrey Street" AND description LIKE "%CS50%";

SELECT transcript
  FROM interviews
  WHERE day = 28 AND month = 7 and transcript like "%thief%";

-- People who exit the bakery within 10 minutes of theft
select license_plate
  from bakery_security_logs
  where day = 28 and month = 7 and id >= 260 and hour = 10 and minute <= 25;

-- People who withdraw money on July 28 on Leggett Street
select name
  from people
  where id in
    (select person_id
       from bank_accounts
       where account_number in
         (select account_number
            from atm_transactions
            where atm_location = "Leggett Street" and day = 28 and month = 7 and transaction_type = "withdraw"));

-- People who withdraw money on July 28 on Leggett Street and exit the bakery within 10 minutes of theft
select bakery_security_logs.license_plate
  from bakery_security_logs
    join people
    on bakery_security_logs.license_plate = people.license_plate
    where people.id in
    (select person_id
      from bank_accounts
      where account_number in
        (select account_number
          from atm_transactions
          where atm_location = "Leggett Street" and atm_transactions.day = 28 and atm_transactions.month = 7 and transaction_type = "withdraw"))
  and bakery_security_logs.day = 28 and bakery_security_logs.month = 7 and bakery_security_logs.id >= 260 and hour = 10 and minute <= 25;

-- Suspect's details
select *
  from people
  where license_plate in
    (select bakery_security_logs.license_plate
      from bakery_security_logs
        join people
        on bakery_security_logs.license_plate = people.license_plate
        where people.id in
        (select person_id
          from bank_accounts
          where account_number in
            (select account_number
              from atm_transactions
              where atm_location = "Leggett Street" and atm_transactions.day = 28 and atm_transactions.month = 7 and transaction_type = "withdraw"))
      and bakery_security_logs.day = 28 and bakery_security_logs.month = 7 and bakery_security_logs.id >= 260 and hour = 10 and minute <= 25);

-- Suspects details who took flight on July 29
select *
  from people
  where passport_number in
(select passport_number
  from passengers
    join flights
      on flights.id = passengers.flight_id
  where flights.day = 29 and passport_number in
    (select passport_number
      from people
      where license_plate in
        (select bakery_security_logs.license_plate
          from bakery_security_logs
            join people
            on bakery_security_logs.license_plate = people.license_plate
            where people.id in
            (select person_id
              from bank_accounts
              where account_number in
                (select account_number
                  from atm_transactions
                  where atm_location = "Leggett Street" and atm_transactions.day = 28 and atm_transactions.month = 7 and transaction_type = "withdraw"))
          and bakery_security_logs.day = 28 and bakery_security_logs.month = 7 and bakery_security_logs.id >= 260 and hour = 10 and minute <= 25))
  order by hour);

select *
  from people
  where phone_number in
    (select receiver
      from phone_calls
      where caller in
        (select phone_number
          from people
          where name = "Luca" or name = "Bruce") and duration <= 60);

select *
  from flights
  where day = 29 and month = 7;

select *
  from airports
  where id = 4;

