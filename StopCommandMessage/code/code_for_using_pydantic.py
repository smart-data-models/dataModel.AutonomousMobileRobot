from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class StopCommand(Enum):
    stop = 'stop'


class Type(Enum):
    StopCommandMessage = 'StopCommandMessage'


class StopCommandMessage(BaseModel):
    commandTime: Optional[AwareDatetime] = Field(
        None, description='Sent time to the robot'
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
    stopCommand: Optional[StopCommand] = Field(
        None, description="Enum:'stop'. The stop command to the robot"
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be StopCommandMessage'
    )
