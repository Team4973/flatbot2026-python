#!/usr/bin/env python3
"""
Flatbot 2026 - FRC Team 4973
Python/RobotPy version

Controls:
    A button (hold): Spin motor at current speed
    A button (release): Stop motor
    D-pad up: Increase speed by 0.05
    D-pad down: Decrease speed by 0.05
    Starting speed: 0.1

Hardware:
    - TalonFX motor on CAN ID 30
    - Xbox controller on port 0
"""

import wpilib
from commands2 import CommandScheduler

from robot_container import RobotContainer


class Robot(wpilib.TimedRobot):
    """
    Main robot class - controls the robot lifecycle.

    TimedRobot runs periodic functions every 20ms (50Hz).
    The CommandScheduler handles button bindings and command execution.
    """

    def robotInit(self):
        """Called once when the robot starts. Set up all hardware here."""
        print("Hello, World")
        self.container = RobotContainer()

    def robotPeriodic(self):
        """Called every 20ms. Runs the command scheduler to process button presses."""
        CommandScheduler.getInstance().run()
        self.container.update_telemetry()

    def autonomousInit(self):
        """Called once when autonomous mode starts."""
        pass

    def autonomousPeriodic(self):
        """Called every 20ms during autonomous mode."""
        pass

    def teleopInit(self):
        """Called once when teleop mode starts."""
        pass

    def teleopPeriodic(self):
        """Called every 20ms during teleop mode."""
        pass

    def testInit(self):
        """Called once when test mode starts."""
        pass

    def testPeriodic(self):
        """Called every 20ms during test mode."""
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
