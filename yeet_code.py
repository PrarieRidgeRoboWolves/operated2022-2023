package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.DcMotorSimple;

@TeleOp(name = "tank (Blocks to Java)", group = "")
public class tank extends LinearOpMode {

  private DcMotor fright;
  private DcMotor fleft;
  private DcMotor bright;
  private DcMotor bleft;
  /**
   * This function is executed when this Op Mode is selected from the Driver Station.
   */
  @Override
  public void runOpMode() {
    fright = hardwareMap.dcMotor.get("fright");
    fleft = hardwareMap.dcMotor.get("bright");
    bright = hardwareMap.dcMotor.get("fleft");
    bleft = hardwareMap.dcMotor.get("bleft");
    // Reverse one of the drive motors.
    // You will have to determine which motor to reverse for your robot.
    // In this example, the right motor was reversed so that positive
    // applied power makes it move the robot in the forward direction.
    fright.setDirection(DcMotorSimple.Direction.REVERSE);
    waitForStart();
    if (opModeIsActive()) {
      // Put run blocks here.
      while (opModeIsActive()) {
        // Put loop blocks here.
        // The Y axis of a joystick ranges from -1 in its topmost position
        // to +1 in its bottommost position. We negate this value so that
        // the topmost position corresponds to maximum forward power.
        // fleft = bright
        // bright = fleft
        fleft.setPower(-gamepad1.left_stick_y*.5);
        fright.setPower(-gamepad1.left_stick_y);
        bleft.setPower(gamepad1.left_stick_y*.5);
        bright.setPower(-gamepad1.left_stick_y*.75);
        telemetry.addData("Left Pow", fleft.getPower());
        telemetry.addData("Right Pow", bright.getPower());
        telemetry.addData("Left Pow2", bleft.getPower());
        telemetry.addData("Right Pow2", fright.getPower());
        telemetry.update();
        bright.setPower(-gamepad1.right_stick_x);
        fright.setPower(gamepad1.right_stick_x);
        bleft.setPower(-gamepad1.right_stick_x * 100);
        fleft.setPower(-gamepad1.right_stick_x * 1000);
        fleft.setPower(-gamepad1.right_stick_y*.5);
        fright.setPower(-gamepad1.right_stick_y);
        bleft.setPower(gamepad1.right_stick_y*.5);
        bright.setPower(-gamepad1.right_stick_y*.75);
      }
    }
  }
}
