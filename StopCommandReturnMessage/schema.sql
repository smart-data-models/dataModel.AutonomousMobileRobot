/* (Beta) Export of data model StopCommandReturnMessage of the subject dataModel.AutonomousMobileRobot for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE receivedStopCommand_type AS ENUM ('stop');CREATE TYPE resultsOfStopCommand_type AS ENUM ('ack', 'error');CREATE TYPE StopCommandReturnMessage_type AS ENUM ('StopCommandReturnMessage');
CREATE TABLE StopCommandReturnMessage (commandTime timestamp, errors json, receivedStopCommand receivedStopCommand_type, receivedTime timestamp, resultsOfStopCommand resultsOfStopCommand_type, type StopCommandReturnMessage_type);