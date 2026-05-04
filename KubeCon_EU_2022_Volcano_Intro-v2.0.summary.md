# KubeCon EU 2022 Volcano Intro v2.0 — Processed Summary

## PDF metadata

- **Title:** PowerPoint Presentation
- **Author:** Alex Contini
- **Creator/Producer:** Microsoft PowerPoint 2013
- **Created/Modified:** 2022-05-06
- **Pages:** 24
- **File size:** 3,382,643 bytes
- **PDF version:** 1.5
- **Encrypted:** No

## Main topic

The slide deck introduces **Volcano**, a cloud-native batch system for Kubernetes workloads such as HPC, Big Data, and AI/ML.

## Key points

- Cloud-native infrastructure is increasingly used to unify fragmented HPC, Big Data, and AI stacks and improve resource utilization.
- Volcano provides Kubernetes-native batch scheduling capabilities through components such as:
  - Volcano Scheduler
  - Volcano Controller
  - Jobs
  - Queues
  - JobFlow
  - Federation support across clusters
- Project status at the time of the deck:
  - Created March 2019
  - CNCF Sandbox in April 2020
  - CNCF Incubator in April 2022
  - Around 2.3k GitHub stars and 350+ contributors
  - Adopted by 50+ enterprises in production
- Volcano supports batch-job features such as:
  - `minAvailable` gang scheduling semantics
  - MPI-style jobs
  - SSH and service plugins
  - Job restart/complete policies
  - Queue-based resource management
  - Capacity, guarantees, and resource reclaiming
  - Fair-share scheduling across queues, namespaces, users, and jobs
  - Elastic training jobs with minimum and maximum pod ranges
  - Task topology scheduling
  - SLA/waiting-time handling for large jobs
- The deck references Spark integration work: **SPARK-36057: Support volcano/alternative schedulers**.
- Use cases shown include AI, transcoding, Big Data, microservices, large-scale node management, model training pipelines, and offline HPC jobs.
- Community links:
  - Website: https://volcano.sh/en/
  - GitHub: https://github.com/volcano-sh
  - Slack: https://volcano-sh.slack.com

## Extracted files

- Full extracted text: `KubeCon_EU_2022_Volcano_Intro-v2.0.extracted.txt`
- This summary: `KubeCon_EU_2022_Volcano_Intro-v2.0.summary.md`

## Notes

Some slides are diagram-heavy or use embedded PowerPoint symbols, so plain-text extraction is sparse on those pages.
