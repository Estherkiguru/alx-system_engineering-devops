![image](https://github.com/Estherkiguru/alx-system_engineering-devops/assets/138945105/8f982afe-994f-4ad9-863e-73a6c6c25f1d)


**Distributed Web Infrastructure for www.foobar.com**

In this distributed web infrastructure, the primary goal is to optimize the traffic distribution to the primary server by introducing a replica server facilitated by an HAProxy load balancer. This infrastructure encompasses various components with specific configurations and functionalities.

**Load Balancing (HAProxy):**

The HAProxy load balancer is configured with the Round Robin algorithm, designed to evenly distribute incoming requests among servers based on their weights. This dynamic algorithm allows real-time adjustments to the weights assigned to servers, ensuring smooth and fair distribution. The load balancer is set up in an Active-Passive configuration, where one server is active while the other remains on standby. This setup aims to prevent overloading a single node, and the standby server becomes active in the event of the primary node's inactivity.

**Nginx Web Server:**

The Nginx web server serves as the gateway for handling static content, such as images and CSS, and acts as a reverse proxy for dynamic content directed to the application server. It plays a crucial role in efficiently serving static content and delegating dynamic content processing to the application server.

**Application Server:**

The application server is responsible for hosting the application's code base, managing client requests, and generating the required responses. It executes the application logic, communicates with the database, and ensures the seamless functioning of dynamic content.

**SQL-Based Database (Primary-Replica Cluster):**

The database is configured as a Primary-Replica (Master-Slave) cluster. The Primary server manages both read and write operations, while the Replica server is limited to read operations. Data synchronization occurs whenever a write operation is executed on the Primary server. This setup minimizes read traffic to the Primary node, enhancing performance.

**Issues with the Infrastructure:**

Despite the sophisticated design, there are identified issues in the infrastructure. Notably, there are single points of failure (SPOFs) in components such as the Primary MySQL database server, the server housing the load balancer, and the application server connecting to the primary database. Security concerns include the absence of SSL encryption, leaving transmitted data vulnerable to eavesdropping, and the lack of a firewall, making it challenging to block unauthorized IPs. Additionally, the absence of a monitoring mechanism hampers the ability to recognize and address issues promptly.

