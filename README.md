Easy Modbus – Gateway Pass-Through for PXR Switchgear (Python)

Easy Modbus is a lightweight Python project designed to simplify Modbus communication with PXR switchgear using a TCP-to-RTU gateway pass-through model. It is intended for engineers and technicians who need a fast, reliable way to read and write Modbus registers during commissioning, testing, or troubleshooting.

The primary use case is communicating with PXR devices over Modbus TCP, while routing requests through an Ethernet-to-serial gateway to downstream Modbus RTU slave devices. The script acts as a TCP client, connects to the gateway, and transparently addresses RTU devices on the serial bus using their slave IDs.

This project focuses on practicality rather than abstraction. It provides a clear, minimal interface for reading holding and input registers without unnecessary complexity. Timeouts, logging, and connection behavior are intentionally explicit to make diagnosing communication issues easier in real switchgear environments.

Easy Modbus supports common serial configurations typically required in PXR installations, including configurable baud rate, parity, and stop bits. This allows the script to match site-specific RS-485 trunk settings without modifying core logic.

A typical setup involves a Python script connecting to a Modbus TCP gateway over Ethernet, which then passes requests through to PXR devices or other RTU equipment on an RS-485 network. The user supplies the gateway IP and port, the RTU slave address, and the register information to be accessed.

This repository is intended for use during factory witness testing, field commissioning, and system validation. It is especially useful for confirming end-to-end communication, validating register maps, and troubleshooting addressing or serial configuration issues.

Because switchgear and protection equipment are safety-critical, this project assumes the user understands the impact of Modbus operations. Reading registers is generally safe, but writing registers may alter control behavior or protection settings. Always follow site procedures and test in a controlled environment when possible.

The code is written in Python 3 and typically leverages a standard Modbus client library such as pymodbus. The structure is intentionally simple so it can be easily extended for polling loops, CSV logging, dashboards, or automated test workflows.

This project is provided as-is, with no warranty or guarantee of suitability for any specific application. Users are responsible for verifying correctness, ensuring safe operation, and complying with all applicable standards and procedures.
