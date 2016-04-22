#Define the imports
import time
from time import gmtime, strftime
import twitch
import keypresser
t = twitch.Twitch();
k = keypresser.Keypresser();
 
#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = "nets213";
key = "oauth:c20fih2k3bbltnbk3s8cc75buk8eh1";
t.twitch_connect(username, key);
new_messages = []
counter = 0
valid_keys = ['up','down','left','right']

with open('chat_log.txt','a') as f:


    #The main loop
    while True:
        #Check for new mesasages
        new_message = t.twitch_recieve_messages();
        if new_message:
            for item in new_message:
                new_messages.append((item, strftime("%d %b %Y %H:%M:%S", gmtime())))
                counter += 1

        if (counter == 5):
            counter = 0
            freqs = {};
         
            # if not new_messages:
            #     #No new messages...
            #     continue
            #     print "nobody home"
            # else:
            key_f = ''
            max_f = 0
            # print len(new_messages)
            for pair in new_messages:
                message = pair[0]
                #Wuhu we got a message. Let's extract some details from it
                msg = message['message'].lower()
                username = message['username']
                timestamp = pair[1]

                output = "timestamp: " + timestamp + " | username: " + username + " | message: " + msg + "\n" 
                print output
                f.write(output)

                # print(username + ": " + msg);

                if msg not in freqs:
                    freqs[msg] = 0;
                freqs[msg] += 1

                for key in freqs:
                    if freqs[key] > max_f:
                        if key in valid_keys:
                            max_f = freqs[key]
                            key_f = key
     
            #This is where you change the keys that shall be pressed and listened to.
            #The code below will simulate the key q if "q" is typed into twitch by someone
            #.. the same thing with "w"
            #Change this to make Twitch fit to your game!
            # if key_f == "a": k.key_press("a");
            # if key_f == "s": k.key_press("s");
            # if key_f == "w": k.key_press("w");
            # if key_f == "d": k.key_press("d");
            # if key_f == "r": k.key_press("r");
            # if key_f == "t": k.key_press("t");
            # if key_f == "q": k.key_press("q");
            if key_f != '' :
                if key_f == 'up':
                    k.key_press('{UP}')
                if key_f == 'down':
                    k.key_press('{DOWN}')
                if key_f == 'left':
                    k.key_press('{LEFT}')
                if key_f == 'right':
                    k.key_press('{RIGHT}')


            print (key_f)
            new_messages = []
