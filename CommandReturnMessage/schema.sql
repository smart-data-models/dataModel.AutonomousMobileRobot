/* (Beta) Export of data model CommandReturnMessage of the subject dataModel.AutonomousMobileRobot for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CommandReturnMessage_result_type AS ENUM ('ack', 'ignore', 'error');
CREATE TYPE CommandReturnMessage_type AS ENUM ('CommandReturnMessage');
CREATE TABLE CommandReturnMessage (
  "commandTime" TIMESTAMP,
  "errors" JSON,
  "receivedCommand" TEXT,
  "receivedTime" TIMESTAMP,
  "receivedWaypoints" JSON,
  "result" CommandReturnMessage_result_type,
  "type" CommandReturnMessage_type
);