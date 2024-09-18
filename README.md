# Overview
This project involves designing and implementing a database system to manage research grants, proposals, reviewers, and related processes. The system uses a normalized database schema to ensure data integrity and streamline grant management workflows. The project includes a Python application for database interactions and automates key aspects of the grant review process.
# Features
- **Database Schema**
    - Models relationships between researchers, grant proposals, competitions, and reviewers.
- **Schema Design**
    - Normalized to BCNF (Boyce-Codd Normal Form) to eliminate redundancy and anomalies.
- **Path cost optimization** using step costs and penalties for turns.
- Optional behaviors: "StayLeft" and "StayTop" cost functions to influence the agent's path.
- Dynamic visualization of the agent’s path and explored rooms on the grid.
