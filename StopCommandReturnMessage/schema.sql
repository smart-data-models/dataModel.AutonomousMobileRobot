/* (Beta) Export of data model StopCommandReturnMessage of the subject dataModel.AutonomousMobileRobot for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE StopCommandReturnMessage_receivedStopCommand_type AS ENUM ('stop');
CREATE TYPE StopCommandReturnMessage_resultsOfStopCommand_type AS ENUM ('ack', 'error');
CREATE TYPE StopCommandReturnMessage_type AS ENUM ('StopCommandReturnMessage');
CREATE TABLE StopCommandReturnMessage (
  "commandTime" TIMESTAMP,
  "errors" JSON,
  "id" TEXT PRIMARY KEY,
  "receivedStopCommand" StopCommandReturnMessage_receivedStopCommand_type,
  "receivedTime" TIMESTAMP,
  "resultsOfStopCommand" StopCommandReturnMessage_resultsOfStopCommand_type,
  "type" StopCommandReturnMessage_type
);