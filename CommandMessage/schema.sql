/* (Beta) Export of data model CommandMessage of the subject dataModel.AutonomousMobileRobot for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CommandMessage_type AS ENUM ('CommandMessage');
CREATE TABLE CommandMessage (command TEXT, commandTime TIMESTAMP, type CommandMessage_type, waypoints JSON);