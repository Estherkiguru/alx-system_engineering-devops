Simple Web Infrastructure for www.foobar.com:

This web infrastructure serves the website accessible via www.foobar.com. When a user enters the URL "www.foobar.com" into their web browser, the browser initiates a DNS query to determine the IP address associated with the domain. In this case, the DNS entry for "www.foobar.com" is a "www" record pointing to the IP address 8.8.8.8.

Infrastructure specifics:
What is a server.
It is a computer/software system that responds to clients requests,processes the request, executes code and delivers responses to users.

Role of Domain name.
A domain name serves as a user-friendly address,www.foobar.com, acting as the entry point for users to access the website. It functions by translating  human-readable domain name into the corresponding IP address through the Domain Name System(DNS).

Type of DNS record in www.foobar.com
The DNS record for www.foobar.com is an A record that maps the www subdomain to the precise IPV4 address of the server.

Role of the web server
Manages incoming HTTP request from clients and manages the delivery of web content.

Role of application server
Executes and manages the web applications code, handling dynamic content and generating responses for user requests.

Role of the database
Stores and manages structured data allowing the application to retrieve, update and organize information.

What the server uses to communicate with the client.
The server uses HTTP/HTTPS protocols to communicate with the computer of the user requesting the website.

Infrastructure issues:
Single Point of Failure(SPOF):
This infrastructure has several SPOF such as if the MySQL database server is down leading to the entire system being inaccessible.

Downtime during maintenance:
This challenge arises during maintenance activity when deploying new code that necessitates restarting the web server.

Scalability Challenge:
This infrastructure may encounter difficulties in scaling effectively to handle a surge in incoming traffic posing a risk of performance degradation/downtime during high user activity periods.


