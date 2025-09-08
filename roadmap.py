from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Robotics Career Roadmap & Business Guide", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 6, body)
        self.ln()

pdf = PDF()
pdf.add_page()

content = [
    ("1. Technical Mastery Roadmap (6–18 months)", """
Phase 1: Foundation (0–3 months)
- Python & C++ programming
- Basic electronics (Arduino, sensors, motors)
- Mechanical basics (gears, torque, design)
- Linux basics (Ubuntu, shell, SSH)
- Git and GitHub

Phase 2: Hands-On Robotics (3–9 months)
- Arduino + Raspberry Pi projects (obstacle bot, smart lamp)
- ROS (Robot Operating System) with Gazebo
- Computer Vision with OpenCV
- Control Systems (PID controllers, kinematics)
- Webots/Gazebo simulation

Phase 3: Advanced Integration + AI (9–18 months)
- Deep learning with TensorFlow or PyTorch
- Reinforcement learning for robotics
- SLAM and autonomous navigation
- Human-robot interaction (voice, gestures)
- IoT integration (MQTT, Node-RED)
"""),

    ("2. Project Ideas", """
- Robotic arm with joystick/mobile control
- Color/shapes sorting system using OpenCV
- Autonomous campus delivery bot
- Swarm robotics demo (multiple bots coordination)
- Voice/gesture-controlled wheelchair
- Smart vacuum or pet feeder bot

Tip: Host projects on GitHub with code, diagrams, and videos.
"""),

    ("3. Robotics Job Scope & Career Roles", """
Roles:
- Robotics Software Engineer (ROS, SLAM, AI)
- Mechatronics Engineer (motors, sensors, design)
- Embedded Developer (RTOS, microcontrollers)
- AI/ML Engineer (deep learning + control)
- Vision Engineer (OpenCV, YOLO)

Top Companies:
- Boston Dynamics, Tesla, iRobot, Amazon Robotics, ABB, KUKA, FANUC
"""),

    ("4. Building a Robotics Business", """
Models:
- Product: bots for delivery, surveillance, consumer use
- Services: robotics for agriculture, warehouses, healthcare
- SaaS: robotics cloud control, AI-as-a-service
- EdTech: robotics training for students/schools

Startup Steps:
1. Pick a niche and validate a real-world need
2. Prototype and test it quickly
3. Build a multi-disciplinary team
4. Seek funding (VCs, grants, bootstrapping)
5. Iterate, demo, and launch

Future Trends:
- AI-powered robotics
- Autonomous systems (drones, AGVs)
- Humanoid & assistive robotics
- Robot-as-a-Service and factory automation
""")
]

for title, body in content:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output("Robotics_Career_Roadmap.pdf")
