from flask import Flask, render_template, request, jsonify
import subprocess
from subprocess import check_call
import aiml as aiml
import os

kernel = aiml.Kernel()

from capstone2 import response,greeting,GREETING_INPUTS,GREETING_RESPONSES


def substitute_key(msg):
	msg = msg.lower()
	if("msis" in msg):
		msg = msg.replace("msis","Master of Science in Information Systems")
	elif("msba" in msg):
		msg = msg.replace("msba","Master of Science in Business Analytics")
	elif("msfa" in msg):
		msg = msg.replace("msfa","Master of Science in Financial Analytics")
	elif("mba" in msg):
		msg = msg.replace("mba","Master of Science in Business Administration")
	return(msg)

def load_kern(forcereload):
	if os.path.isfile("bot_brain.brn") and not forcereload:
		kernel.bootstrap(brainFile= "bot_brain.brn")
	else:
		kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
		kernel.saveBrain("bot_brain.brn")



app = Flask(__name__)
#app.config['DEBUG']=True
@app.route("/")
def hello():
	load_kern(False)
	return render_template('chat.html')



@app.route("/ask", methods=['POST','GET'])
def ask():
    ans=[]
    message = str(request.form['chatmessage'])
    message1 = substitute_key(message)
    
    print("message1 = "+ str(message1))
    if(message1!='bye'):
    	if (message1=='thanks' or message1=='thank you' ):
    		return jsonify({"status":"ok","answer":"You're Welcome!"})
    	else:
    		if(greeting(message1)!=None):
    			ans=greeting(message1)
    			return jsonify({"status":"ok","answer":ans})
    		else:
    			ans = response(message1)
                print(ans)
                print("ans0" + str(ans[0]))
                print("ans1" + str(ans[1]))
                print("ans2" + str(ans[2]))
                print("ans3" + str(ans[3]))
                print("ans4" + str(ans[4]))
                print("ans5" + str(ans[5]))
                print("ans6" + str(ans[6]))
                                           
                
                return jsonify({"status":"ok","answer1":ans[0],"answer2":ans[3],"url1":ans[1],"url2":ans[4],"flag":ans[2]})





if __name__ == "__main__":
    app.run(debug=True)






