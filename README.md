# Inspiration, Original Ideas
ElevateTogether connects mentors with students to help teach valuable skills in several subjects. As the world becomes more socially connected online, it is more important than ever to provide opportunities for educational growth. 
# How To Use It
Students and mentors can view a list of people, along with the skills they are willing to learn and teach. They can connect with each other and start contacting each other via the chat feature. 
# How we built it
We used Django on the backend of the project. This encompassed creating a chat server with Channels (a pip package) and Docker as well. On the frontend we styled it with bootstrap and HTML/CSS/JS, (along with our own creativity 😉). The whole project is scalable and does not require much work to be ready for a production based environment 💪💪💪.
# Challenges We Ran Into
## Backend
Setting up the chat server was hard; we ran into many bugs and had to get situated with websockets, which behave differently when compared to regular REST APIs. Also, setting up Docker and Redis on multiple machines was no easy feat either. 
## Workflow
We used Git to collaborate and create the project together. However, merge conflicts emerged, which took up precious time that could have been used on the project. Next time around we would still use Git, but just be more careful of what we push out to the rest of the team.
# Accomplishments
We were able to build out a full backend and frontend, within the time limit, with only two people! Also, our codebase is relatively clean and commented, not something every project can say.
# What We Learned
Programming a project in 24 hours is tough! Especially one that has a frontend and backend. Next time around we may opt for a BaaS (backend as a service) such as FireBase to speed things up. 

That said, we did learned an immense amount about Django. Resolving migration conflicts, setting up models and squashing bugs made us more experienced with the framework. We can definitely aim for a more complex project next time if we decide to do so.
# What's Next For ElevateTogether
ElevateTogether has many exciting updates planned. For one, a video calling feature (similar to Discord or Zoom) is in the works. This would allow users to connect easier while also picking up skills faster.

We are also planning on extending the selection of topics to learn. While 6 topics may seem like a lot, more topics will ultimately attract more people to the platform, a net positive for everyone. 