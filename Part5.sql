/*1*/

select s1.name, s1.licence_no, s1.addr, s1.birthday, s1.class, s2.description from (select * from people LEFT JOIN drive_licence on people.sin = drive_licence.sin)s1, (select * from driving_condition LEFT JOIN restriction on driving_condition.c_id = restriction.r_id)s2 where s1.licence_no = s2.licence_no;
/*AND UPPER(s1.name) = 'USERNAMESEARCHSTRING'
AND s1.licence_no = 'LICENCESEARCHSTRING'*/


/*2*/

select ticket_no, vdate, vtype, descriptions from (select * from ticket LEFT JOIN drive_licence on ticket.violator_no = drive_licence.sin) WHERE licence_no = 'GIVENLICENCENO';
/*WHERE sin = 'GIVENSIN'


/*3*/

select counts.c, avgs.a, viols.cnt from (select count(*) as c from auto_sale )counts, (select SUM(price)/count(*) as a from auto_sale )avgs, (select count(*) as cnt from ticket )viols where counts.vehicle_id = 'INPUT STRING' AND avgs.vehicle_id = 'INPUT STRING' AND viols.vehicle_id = 'INPUT STRING';

/*where vehicle_id = 'INPUTVIN'
/*where vehicle_id = 'INPUTVIN'
/*where vehicle_id = 'INPUTVIN'
