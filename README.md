# OneHacks-Focus-Pocus
Inspiration:
As a result of the work from home situation that started two years ago, we have had to rely on home technology for our work. Despite the reduction in COVID cases, some corporations loved the convenience of the work-from-home model and have decided to keep it. However, performing professional work in a casual environment such as a bedroom can cause distractions. Additionally, for teens like me, we have been so used to wasting time in quarantine that I believe a focus tracker at this stage would be helpful. So I developed Part 1 which tracks facial movements to ensure tasks are done one at a time in an orderly fashion. 

What it does:
This product utilizes facial recognition from haar cascades to track the position of the face on the screen. Typically, in the middle of a task, I might get distracted by my phone or by what is happening outside the window. The code is able to detect a change in position of my face and gives me a 5 second countdown to come back to the task I am supposed to be working on. If I don’t move back to my original position by that time, it will log how long I stayed on focus and start a new session. This game-like feature is meant for users to take this as a challenge and strive for the best scores possible. 

How I built it:
This software was built completely in the python language. This project is primarily AI based as haar cascades was used for the facial recognition classifier training. I used VSCode for this project. 

Challenges we ran into:
At one point, the text I wanted to insert in the frames did not last for more than a second even though I did not specify that to be the case. It took me 4 whole hours to fix issues relating to that user interface. Additionally at some points, the face detection classifier did not do its job properly so I needed to spend some time changing the parameters.

Accomplishments that I’m proud of:
I believe that this is a product that I will actually end up using in my daily life as it will definitely help. I am proud that I was able to build a product that could impact many people’s lives that has not really been done before.

What I learned:
Overall, I learned more about the different functions that are available in computer vision and was able to build my knowledge base on that. Additionally, persistence and working through this challenge were additional skills that definitely made an impact. 

Whats next:
Part 2 of course.
Well it would include access to browser data to prevent distractions from devices and not just the environment. Being able to scale this product into a web app or mobile app with a server would also be cool. Finding more accurate face recognition models and finding additional GPU would also make a difference. 
