[![Docker-Docker-Compose Logo](https://static.codingforentrepreneurs.com/media/projects/docker-and-docker-compose/images/share/Docker__Docker_Compose.jpg)](https://www.codingforentrepreneurs.com/projects/docker-and-docker-compose)

# [Docker & Docker Compose](https://www.codingforentrepreneurs.com/projects/docker-and-docker-compose)


**Docker** helps us isolate our apps from everything else. It's *almost* as if our apps have their very own computer and I think that's pretty cool.

**Docker Compose** helps us build local networks with many apps attached to it. 

This series will show you the fundamentals of using both in together. 

But why?

Let's pretend I need Django, Express.js, and FastAPI to run on the *same domain*.  Django will handle all the primary routes, Express.js will handle `/notifications` routes, FastAPI will handle the `/api/` routes. 

But how do we run these all on the *same domain*? **nginx** to the rescue! That's true, nginx can help us run all of these apps as illustrated above.

But there's another problem. How can I use Docker for each of these apps?

This is where **docker compose** comes in. **Docker Compose** will orchestrate containers in a network of their own. 

**Uh oh! This sounds complicated...**

That's true. This does sound complicated but it's not. It's really just a bunch of configuration to get this stuff working correctly. Once you understand it fully, you'll be ready to use it in all kinds of projects.

The goal of this series is to unpack what I mentioned above while building something real. 
