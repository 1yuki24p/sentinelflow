# SentinelFlow

I started building SentinelFlow with a fairly simple idea: take the large amount of information sitting inside server and application logs and turn it into something that can actually help identify security problems.

Logs are everywhere in cybersecurity. Every login attempt, HTTP request, error, and suspicious action can leave behind a trail. The difficult part isn't necessarily collecting those logs. It's making sense of them and recognizing when a normal-looking event becomes part of a larger attack pattern.

SentinelFlow is my attempt to explore that problem by building a security log analyzer from the ground up using Python.

## Where It Started

The first version of SentinelFlow is intentionally simple.

It can read structured log files, parse individual events, and look for patterns that could indicate suspicious activity. One of the first things I implemented was failed login detection.

For example, if a log contains several failed login attempts from the same IP address, SentinelFlow can group those events together and flag the activity as a potential brute-force attack.

Instead of manually going through a log file like this:

```text
192.168.1.10 - Failed login
192.168.1.10 - Failed login
192.168.1.10 - Failed login
192.168.1.10 - Failed login
192.168.1.10 - Failed login
```

the analyzer can turn it into a more meaningful security event:

```text
Potential Brute Force Attack Detected

IP Address: 192.168.1.10
Failed Login Attempts: 5
```

It's a small feature, but it represents the basic idea behind the entire project: **turn raw security data into information that is easier to understand and act on.**

## What SentinelFlow Can Do Today

The current version focuses on the fundamentals of log analysis.

It can:

* Parse structured log files
* Detect HTTP errors
* Identify failed login attempts
* Group failed attempts by IP address
* Detect potential brute-force attacks
* Generate basic detection results

There is still a lot to improve, but these features provide the foundation for the next stages of the project.

## Where I Want to Take It

I don't want SentinelFlow to remain just a Python script that searches for a few keywords in a log file.

The long-term goal is to turn it into a small security monitoring and detection platform.

The next step is building a proper detection engine where different types of security detections can operate independently. This would make it possible to add detectors for different attacks without constantly modifying the core application.

From there, I want to introduce incident management, risk scoring, and a database for storing security events.

Eventually, SentinelFlow will have a REST API and a web dashboard so that detected incidents can be viewed and investigated through an interface rather than directly from the terminal.

## Moving Beyond Rules

One of the parts I'm particularly interested in is anomaly detection.

Traditional security detection often relies heavily on predefined rules. Rules are useful, but they also have limitations. Not every attack will follow a predictable pattern, and unusual activity doesn't always fit neatly into a predefined rule.

Once the core detection system is working reliably, I want to experiment with statistical methods and machine learning to see how SentinelFlow can identify unusual behavior that might otherwise go unnoticed.

This is also why scikit-learn is part of the planned technology stack. Machine learning isn't being added just for the sake of using AI. The goal is to first understand the fundamentals of log analysis and detection engineering, then explore where machine learning can actually provide value.

## Roadmap

The project is being developed incrementally.

### Foundation

* Basic log parsing
* Failed login detection
* IP-based grouping
* HTTP error detection
* Brute-force detection
* Improved error handling
* More robust log parsing

### Detection Engine

* Modular detection architecture
* Multiple attack detectors
* Configurable detection rules
* Severity levels
* Risk scoring

### Security Platform

* SQLite database
* Incident management
* REST API
* Authentication
* Web dashboard

### Detection Intelligence

* Anomaly detection
* Statistical analysis
* Machine learning models
* Automated risk scoring

### Deployment and Reliability

* Docker support
* Automated tests
* CI/CD
* Production-ready configuration

## Technology

The project is currently being built primarily with Python.

The planned stack includes:

* Python
* SQLite
* FastAPI
* pytest
* scikit-learn
* Docker

## Why I'm Building It

SentinelFlow is also a learning project.

Rather than simply reading about SIEM systems, detection engineering, and security monitoring, I wanted to build something that forces me to understand how these systems actually work.

Building the project means dealing with real problems: parsing inconsistent data, designing detection rules, reducing false positives, storing events, assigning risk, and eventually figuring out how machine learning can fit into the system.

The project is still in its early stages, and there is a long way to go.

For now, I'm focusing on getting the fundamentals right and building SentinelFlow one feature at a time.

## Disclaimer

SentinelFlow is intended for defensive security research, education, and analysis of log data from systems you own or are authorized to monitor.

It should not be used to monitor or analyze systems without appropriate authorization.
