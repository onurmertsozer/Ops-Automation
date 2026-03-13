# Ops-Automation
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onurmertsozer/Ops-Automation/blob/main/launh_manifest.ipynb)

Automated readiness assessment logic for regional robotics fleet deployment
Ops Automation

This repository demonstrates a Python based decision engine designed to automate regional launch readiness assessments. Drawing from my experience in scaling autonomous robot fleets across Europe, I built this tool to replace manual, error-prone spreadsheets with a logic driven, scalable framework.

The Problem: In high-growth scale-ups, tracking "Go/No-Go" status across multiple regions involves managing complex dependencies (Legal, Technical, and Partner readiness). Manual tracking often leads to oversight of critical blockers.

The Solution: This orchestrator applies a strict Dependency Logic to a fleet manifest. It identifies exactly where a launch is stalled—whether it's a legal compliance issue or a hardware calibration delay.

Uses Pandas to process regional data from an external CSV, allowing for 100+ cities to be audited in milliseconds.

Includes a pre-processing step to clean "dirty" data (whitespace stripping and type-casting).

Instead of a simple "Error," the system generates a detailed Missing Milestones report for operational teams.

Privacy & Confidentiality
All data (city names, partners, and readiness metrics) in this repository is completely synthetic and created for demonstration. No proprietary information from  employers is used. This project is a showcase of software logic and architectural mindset.

The following report avaliable in launch_manifest.jpynb


