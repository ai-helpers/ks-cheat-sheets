# Cheat Sheet - MLOps

# Table of Contents (ToC)

- [Cheat Sheet - MLOps](#cheat-sheet---mlops)
- [Table of Contents (ToC)](#table-of-contents-toc)
  - [Overview](#overview)
  - [Courses](#courses)
  - [Standards - SPDX](#standards---spdx)
  - [Project Management](#project-management)
  - [Roles overview](#roles-overview)
  - [Roles description](#roles-description)
  - [Here are some guidelines to keep in mind](#here-are-some-guidelines-to-keep-in-mind)


## Overview

Sources:
- [Youtube - MLOps World](https://www.youtube.com/channel/UCvfUFYIYTbTgxKQNGc2zoqQ)
- [Wind 4 Change - Design Thinking](https://wind4change.com/design-thinking-d-school-stanford-ideo-approach-methodology/?ref=dl-staging-website.ghost.io)
- [DeepLearning AI - Andrew Ng AI Product](https://www.deeplearning.ai/the-batch/issue-279/)

## Courses

- [LinkedIn Learning -  MLOps with Databricks](https://www.linkedin.com/learning/mlops-with-databricks)

## Articles 
- [RICE - priorization framework](https://marily.substack.com/p/rice-a-a-prioritization-framework?utm_source=post-email-title&publication_id=547073&post_id=155290254&utm_campaign=email-post-title&isFreemail=true&r=1gsxm1&triedRedirect=true&utm_medium=email)
- [Keynote - ML Engineering rules](https://media.licdn.com/dms/document/media/v2/D4D1FAQFyZb9o5dsizw/feedshare-document-pdf-analyzed/feedshare-document-pdf-analyzed/0/1732900953798?e=1738195200&v=beta&t=EVTcodB7NwaJXHqLieI8UO3uN9VVu6DwSYvaeMpoaIo)

## Standards - SPDX

- SPDX AI: https://spdx.dev/learn/areas-of-interest/ai/
- AI Factsheets: https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/factsheets-model-inventory.html?context=cpdaas
  - https://s3.us.cloud-object-storage.appdomain.cloud/aifactsheets-client/doc_files/Main/installation.html
  - https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/df_AI_create_model.html?context=cpdaas
  - https://docs.docker.com/build/ci/github-actions/attestations/
  - https://github.com/dktunited/.github/blob/5a0f62cdec0d311d0583f97892b7cbc38b794db0/.github/workflows/build-maven-docker.yaml#L111
  - https://spdx.dev/use/spdx-tools/

## Principe of ML Operations

![image](https://github.com/user-attachments/assets/37495488-32c2-44d6-a647-ee0f719da664)
_Figure: strongly inspired from [data-engineering-helpers/architecture-principles](https://github.com/data-engineering-helpers/architecture-principles?tab=readme-ov-file#data-engineering)_

## Project Management

POC | MVP | Pilot | Run

## Roles overview

Doing ML work well involves a dizzying array of skills, focuses areas and business concerns. We find one useful way to structure this knowledge is by thinking as always of the flow of data.

## Roles description

This section enumerates the roles involved in the creation and management of ML solutions.

- Data Engineer | Data Scientist | Data Analyst: These people understand how to extract, curate, manage, and track data as well as how to extract value from it.
- ML Engineer: They build and manage ML models by using software development guidelines and handling model lifecycle.
- MLOps Engineer: They lead the overall reliability and safety for the deployment of ML models. They improve existing processes for building
and deploying models, propose and manage the metrics to track our performance over time, and develop new software infrastructure
to enforce model reliability. 

## Here are some guidelines to keep in mind

MLOps is a paradigm, including aspects like best practices, sets of concepts, as well as a development culture when it comes to the end-to-end conceptualization, implementation, monitoring, deployment, and scalability of machine learning products. 

Most of all, it is an engineering practice that leverages three contributing disciplines: machine learning, software engineering (especially DevOps), and data engineering. MLOps is aimed at productionizing machine learning systems by bridging the gap between development (Dev) and operations (Ops). 

Essentially, MLOps aims to facilitate the creation of machine learning products by leveraging these principles: 

**1. Versioning:** versioning ensures the versioning of data (with delta), model (with mlflow model registry) and code (with Github) to enable not only reproducibility, but also traceability (for compliance and audit reasons).
**2. Collaboration:** collaboration ensures the possibility to work collaboratively on data, model and code. Besides the technical aspect, this principle emphasize a collaborative and communicative work culture aiming to reduce domain silos between different roles.
To do so, make sure to use the same git workflow mechanism with your partners.
**3. Testing:** Testing can ensure its quality by verifying that it meets the desired specifications, functionality, and performance requirements. This can help detect bugs, errors, or vulnerabilities before the code is deployed, reducing the likelihood of failures or security breaches. It should be covering all the aspects of our ML systems, including the code but also the data and models.
Similarly, a shoe manufacturer can ensure the quality of their products by performing tests on different aspects such as the materials used, durability, and comfort. These tests can help identify any defects or issues before the shoes are shipped to customers, ensuring that they meet the required standards of quality and safety.
**4. Automation**
  - _4.1. CICD:_ CICD automation proceeds continuous integration (e.g. package, code readability, tests coverage), continuous delivery and the continuous deployment. It carries out the build, test, delivery and deploy steps.
  It provides fast feedback to developers regarding the success or failure of certain steps, thus increasing the overall productivity.
  - _4.2. Orchestration and scheduling:_ workflow orchestration coordinates the tasks of an ML workflow pipeline according to directed acyclic graphs (DAGs). DAGs define the task execution order by considering relationships and dependencies.
  - _4.3. CT (optional):_ continuous training means periodic or trigger a retraining of the ML model based on new feature data. CT is enabled through the support of a monitoring component, feedback loop and an automated ML workflow pipeline. Continuous training always includes an evaluation run  to access the change in model quality.
5. **Reproducibility:** reproducibility is the ability to reproduce an ML experiment or rollback to a previous version in order to obtain the exact same results.
6. **Tracking and logging:** track and log each orchestrated ML workflow task. Tracking and logging is required for each training job iteration (e.g. training date and time, duration) including the model specific metadata (e.g. used parameters and the resulting performance metrics, model lineage : data and code used) to ensure the full traceability of experiments run.
**7. Continuous monitoring:** Continuous monitoring implies the periodic assessment of data, mode, code, infrastructure resources, and model serving performance (e.g. prediction accuracy) to detect potential errors or changes that influence the product quality.
Where Testing ensures that the system (code, data and models) respects the expectations set offline (Build), Monitoring will rather ensure that the system continues to pass these expectations live in a production environment (Run)
**8. Feedback loops:** Multiple feedback loops are required to integrate insights from the quality assessment step into the development or engineering process. 
Production deployment (canary, shadow, blue/green deployment) and online experimentation (e.g. A/B Testing, Smoke testing, MAB testing) are solution in order to collect feedback.
Another feedback loop from the monitoring component (e.g. observing the model, serving performance) to the scheduler to enable the retraining.
**9. A/B Testing: xxx**
