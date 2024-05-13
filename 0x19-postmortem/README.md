# Postmortem: Safaricom Internet Outage Incident

![WhatsApp Image 2024-05-13 at 20 21 45_97eefded](https://github.com/Estherkiguru/alx-system_engineering-devops/assets/138945105/3df648d2-e023-4798-bbd0-54986fc85bd0)

## Issue Summary:

**Duration:** May 12, 2024, from 7:00 PM to 9:00 PM (UTC+3)

**Impact:** Safaricom customers experienced significantly reduced internet speeds due to an outage in one of the undersea cables delivering internet traffic in and out of Kenya. Approximately 70% of users were affected, reporting slow loading times and difficulties accessing online services.

**Root Cause:** Disruption in the undersea cable infrastructure, interrupting internet traffic flow to and from Kenya.

## Timeline:

- **7:00 PM:** Issue detected as Safaricom customers began reporting slow internet speeds and difficulties accessing online services.
- **7:15 PM:** Engineering team notified of the issue and began investigating potential causes.
- **7:30 PM:** Initial investigation focused on internal server issues, suspecting server damage due to power outages.
- **7:35 PM:** Issue escalated to senior engineers for further assessment.
- **7:45 PM:** Senior engineers identified the undersea cable outage as the root cause of the internet disruption and initiated contingency measures.
- **8:00 PM:** Redundancy measures activated to mitigate service interruption and maintain connectivity while awaiting cable restoration.
- **8:30 PM:** Ongoing complaints from customers prompted Safaricom to provide regular updates on restoration efforts.
- **9:00 PM:** Internet services gradually restored as the undersea cable repair efforts were successful.

## Root Cause and Resolution:

**Root Cause:** The root cause was identified as disruption in the undersea cable infrastructure interrupted the flow of internet traffic to and from Kenya, resulting in reduced internet speeds for Safaricom customers.

**Resolution:** Safaricom activated redundancy measures to minimize service interruption and maintain connectivity while awaiting the full restoration of the undersea cable. Once repairs were completed, internet services were gradually restored to normal levels.
Corrective and Preventative Measures:

## Improvements/Fixes:

- Enhance monitoring systems to detect undersea cable disruptions more quickly in the future.
- Investigate alternative communication paths to diversify internet traffic routes and reduce reliance on single points of failure.

 ## Tasks  to address the issue:
 
 - Conduct a comprehensive review of undersea cable infrastructure to identify vulnerabilities and implement resilience measures.
 - Develop contingency plans for handling future undersea cable outages, including communication strategies and customer support measures.
 - Collaborate with international partners to improve undersea cable maintenance and response protocols to expedite restoration efforts during outages.

