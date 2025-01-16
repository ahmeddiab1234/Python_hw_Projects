# HW - 4 - OOP - inhertance - Medium - Irrelevant!

"""

Approach 1 

Each app periodically contacts the server to see if there are new notifications or not
- Then Game site provide an API to be contacted through it
- Each mobile/desktop/tablet send/receive request/response


Advantages

- this approach is simple to implementation and display on both the server and client sides
- ant there is scalabality for clients thay control the frequency of requests, balance data usage


Disadvantages

- the client may poll even no updates that will cause ineffiecient resource usage and wasting bandwidth and server resource
- there is millions of users polling frequently can create high server traffic


"""

"""

Approach 2

When user opens the application, a registration message is sent to the game
- Whenever server has a new message, it iterates on whoever registered and send msg

Advantages

- messages are sent immediately to players that imporove the user experience
- the server will send message only when there are update that cause efficinet resource usage and reduce unnecessary traffic

"""

"""

use option 1 when Small teams or limited resources are available and Small teams or limited resources are available
uss option 2 when The infrastructure can handle the complexity and scalability challenges.

"""

