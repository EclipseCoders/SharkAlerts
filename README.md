# SharkAlerts
Stay updated on Shark Sightings with SharkAlerts via SMS, powered by Twilio! Developed for Shark Hacks 2 by EclipseCoders, lead by Anson Wong.

## Inspiration
To us, sharks have always been fascinating and beautiful creatures whose portrayal has been negatively skewed by media, and while it is true that they are disproportionately feared in relation to how many fatalities they cause every year, it is still safer for both humans and sharks to avoid contact with each other if possible. Our team frequents beaches during the summer, and although marine creatures are not the main safety concern for us, this is definitely not the case for tourists and residents of waters that sharks frequent. Thus, we were inspired to create an application that allows users to stay informed of shark sightings to avoid the risk of running into one while doing any recreational activities in bodies of waters that sharks frequent.
Our teammate Anson Wong was also nearly an unfortunate victim of a shark attack due to the phenomenon of mislabeled identity as sharks tend to mistake humans for seals according to scientific research. Fortunately, our colleague and friend made it out unscathed; however, this led us to the further realization that man and beast should be separated, ultimately inspiring us to develop SharkAlerts.

## What it does
This application allows users who sign up for the service to receive SMS notifications from authorities or whoever is running the application to minimize the risk of users having close encounters of Sharks whenever possible.

## How we built it
We built this application with React and a custom-made API using Flask along with our MongoDB database. The backend is also supplemented with the Twilio API to send users SMS messages.

## Challenges we ran into
One of the main challenges we ran into while designing this application was figuring out who would be providing information about the shark sightings, as this would directly affect the implementation of our application. This was a hurdle since we needed to decide if regular users should have access to the functionality to send alerts to all other users in the case that they themselves saw a shark that they would want to report. After a lengthy debate, we decided that this could introduce spamming issues, and that it would make sense for these users to report the sighting to whoever is actually running the application so that they can relay the message to other users, since they would likely be someone who has access to a wider array of tools to help them spot sharks easier (such as the Coast Guard).

## Accomplishments that we're proud of
We are proud that we managed to create this application in a short amount of time as well as collaborating effectively to narrow down our originally abundant number of ideas brainstormed to the Shark Alert application! We also take pride in the fact that we learned how to utilize the Twilio API in a short amount of time as some members of our team never had experience with it prior to this hackathon!

## What we learned
We learned about many things related to programming, but the more interesting thing we learned about while participating in this hackathon were some incredible shark tidbits. We were truly not aware that the number of shark fatalities every year was so low compared to our original estimates! One fun fact that we learned was that you actually have a higher chance of being killed by a vending machine than a shark, which makes sense upon reflection as you would interact with vending machines far more than sharks but it is still such a ridiculous statement to be able to say!

## What's next for SharkAlerts
We plan on allowing users to specify the geographic region on their map that they would like to receive alerts for, as this could be useful for users who are travel a lot, especially users that like diving or snorkeling as they are the ones that would be the most likely to encounter sharks on their excursions!
