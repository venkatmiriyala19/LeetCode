# Write your MySQL query statement below
select firstName,lastName,city,state
from Person p
left join Address adds
on p.personId=adds.personId
