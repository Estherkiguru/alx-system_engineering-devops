![2-secured_and_monitored_web_infrastructure](https://github.com/Estherkiguru/alx-system_engineering-devops/assets/138945105/0753b7ac-ab9b-496b-be8c-5f763755c332)


**Infrastructure:**

This three-server web infrastructure hosts www.foobar.com, emphasizing security, encrypted traffic, and efficient monitoring.

**Security Measures:**

Firewalls: Three firewalls are implemented to secure the network, acting as intermediaries between the internal and external networks. They block incoming traffic from unwanted and unauthorized users.

**Encryption and SSL:**

SSL Certificate: An SSL certificate is used to encrypt traffic between web servers and the external network, preventing potential threats like man-in-the-middle attacks and network sniffing. This ensures privacy, integrity, and identification.

**Monitoring:**

Monitoring Clients: Three monitoring clients, acting as data collectors for services like Sumo Logic, are in place to monitor servers and the external network. They analyze performance, measure health, and alert administrators of any deviations. Key metrics about server operations are provided, including accessibility, response time, and potential issues like security vulnerabilities.

**Identified Issues:**

-SSL Termination at Load Balancer:
Terminating SSL at the load balancer can create a single point of failure and raise security concerns.

-Single MySQL Server:
Having only one MySQL server is not scalable and poses a single point of failure for write operations..

-Servers with Same Components:
Uniform servers with the same components may lead to contention for resources, resulting in poor performance and difficulty in identifying the source of problems.
