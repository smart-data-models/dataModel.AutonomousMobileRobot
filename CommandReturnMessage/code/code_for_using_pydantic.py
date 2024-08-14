from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class Latitude(BaseModel):
    pass


class Longitude(BaseModel):
    pass


class GeographicPoint(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    altitude: float = Field(..., description='Simple coordinate of a point')
    latitude: Latitude
    longitude: Longitude


class Orientation2D(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    theta: float = Field(..., description='Simple measurement of an angle')


class Orientation3D(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    pitch: float = Field(..., description='Simple measurement of an angle')
    roll: float = Field(..., description='Simple measurement of an angle')
    yaw: float = Field(..., description='Simple measurement of an angle')


class Point2D(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    x: float = Field(..., description='Simple coordinate of a point')
    y: float = Field(..., description='Simple coordinate of a point')


class Point3D(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    x: float = Field(..., description='Simple coordinate of a point')
    y: float = Field(..., description='Simple coordinate of a point')
    z: float = Field(..., description='Simple coordinate of a point')


class ReceivedWaypoint(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    geographicPoint: Optional[GeographicPoint] = Field(
        None, description='Point in geographic coordinates'
    )
    mapId: Optional[str] = Field(None, description='Map ID')
    orientation2D: Optional[Orientation2D] = Field(
        None, description='2D Angle of an element'
    )
    orientation3D: Optional[Orientation3D] = Field(
        None, description='3D Angles of an element'
    )
    point2D: Optional[Point2D] = Field(
        None, description='Point in 2D as a two simple coordinates x and y'
    )
    point3D: Optional[Point3D] = Field(
        None, description='Point in 3D as a three simple coordinates x, y and z'
    )
    speed: Optional[float] = Field(
        None, description='Robot speed between coordinates of waypoints[m/s]'
    )


class Result(Enum):
    ack = 'ack'
    ignore = 'ignore'
    error = 'error'


class Type(Enum):
    CommandReturnMessage = 'CommandReturnMessage'


class CommandReturnMessage(BaseModel):
    commandTime: Optional[AwareDatetime] = Field(
        None, description='Sent time to the robot'
    )
    errors: Optional[List[str]] = Field(
        None, description='Describes the errors that occurred in the robot'
    )
    receivedCommand: Optional[str] = Field(
        None, description='The command which the robot received'
    )
    receivedTime: Optional[AwareDatetime] = Field(
        None, description='Command received time to the robot'
    )
    receivedWaypoints: Optional[List[ReceivedWaypoint]] = Field(
        None, description='The waypoints which the robot received'
    )
    result: Optional[Result] = Field(
        None,
        description="Enum:'ack, error, ignore'. The result of the robot received the command",
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be CommandReturnMessage'
    )
