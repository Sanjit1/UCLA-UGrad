# ENGR 96A: Underwater Robotics

**Instructor**: Abi and John.

**Term**: Fall 2022

**Review**: ENGR 96's are always fun. This one was no exception. Take one, actually take as many as you can. 

## Class Structure
This Engineering 96A course was Underwater Robotics. 


Constraints: It was mostly freeform, but we were to use Johnson Bilge Motors as thrusters, PVC pipes and connectors as the frame, and the thrusters were to be mounted on the robot and the controller directly wired to the thrusters through a coaxial cable. This made it so that if we needed to extract the robot from the water, we could just pull the coaxial cable and the robot would come out. 

Teams: We worked in teams of 5 people.

## Our Robot
~~Im too lazy to find and upload the schematics and CAD files(also because I don't wanna upload things that I didn't write), but here's a picture of our robot.~~ [Here](https://docs.google.com/presentation/d/1EDqoLFrslpXSK632AuDD5Fuua_n4EsB2LjOhfmIVRCE/edit#slide=id.g1a114af74db_0_717) are the slides for our presentation.


### What we did special
There were two things our team did differently that was worth mentioning.
We used 3D printed connectors to connect the PVC frame in a triangular fashion. This was to get a smaller footprint, and to make it easier to mount the thrusters. 

We also used an Arduino Nano to control the thrusters. This was to make it easier to control the thrusters instead of a switch for each polarity of the thruster. 

#### Things that I can talk about
I worked mostly on the electronics for the controller with one of my teammates. I did the hardware and he wrote most of the software.

The main challenge was that the thrusters ran on 12V, and the Arduino Nano ran on 5V. We also wanted to be able to reverse the polarity of the thrusters. Additionally, we did not want to use level shifters since that felt kinda cheaty.

We came up with two concepts: a Discrete Driver and a Continuous Driver. 
 - The Discrete Driver was our backup plan since it was very simple and easy to implement. It used a SPDT relay to turn on the thrusters, and a DPDT relay to control the polarity. With joystick modules, we could control the thrusters by just using the joystick module to control the relays.

 - Continuous Driver was our main plan. It used a MOSFET to control the strength of the thruster and a DPDT relay to control the polarity. The MOSFET was controlled by a PWM signal from the Arduino Nano, driven from the joystick module. 

**Discrete Driver Schematics**
![Discrete Driver Schematics](./Schematics/Discrete%20Schematic.png)
![Discrete Driver PCB](./Schematics/Discrete%20PCB.png)

**Continuous Driver Schematics**
**Note**: This connects a non pwm signal to a pwm signal. Don't do this. This caused issues.
![Continuous Driver Schematics](./Schematics/Continuous%20Schematic.png)
![Continuous Driver PCB](./Schematics/Continuous%20PCB.png)


Talking more about the continuous driver, we went through a few iterations of the circuit. 
All iterations of the circuits used a DPDT relay to control the polarity of the thrusters. 

The first iteration used an OPAMP instead of a MOS to scale the PWM signal from a 5V signal to a 12V signal. The problem with that was we had a 12V power supply and to be able to drive the OPAMP to scale up to 12V we needed a 24V power supply, which was not allowed.

Since we were using a PWM signal, we could also use transistor amplifiers, since while they did not scale analog signals they can scale digital signals(like a PWM one). We used a BJT transistor amplifier with a 2N3904 transistor. This worked, but the transistor was not able to handle the current of the thrusters(and fried some of the digital pins on the Arduino Nano). 

We eventually ended up using a MOSFET, so that there was no back EMF from the thrusters. 

The other issue we had was with the PCB not being able to handle the current required to drive the thrusters. We needed to use a thicker trace to be able to handle the current. It also took 4 layers to route the traces. Most PCB manufacturers have thicker copper traces on the top and bottom layers, so we had to use the inner layers to route the rest of the traces.

Anyways, this was a fun thing to write about yay!