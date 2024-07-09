
# sic_mpu9250_pyserial_lib
This is a child project of the Samuko IMU Compute (**`sic_mpu9250`**) project. This library helps communicate with the already setup IMU (`MPU9250 module`) in you PC or microcomputer-based python projects, after successful setup with the [**`sic_mpu9250_setup_application`**](https://github.com/samuko-things-company/sic_mpu9250_setup_application).

> you can use it in your microcomputer robotics project (e.g Raspberry Pi, PC, etc.)

A simple way to get started is simply to try out and follow the example code


## Dependencies
- you'll need to pip install the pyserial library
  ```shell
    pip3 install pyserial   //linux or mac
    pip install pyserial   //windows
  ```

## How to Use the Library
- Download (by clicking on the green Code button above) or clone the repo into your PC using `git clone`

- Ensure you have the **`sic_mpu9250_driver module`** interfaced with the **`MPU9250`** module and already calibrated.

- Connect the **`sic_mpu9250_driver module`** to your PC or microcomputer

- A simple way to get started is simply to try out and follow the example `read_rpy.py` code.

- You can copy the **`sic_mpu9250_pyserial_lib.py`** file into your python robotics project, import the library as shown in the example `read_rpy.py` code, add it to your code, and start using it.

## Basic Library functions and usage

- connect to sic_driver shield module
  > SIC("port_name or port_path")

- get filtered Roll, Pitch and Yaw readings
  > getRPY()

- get quaternions qw, qx, qy, qz
  > getQuat()

- get Roll(gx), Pitch(gy) and Yaw(gz) rates value
  > getGyro()

- get linear acceleration values ax, ay, az
  > getAcc()

- get rpy variances
  > getRPYvariance()

- get rpy rate variances
  > getGyroVariance()

- get acceleration variances
  > getAccVariance()