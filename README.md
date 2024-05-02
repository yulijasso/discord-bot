In my Discord bot script, I've focused on the primary functionality of detecting messages from users and responding accordingly. Leveraging the spaCy library, I incorporated natural language processing capabilities to enhance the bot's understanding of user input. (To install spaCy on my system, I ran “pip install spacy” and “python -m spacy download en_core_web_sm”). By analyzing the content of messages, the bot can identify keywords or intents, allowing it to provide relevant and contextually appropriate responses. This approach not only improves the bot's ability to engage with users but also enhances the overall user experience by delivering more personalized interactions. Through continuous refinement and optimization of the bot's response mechanisms, I aim to further enhance its effectiveness in meeting user needs and expectations. 

For the web server script, the code includes the discord token generated in the discord portal for the creation of the new bot to control the bot as well as the host and port number. I utilized host 0.0.0.0 and port 8080. The IP address 0.0.0.0 indicates that the server should listen on all available network interfaces on the host machine. This means that the server will accept connections from any IP address that can reach the host. Using 0.0.0.0 allows your server to be accessible from both the local network and the internet. Ports are used to differentiate between different services running on the same host. Port 8080 is commonly used for hosting web servers. It's an alternative to the standard HTTP port (80) and is often chosen for development and testing purposes. Additionally, using a non-standard port like 8080 can help avoid conflicts with other services running on the same machine. 
