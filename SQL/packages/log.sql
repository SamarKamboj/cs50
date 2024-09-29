
-- *** The Lost Letter ***
select * from addresses;

-- *** The Devious Delivery ***
select * from scans where package_id = (select id from packages where from_address_id IS NULL);

select * from addresses where id = 348;

-- *** The Forgotten Gift ***

select * from packages where to_address_id = 7432;

