INSERT INTO people VALUES (100001, 'Bobby', 100.10, 150.60, 'blue', 'blonde', '123 abc street Edmonton', 'm', '22-MAR-94');
INSERT INTO people VALUES (100002, 'Johnson', 160.5, 200.1, 'green', 'brown', '124 abc street Edmonton', 'm', '12-Jan-72');
INSERT INTO people VALUES (100003, 'Joe', 145.23, 170, 'blue', 'black', '125 abc street Edmonton', 'm', '14-FEB-00');
INSERT INTO people VALUES (100004, 'Sally', 100.3, 130.3, 'red', 'blonde', '432 def street Saskatchewan', 'f', '13-MAR-06');
INSERT INTO people VALUES (100005, 'Ben', 300.50, 179.68, 'brown', 'blonde', '444 abc street Edmonton', 'm', '10-APR-94');
INSERT INTO people VALUES (100006, 'Ashley', 67.2, 154.54, 'purple', 'brown', '267 sweet street Vancouver', 'f', '14-MAY-94');
INSERT INTO people VALUES (100007, 'Mark', 200.5, 189.75, 'brown', 'red', '123 some street Edmonton', 'm', '22-JUN-96');
INSERT INTO people VALUES (100008, 'Mary', 140.25, 200.5, 'blue', 'pink', '235 abc street Winnipeg', 'f', '05-MAR-94');
INSERT INTO people VALUES (100009, 'April', 170.65, 130, 'green', 'black', '123 def street Edmonton', 'f', '04-MAR-99');
INSERT INTO people VALUES (100010, 'Dakota', 300.15, 100, 'brown', 'red', '124 def street Vancouver', 'f', '22-SEP-94');

INSERT INTO drive_licence VALUES (123456, 100001, 'GOOD', NULL, '22-MAR-10', '22-MAR-15');
INSERT INTO drive_licence VALUES (123457, 100002, 'BAD', NULL, '12-FEB-88', '12-FEB-93');
INSERT INTO drive_licence VALUES (123458, 100003, 'MEH', NULL, '14-FEB-13', '14-FEB-18');
INSERT INTO drive_licence VALUES (123459, 100004, 'OK', NULL, '14-MAR-13', '14-MAR-18');
INSERT INTO drive_licence VALUES (123460, 100005, 'GOOD', NULL, '22-MAR-10', '22-MAR-15');
INSERT INTO drive_licence VALUES (123461, 100006, 'TERRIBLE', NULL, '14-MAY-10', '14-MAY-15');
INSERT INTO drive_licence VALUES (123462, 100007, 'MEH', NULL, '30-JUL-12', '30-JUL-17');
INSERT INTO drive_licence VALUES (123463, 100008, 'MEH', NULL, '05-MAR-10', '05-MAR-15');
INSERT INTO drive_licence VALUES (123464, 100009, 'nondriving', NULL, '22-MAR-10', '22-MAR-15');

INSERT INTO driving_condition VALUES (0001, 'scary roads');
INSERT INTO driving_condition VALUES (0002, 'winding roads');
INSERT INTO driving_condition VALUES (0003, 'icy roads');
INSERT INTO driving_condition VALUES (0004, 'dry roads');

INSERT INTO restriction VALUES (123456, 0001);
INSERT INTO restriction VALUES (123457, 0003);
INSERT INTO restriction VALUES (123458, 0002);
INSERT INTO restriction VALUES (123459, 0001);
INSERT INTO restriction VALUES (123460, 0001);
INSERT INTO restriction VALUES (123461, 0002);
INSERT INTO restriction VALUES (123462, 0004);
INSERT INTO restriction VALUES (123463, 0003);
INSERT INTO restriction VALUES (123464, 0001);

INSERT INTO vehicle_type VALUES (0001, 'car');
INSERT INTO vehicle_type VALUES (0002, 'truck');
INSERT INTO vehicle_type VALUES (0003, 'van');
INSERT INTO vehicle_type VALUES (0004, 'suv');
INSERT INTO vehicle_type VALUES (0005, 'crossover');
INSERT INTO vehicle_type VALUES (0006, 'supercar');

INSERT INTO vehicle VALUES ('1K53KG', 'Lamborghini', 'Veneno', 2014, 'yellow', 0006);
INSERT INTO vehicle VALUES ('1R53KG', 'Aston Martin', 'V8 Vantage', 2014, 'grey', 0006);
INSERT INTO vehicle VALUES ('1K43KG', 'Toyota', 'Tundra', 2005, 'blue', 0002);
INSERT INTO vehicle VALUES ('1K53KF', 'Honda', 'Civic', 1994, 'white', 0001);
INSERT INTO vehicle VALUES ('1K34KF', 'Honda', 'CRV', 2014, 'purple', 0005);
INSERT INTO vehicle VALUES ('7K53KF', 'Honda', 'Odyssey', 2008, 'red', 0003);
INSERT INTO vehicle VALUES ('7K45GR', 'Porsche', 'Cayenne', 2012, 'black', 0004);
INSERT INTO vehicle VALUES ('9R34TD', 'Ferrari', '458 Italia', 2015, 'red', 0006);
INSERT INTO vehicle VALUES ('8P73RF', 'Mitsubishi', 'Lancer', 2008, 'white', 0001);

INSERT INTO owner VALUES (100001, '1K53KG', 'y');
INSERT INTO owner VALUES (100002, '1K53KG', 'n');
INSERT INTO owner VALUES (100003, '1K53KG', 'n');
INSERT INTO owner VALUES (100002, '1R53KG', 'y');
INSERT INTO owner VALUES (100004, '1K43KG', 'y');
INSERT INTO owner VALUES (100005, '1K53KF', 'y');
INSERT INTO owner VALUES (100006, '1K34KF', 'y');
INSERT INTO owner VALUES (100007, '7K53KF', 'y');
INSERT INTO owner VALUES (100008, '7K45GR', 'y');
INSERT INTO owner VALUES (100009, '9R34TD', 'y');
INSERT INTO owner VALUES (100004, '8P73RF', 'y');

INSERT INTO auto_sale VALUES (0001, 100005, 100001, '1K53KG', '21-MAR-10', 4999999.95);
INSERT INTO auto_sale VALUES (0002, 100002, 100002, '1R53KG', '18-FEB-08', 180000.00);
INSERT INTO auto_sale VALUES (0003, 100003, 100004, '1K43KG', '17-MAY-10', 39999.99);
INSERT INTO auto_sale VALUES (0004, 100009, 100005, '1K53KF', '24-APR-06', 25000.00);
INSERT INTO auto_sale VALUES (0005, 100006, 100006, '1K34KF', '15-MAR-10', 30000.00);
INSERT INTO auto_sale VALUES (0006, 100005, 100007, '7K53KF', '14-SEP-08', 28799.95);
INSERT INTO auto_sale VALUES (0007, 100008, 100008, '7K45GR', '16-JUN-09', 78000.00);
INSERT INTO auto_sale VALUES (0008, 100001, 100009, '9R34TD', '21-MAR-10', 350000.00);
INSERT INTO auto_sale VALUES (0009, 100002, 100004, '8P73RF', '25-MAR-12', 10800.00);
INSERT INTO auto_sale VALUES (0010, 100004, 100002, '8P73RF', '26-MAR-12', 500.00);
INSERT INTO auto_sale VALUES (0011, 100002, 100004, '8P73RF', '27-MAR-12', 500.00);


INSERT INTO ticket_type VALUES ('parking', 150);
INSERT INTO ticket_type VALUES ('speeding', 500);
INSERT INTO ticket_type VALUES ('smugling', 10);
INSERT INTO ticket_type VALUES ('racing', 900);

INSERT INTO ticket VALUES (0001, 100001, '1K53KG', 100005, 'speeding', '21-MAR-13', '123 street', 'What a crazy guy. going like 300 in a 50. waaaaay too fast man');
INSERT INTO ticket VALUES (0002, 100001, '1K53KG', 100005, 'racing', '22-MAR-10','51 street', 'same guy from yesterday... at this rate we might be getting some new police cars');
INSERT INTO ticket VALUES (0003, 100001, '1K53KG', 100004, 'speeding', '22-MAR-13', '51 street', 'Ben got him going to work, i got him going home');
INSERT INTO ticket VALUES (0004, 100005, '1K53KF', 100004, 'parking', '28-MAR_10', '89 street', 'a sidewalk is not a parking spot');
INSERT INTO ticket VALUES (0005, 100001, '1K53KG', 100004, 'speeding', '23-MAR-13', '51 street', 'Ben got him going to work, i got him going home');
INSERT INTO ticket VALUES (0006, 100002, '1R53KG', 100004, 'speeding', '21-MAR-13', 'some street', 'some comments' );
INSERT INTO ticket VALUES (0007, 100002, '1R53KG', 100004, 'speeding', '22-MAR-13', 'some street', 'some comments' );
INSERT INTO ticket VALUES (0008, 100002, '1R53KG', 100004, 'speeding', '21-MAR-12', 'some street', 'some comments' );







