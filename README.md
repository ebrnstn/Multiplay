Elias Bernstein\
Aashish Lalani\
Yuqi Zhu\
Jie Guo\
NETS 213 Final Project Part 2 Deliverable 1

# Multiplay - Crowdsourcing Computer Gaming
#### 1. Users provide input via chat on the Twitch frontend interface (1 point)
Using the game streaming service Twitch (https://www.twitch.tv/), we will stream a game of our choice to the user community. According to Quantcast, Twitch reaches over 20 million people per month, meaning that there are more than enough users available for us to implement our project. To participate, users will simply enter the command of their choice into the chat bar on the side of the stream, which could be anything from 
```
"up"
```
to 
```
"a"
```

#### 2. We will pull the chat stream using Twitch API (2 points)
Next, using the Twitch API, we will pull the chat stream for parsing. This may come in the form of a JSON dictionary or an XML file. We will need to make sure to have an efficient implementation here, as many users will be providing input simultaneously.
#### 3. Using Python scripts, we will aggregate the responses and use QC module to determine what the next input command is (3 points)
Once we have parsed the responses, we will need to aggregate them to get counts of each of the commands that were proposed during the time interval chosen. This will require looping through the stream data pull and making sure that only valid commands are included in the input-selection process. We intend to track invalid commands as well for analysis purposes later. Once we have gotten the counts of all the valid commands, we will select the one to input based on a simple-majority vote. Depending on the game, we may also consider implementing some sort of weighted majority vote mechanism.
####In the QC_and_aggregate.py file, we handle both the quality control and aggregation. A JSON file is passed into this module, where we count the frequency of each command in the quality_control function and then match these elements against a predetermined list of acceptable inputs. For our example, we deemed up, down, left, and right as acceptable inputs, so our frequency list is filtered down to these. Next, we then aggregate by choosing either the element with the highest frequency (was typed the most) in pick_aggregated_move function, or the element that was typed first in the pick_sequential_move function. This is then outputted as the consensus agreement of the crowd.  
#### 4. Using another python script, input that command into the game (4 points)
With the command chosen, we will use another python script to input that command into the game. The game will be running on a computer via an emulator, so we may need to delve into the emulator's source code in order to enable the program to interface with the Twitch input.
#### 5. Twitch broadcasts the game back to users so they can perform the next action (1 point)
This is pretty self-explanatory. After we input the command to the game, Twitch will broadcast the updated gamestate back to users.
#### 6. Evaluate success of users qualitatively (and quantitatively if possible) at a certain interval (3 points)
Ultimately, what we would like to do is evaluate how well users are able to play the game. Our exact evaluation method will depend on the game; if we streaming a game with a score value, for example, we could evaluate the score that users are able to achieve over time and compare this score to the scores of individual users or other comparable data available online. Alternatively, we could perform a more qualitative analysis and just see if users are able to perform well. For example, if we streamed a chess emulator, we could easily tell how well users were playing the game just by observing their progress.
#### 7. Perform data analysis on user inputs (4 points)
In addition to gauging user success, we would also like to analyze user input. Perhaps we could perform sentiment analysis and see how user sentiment tracks game success. Another option might be to see how dispersed the chat inputs are - are many users voting a few times, or are a few users voting many times? Furthermore, we could examine how prevalent groupthink is within the user community.
