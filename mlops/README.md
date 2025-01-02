# Cheat Sheet - MLOps

# Table of Contents (ToC)

- [Cheat Sheet - MLOps](#cheat-sheet---mlops)
- [Table of Contents (ToC)](#table-of-contents-toc)
  - [Overview](#overview)
  - [Project Management](#project-management)
  - [Roles overview](#roles-overview)
  - [Roles description](#roles-description)
    - [Data Engineer | Data Scientist | Data Analyst](#data-engineer--data-scientist--data-analyst)
    - [ML Engineer](#ml-engineer)
    - [MLOps Engineer](#mlops-engineer)
  - [Teams](#teams)
    - [AI Factories](#ai-factories)
    - [Data Ops](#data-ops)
    - [Architects](#architects)
    - [Data Processing Solutions (DPS)](#data-processing-solutions-dps)
  - [Here are some guidelines to keep in mind](#here-are-some-guidelines-to-keep-in-mind)
    - [1. Versioning](#1-versioning)
    - [2. Collaboration](#2-collaboration)
    - [3. Testing](#3-testing)
    - [4. Automation](#4-automation)
      - [4.1. CICD](#41-cicd)
      - [4.2. Orchestration and scheduling](#42-orchestration-and-scheduling)
      - [4.3. CT (optional)](#43-ct-optional)
    - [5. Reproducibility](#5-reproducibility)
    - [6. Tracking and logging](#6-tracking-and-logging)
    - [7. Continuous monitoring](#7-continuous-monitoring)
    - [8. Feedback loops](#8-feedback-loops)
    - [9. A/B Testing](#9-ab-testing)


## Overview

xxx


Sources:
- [Youtube - MLOpsWorld](https://www.youtube.com/channel/UCvfUFYIYTbTgxKQNGc2zoqQ)
- [Wind 4 Change - Design Thinking](https://wind4change.com/design-thinking-d-school-stanford-ideo-approach-methodology/?ref=dl-staging-website.ghost.io)
- [DeepLearning AI - Andrew Ng AI Product](https://www.deeplearning.ai/the-batch/issue-279/)

## Project Management

xxx

## Roles overview

Doing ML work well involves a dizzying array of skills, focuses areas and business concerns. We find one useful way to structure this knowledge is by thinking as always of the flow of data.

## Roles description

This section enumerates the roles involved in the creation and management of ML solutions.

### Data Engineer | Data Scientist | Data Analyst

These people understand how to extract, curate, manage, and track data as well as how to extract value from it.

### ML Engineer

They build and manage ML models by using software development guidelines and handling model lifecycle.

### MLOps Engineer

They lead the overall reliability and safety for the deployment of ML models. They improve existing processes for building
and deploying models, propose and manage the metrics to track our performance over time, and develop new software infrastructure
to enforce model reliability. 

## Teams
### AI Factories
Create ML solutions to solve business needs. These are teams mainly composed of data scientists.

### Data Ops
Design and operate the data and ML platforms.

### Architects
Help teams design their solutions and pipelines. For example, teams can benefit from their advice through the design review process.

### Data Processing Solutions (DPS)
Support Data Science Teams to industrialize ML solutions, and data engineers to set up their pipelines.

## Here are some guidelines to keep in mind

MLOps is a paradigm, including aspects like best practices, sets of concepts, as well as a development culture when it comes to the end-to-end conceptualization, implementation, monitoring, deployment, and scalability of machine learning products. 

Most of all, it is an engineering practice that leverages three contributing disciplines: machine learning, software engineering (especially DevOps), and data engineering. MLOps is aimed at productionizing machine learning systems by bridging the gap between development (Dev) and operations (Ops). 

Essentially, MLOps aims to facilitate the creation of machine learning products by leveraging these principles: 
- Versioning of data, model, and code; 
- Testing;
- Automation: CI/CD/CT & Workflow orchestration, 
- Reproducibility;
- Tracking & logging; 
- Monitoring;
- Feedback loops.

### 1. Versioning

Versioning ensures the versioning of data (with delta), model (with mlflow model registry) and code (with Github) to enable not only reproducibility, but also traceability (for compliance and audit reasons).

### 2. Collaboration

Collaboration ensures the possibility to work collaboratively on data, model and code. Besides the technical aspect, this principle emphasize a collaborative and communicative work culture aiming to reduce domain silos between different roles.

To do so, make sure to use the same git workflow mechanism with your partners.

### 3. Testing

Testing can ensure its quality by verifying that it meets the desired specifications, functionality, and performance requirements. This can help detect bugs, errors, or vulnerabilities before the code is deployed, reducing the likelihood of failures or security breaches. It should be covering all the aspects of our ML systems, including the code but also the data and models.

Similarly, a shoe manufacturer can ensure the quality of their products by performing tests on different aspects such as the materials used, durability, and comfort. These tests can help identify any defects or issues before the shoes are shipped to customers, ensuring that they meet the required standards of quality and safety.

### 4. Automation
#### 4.1. CICD

CICD automation proceeds continuous integration (e.g. package, code readability, tests coverage), continuous delivery and the continuous deployment. It carries out the build, test, delivery and deploy steps.

It provides fast feedback to developers regarding the success or failure of certain steps, thus increasing the overall productivity.

#### 4.2. Orchestration and scheduling

Workflow orchestration coordinates the tasks of an ML workflow pipeline according to directed acyclic graphs (DAGs). DAGs define the task execution order by considering relationships and dependencies.

#### 4.3. CT (optional)

Continuous training means periodic or trigger a retraining of the ML model based on new feature data. CT is enabled through the support of a monitoring component, feedback loop and an automated ML workflow pipeline. Continuous training always includes an evaluation run  to access the change in model quality.

### 5. Reproducibility

Reproducibility is the ability to reproduce an ML experiment or rollback to a previous version in order to obtain the exact same results.

### 6. Tracking and logging

Track and log each orchestrated ML workflow task. Tracking and logging is required for each training job iteration (e.g. training date and time, duration) including the model specific metadata (e.g. used parameters and the resulting performance metrics, model lineage : data and code used) to ensure the full traceability of experiments run.

### 7. Continuous monitoring

Continuous monitoring implies the periodic assessment of data, mode, code, infrastructure resources, and model serving performance (e.g. prediction accuracy) to detect potential errors or changes that influence the product quality.

Where Testing ensures that the system (code, data and models) respects the expectations set offline (Build), Monitoring will rather ensure that the system continues to pass these expectations live in a production environment (Run)

### 8. Feedback loops

Multiple feedback loops are required to integrate insights from the quality assessment step into the development or engineering process. 

Production deployment (canary, shadow, blue/green deployment) and online experimentation (e.g. A/B Testing, Smoke testing, MAB testing) are solution in order to collect feedback.

Another feedback loop from the monitoring component (e.g. observing the model, serving performance) to the scheduler to enable the retraining.

### 9. A/B Testing 

xxx