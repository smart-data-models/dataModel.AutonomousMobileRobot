/* (Beta) Export of data model CommandMessage of the subject dataModel.AutonomousMobileRobot for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CommandMessage_type AS ENUM ('CommandMessage');
CREATE TABLE CommandMessage (command text, commandTime timestamp, type CommandMessage_type, waypoints json);