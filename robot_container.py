"""
RobotContainer - Hardware setup and button bindings for Flatbot.

This file creates the motor, controller, and connects buttons to actions.
Think of it as the "wiring diagram" between hardware and software.

See WIRING.md for the physical wiring map (PDH channels, CAN IDs, etc.)
"""

import wpilib
from commands2 import InstantCommand
from commands2.button import CommandXboxController
from phoenix6.hardware import Pigeon2, TalonFX
from wpilib import SmartDashboard


class RobotContainer:
    """
    Sets up hardware and connects controller buttons to robot actions.

    Controls:
        A button (hold): Spin motor at current speed
        A button (release): Stop motor
        B button: Zero IMU heading
        D-pad up: Increase speed by 0.05
        D-pad down: Decrease speed by 0.05
    """

    def __init__(self):
        # Power Distribution Hub (REV-11-1850) on CAN ID 1
        # Monitors power to all channels - see WIRING.md for channel assignments
        self.pdh = wpilib.PowerDistribution(1, wpilib.PowerDistribution.ModuleType.kRev)

        # Hardware setup
        self.motor = TalonFX(30)  # TalonFX on CAN ID 30

        # Pigeon 2 IMU on CAN ID 39
        # Note: Pigeon2 causes timeout in simulation, only init on real robot
        if wpilib.RobotBase.isReal():
            self.imu = Pigeon2(39)
        else:
            self.imu = None

        # Driver controller
        self.controller = CommandXboxController(0)  # Xbox controller on port 0

        # Motor speed (adjustable via D-pad)
        self.speed = 0.1

        # Connect buttons to actions
        self._configure_button_bindings()

    def _configure_button_bindings(self):
        """Wire up controller buttons to robot actions."""
        # A button: hold to spin motor, release to stop
        self.controller.a().onTrue(InstantCommand(self._start_motor))
        self.controller.a().onFalse(InstantCommand(self._stop_motor))

        # B button: zero IMU heading
        self.controller.b().onTrue(InstantCommand(self.zero_heading))

        # D-pad: adjust speed
        self.controller.povUp().onTrue(InstantCommand(lambda: self._change_speed(0.05)))
        self.controller.povDown().onTrue(InstantCommand(lambda: self._change_speed(-0.05)))

    def _start_motor(self):
        """Spin the motor at the current speed."""
        print(f"Motor set at {self.speed}")
        self.motor.set(self.speed)

    def _stop_motor(self):
        """Stop the motor."""
        self.motor.set(0.0)

    def _change_speed(self, delta: float):
        """Adjust the motor speed by the given amount."""
        self.speed += delta
        print(f"Speed changed to {self.speed}")

    def update_telemetry(self):
        """Publish motor and IMU data to SmartDashboard."""
        # Motor telemetry
        SmartDashboard.putNumber("Motor/Target Speed", self.speed)
        SmartDashboard.putNumber("Motor/Output", self.motor.get())
        SmartDashboard.putNumber("Motor/Velocity (rps)", self.motor.get_velocity().value)
        SmartDashboard.putNumber("Motor/Position (rot)", self.motor.get_position().value)
        SmartDashboard.putNumber("Motor/Voltage", self.motor.get_motor_voltage().value)

        # IMU telemetry (only on real robot)
        if self.imu is not None:
            SmartDashboard.putNumber("IMU/Yaw (deg)", self.imu.get_yaw().value)
            SmartDashboard.putNumber("IMU/Pitch (deg)", self.imu.get_pitch().value)
            SmartDashboard.putNumber("IMU/Roll (deg)", self.imu.get_roll().value)

    def zero_heading(self):
        """Reset the IMU yaw to zero."""
        if self.imu is not None:
            self.imu.set_yaw(0)
