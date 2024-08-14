from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class ReceivedStopCommand(Enum):
    stop = 'stop'


class ResultsOfStopCommand(Enum):
    ack = 'ack'
    error = 'error'


class Type(Enum):
    StopCommandReturnMessage = 'StopCommandReturnMessage'


class StopCommandReturnMessage(BaseModel):
    commandTime: Optional[AwareDatetime] = Field(
        None, description='Sent time to the robot'
    )
    errors: Optional[List[str]] = Field(
        None, description='Describes the errors that occurred in the robot'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    receivedStopCommand: Optional[ReceivedStopCommand] = Field(
        None, description='The stop command which the robot received.'
    )
    receivedTime: Optional[AwareDatetime] = Field(
        None, description='Command received time to the robot'
    )
    resultsOfStopCommand: Optional[ResultsOfStopCommand] = Field(
        None,
        description="Enum:'ack, error'. The result of the robot received the stop command",
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be StopCommandReturnMessage'
    )
