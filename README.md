
# sic_pyserial_lib
This is a child project of the Samuko IMU Compute (SIC) project. This library helps communicate with the already setup IMU (`MPU9250 module`) in you PC or microcomputer-based python projects, after successful setup with the [**`sic_calibration_py_codes`**](https://github.com/samuko-things-company/sic_calibration_py_codes).

> you can use it in your microcomputer robotics project (e.g Raspberry Pi, PC, etc.)

A simple way to get started is simply to try out and follow the example code


## Dependencies
- you'll need to pip install the pyserial library
  > pip3 install pyserial


## How to Use the Library
- Ensure you have the **`sic_mpu9250_driver module`** interfaced with the **`MPU9250`** module. setup and cilibrate it using the **`sic_calibration_py_codes`**.

- Download (by clicking on the green Code button above) or clone the repo into your PC.

- A simple way to get started is simply to try out and follow the example `read_rpy.py` code.

- You can copy the **`sic_pyserial_lib.py`** file into your python robotics project, import the library as shown in the example `read_rpy.py` code, add it to your code, and start using it.

## Basic Library functions and usage

- connect to sic_driver shield module
  > SIC("port_name or port_path")

- get filtered Roll, Pitch and Yaw readings
  > getRPY()

- get quaternions qw, qx, qy, qz
  > getQuat()

- get Roll, Pitch and Yaw rates value
  > getRPYrate()

- get linear acceleration values ax, ay, az
  > getAcc()

- get rpy variances
  > getRPYvariance()

- get rpy rate variances
  > getRPYrateVariance()

- get acceleration variances
  > getAccVariance()