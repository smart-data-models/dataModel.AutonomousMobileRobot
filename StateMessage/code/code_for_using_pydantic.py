from __future__ import annotations

from datetime import time
from enum import Enum
from typing import List, Optional, Union

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, confloat


class Accuracy(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    covariance: Optional[List[float]] = Field(
        None, description='Error covariance matrix of estimated position'
    )


class Battery(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    current: Optional[float] = Field(None, description='Current of the mobile element')
    remainingPercentage: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None, description='Remaining battery charge'
    )
    remainingTime: Optional[time] = Field(
        None, description='Expected lifespan of a battery'
    )
    voltage: float = Field(..., description='Voltage of the mobile element')


class Battery1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    current: Optional[float] = Field(None, description='Current of the mobile element')
    remainingPercentage: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None, description='Remaining battery charge'
    )
    remainingTime: time = Field(..., description='Expected lifespan of a battery')
    voltage: Optional[float] = Field(None, description='Voltage of the mobile element')


class Battery2(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    current: Optional[float] = Field(None, description='Current of the mobile element')
    remainingPercentage: confloat(ge=0.0, le=100.0) = Field(
        ..., description='Remaining battery charge'
    )
    remainingTime: Optional[time] = Field(
        None, description='Expected lifespan of a battery'
    )
    voltage: Optional[float] = Field(None, description='Voltage of the mobile element')


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


class Destination(BaseModel):
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


class Mode(Enum):
    error = 'error'
    navi = 'navi'
    standby = 'standby'


class GeographicPoint1(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    altitude: float = Field(..., description='Simple coordinate of a point')
    latitude: Latitude
    longitude: Longitude


class Pose(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    geographicPoint: Optional[GeographicPoint1] = Field(
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


class Type(Enum):
    StateMessage = 'StateMessage'


class StateMessage(BaseModel):
    accuracy: Optional[Accuracy] = Field(
        None, description='Position accuracy of the robot'
    )
    battery: Optional[Union[Battery, Battery1, Battery2]] = Field(
        None, description='The states of the battery the robot mounted'
    )
    commandTime: Optional[AwareDatetime] = Field(
        None, description='Sent time to the robot'
    )
    destination: Optional[Destination] = Field(
        None,
        description='Current destination of the robot. Basically, it is the same as one of the waypoints',
    )
    errors: Optional[List[str]] = Field(
        None, description='Describes the errors that occurred in the robot'
    )
    mode: Optional[Mode] = Field(
        None,
        description="Enum:'error, navi, standby'. Navigational status of the robot",
    )
    pose: Optional[Pose] = Field(None, description='Current position of the robot.')
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be StateMessage'
    )
