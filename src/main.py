#Define the imports
import twitch
import keypresser
t = twitch.Twitch();
k = keypresser.Keypresser();
 
#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = "nets213";
key = "oauth:c20fih2k3bbltnbk3s8cc75buk8eh1";
t.twitch_connect(username, key);
 
#The main loop
while True:
    #Check for new mesasages
    new_messages = t.twitch_recieve_messages();
 
    if not new_messages:
        #No new messages...
        continue
        print "nobody home"
    else:
        for message in new_messages:
            #Wuhu we got a message. Let's extract some details from it
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg);
 
            #This is where you change the keys that shall be pressed and listened to.
            #The code below will simulate the key q if "q" is typed into twitch by someone
            #.. the same thing with "w"
            #Change this to make Twitch fit to your game!
            if msg == "a": k.key_press("a");
            if msg == "s": k.key_press("s");
            if msg == "w": k.key_press("w");
            if msg == "d": k.key_press("d");
            if msg == "r": k.key_press("r");
            if msg == "t": k.key_press("t");
            if msg == "q": k.key_press("q");