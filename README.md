🛠️ GearGuard – The Ultimate Maintenance Tracker
📌 Project Overview

GearGuard is a custom Odoo module designed to manage and track organizational assets and their maintenance lifecycle.
It enables companies to connect Equipment, Maintenance Teams, and Maintenance Requests into a single, structured system.

The module supports both corrective (breakdown) and preventive (scheduled) maintenance workflows, ensuring efficient asset management and technician coordination.

🎯 Objective

To develop a maintenance management system that allows a company to:

Track company assets (machines, vehicles, computers, etc.)

Assign responsibility to maintenance teams and technicians

Manage maintenance requests from creation to completion

Provide an intuitive Kanban and Calendar-based user experience

🧩 Core Functional Areas
1️⃣ Equipment Management

The Equipment module acts as a central repository of all company assets.

Key Features:

Equipment tracking by:

Department

Employee ownership

Assignment of a Maintenance Team to each equipment

Key fields include:

Equipment Name

Serial Number

Purchase Date

Warranty Information

Physical Location

Smart button on equipment form:

Opens all maintenance requests related to the equipment

Displays count of active (open) requests

Scrap indicator:

Equipment is marked unusable when scrapped via maintenance workflow

2️⃣ Maintenance Teams

The system supports multiple specialized maintenance teams.

Features:

Team creation (e.g., Mechanics, Electricians, IT Support)

Assignment of users (technicians) to teams

Requests are associated with a specific maintenance team

Teams define responsibility and workflow ownership

3️⃣ Maintenance Requests

Maintenance Requests represent the core transactional workflow.

Request Types:

Corrective – Unplanned breakdown repairs

Preventive – Planned routine maintenance

Key Fields:

Subject / Description

Equipment

Maintenance Team

Assigned Technician

Scheduled Date

Duration (Hours Spent)

🔁 Functional Workflows
🔧 Flow 1: Breakdown (Corrective Maintenance)

Any user creates a maintenance request

On selecting equipment:

Maintenance Team is auto-filled

Request starts in New stage

Technician or manager assigns the request

Stage moves to In Progress

Technician completes work and records duration

Stage moves to Repaired

📅 Flow 2: Routine Checkup (Preventive Maintenance)

Manager creates a request with type Preventive

Scheduled date is defined

Request appears in Calendar View

Technician uses calendar to track upcoming maintenance tasks

🖥️ User Interface & Views
🔹 Kanban Board

Default working area for technicians

Grouped by stages:

New

In Progress

Repaired

Scrap

Drag & drop between stages

Technician avatar displayed on cards

Overdue requests visually highlighted

🔹 Calendar View

Displays Preventive Maintenance requests

Based on scheduled date

Allows easy scheduling and planning

🔹 Reports (Optional)

Pivot / Graph views for:

Requests per team

Requests per equipment category

⚙️ Automation & Smart Features

Auto-fill maintenance team based on selected equipment

Team-based technician assignment

Smart button on equipment for related maintenance

Scrap logic:

Moving request to Scrap marks equipment unusable

Logs activity for auditability

🔐 Security & Access Control
User Roles

Technician (User):

Can create, view, and update maintenance requests

Cannot delete records

Read-only access to equipment

Manager:

Full access to equipment, teams, and requests

Can assign requests and scrap equipment

Access rights are configured using Odoo Access Control Lists (ACLs) via the UI.

🧪 Testing Scenarios

Login as technician and manage assigned requests

Login as manager and oversee all maintenance activity

Verify calendar scheduling for preventive maintenance

Confirm scrap logic updates equipment status

🏁 Conclusion

GearGuard delivers a structured, Odoo-native maintenance tracking solution that aligns with real-world asset management workflows.
By combining automation, role-based access, and intuitive views, the module transforms basic maintenance tracking into a smart, scalable system.
