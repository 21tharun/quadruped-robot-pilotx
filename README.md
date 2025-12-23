# Robotic Dog – Quadruped Robot using PilotX Microcontroller

## Introduction
This project demonstrates the design and implementation of a **quadruped robotic dog**
developed during an industry-aligned robotics workshop conducted at
**BMS College of Engineering**.

The robot is capable of performing fundamental quadruped behaviors such as
**walking, sitting, posture transitions, handshaking, and interactive movements**.
The project focuses on **embedded motion control, servo coordination, and modular
robotics software design** using a dedicated robotics microcontroller.

This repository documents the **hardware setup, software architecture, workflow,
and implementation** of the robotic dog.

---

## About the Microcontroller

### PilotX (Mavrick Series)
The robotic dog is powered by the **PilotX (Mavrick series)** microcontroller,
developed by **:contentReference[oaicite:0]{index=0} (Safear India)**.

Safear India is a deep-tech robotics and automation startup recognized under
**Startup India** and supported by **IIT Mandi – NIDHI Prayas Program**.

#### Key Features of PilotX:
- ARM Cortex–based architecture
- Designed specifically for **robotics and motion control**
- Native **MicroPython** support
- Multiple PWM channels for controlling servo motors
- Communication interfaces:
  - UART
  - I²C
  - SPI
- Sensor-ready architecture:
  - IMU (Gyroscope + Accelerometer)
  - Ultrasonic sensor
  - IR sensors
- Plug-and-play robotics design (no breadboard wiring)

The controller is used along with **PlannerX**, Safear’s robotics control and
visualization software for testing, calibration, and rapid prototyping.

---

## Hardware Components Required

### Mechanical Components
- 3 × 2 Bent Beams  
- 4 × 3 Support Beams  
- Structural plates and connector blocks (MakerX system)  
- Servo holders  
- Fasteners (M3 screws and nuts)  

### Actuators
- **8 × Micro Servo Motors (SG90 or equivalent)**  
  - Hip and knee joints for all four legs  

### Electronics
- PilotX (Mavrick series) Microcontroller  
- Jumper wires (F–F)  
- Power cable (USB / DC jack)  
- Battery pack (Li-ion recommended)  

### Sensors (Platform Supported)
- IMU (Gyroscope + Accelerometer)  
- Ultrasonic distance sensor  
- IR sensors  

---

## Software & Tools

### Programming Language
- **MicroPython**

### Robotics Software
- **PlannerX – Robot Controller & Simulation Software**

📥 **Installation Link:**  
https://www.safeardefense.com/blank-6

PlannerX is used for:
- Servo testing and calibration
- Motion visualization
- Telemetry monitoring
- Rapid robot prototyping

---

## Project Workflow

1. **Mechanical Assembly**
   - Assemble the quadruped frame using MakerX beams and plates
   - Mount servo motors at hip and knee joints
   - Ensure symmetry for balance and stability

2. **Electronics Integration**
   - Connect servo motors to PilotX PWM channels
   - Interface sensors as required
   - Provide stable power to controller and servos

3. **Software Setup**
   - Install PlannerX software
   - Flash MicroPython firmware (if required)
   - Verify communication with the PilotX controller

4. **Servo Calibration**
   - Test individual servos
   - Set neutral (90°) positions
   - Identify servo orientation and limits

5. **Motion Programming**
   - Implement base posture and static poses
   - Add smooth servo interpolation
   - Develop quadruped walking gait
   - Tune timing for balance and coordination

6. **Testing & Demonstration**
   - Execute pose transitions (sit, stand, handshake)
   - Perform walking cycles
   - Record demonstration video

---

## 🎥 Robot Demonstration Video

The video below shows the robotic dog performing walking, posture transitions,
and interactive movements.



---

## Features Implemented
- Base posture stabilization
- Sitting and sit-to-stand transition
- Quadruped walking gait (diagonal leg coordination)
- Smooth servo motion interpolation
- Handshake and attack gestures
- Experimental inverse kinematics for leg motion

---

## Learning Outcomes
- Hands-on experience with embedded robotics
- Servo dynamics and PWM-based motion control
- Quadruped locomotion fundamentals
- MicroPython programming on real hardware
- Modular robotics software architecture
- Understanding real-world hardware constraints

---

## Future Enhancements
- IMU-based self-balancing
- Autonomous obstacle avoidance
- ROS / ROS2 integration
- Vision-based navigation
- AI-assisted gait optimization
