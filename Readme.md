This is a script that lets me make some questions to a LLM (Large Language Model) in the Mistral's API related to any project I am working with. I write the question in the variable named `pregunta` in the script. Then the code recopilates all the code files in the project that I tell it to collect and a description of the project placed in `requestHeader.txt` and then creates a string with all of this information.

After that, the mentioned string with the question and all the important related information is sent to the Mistral's API. The response of the LLM is written in `MistralResponse.txt`. 

These files must be placed within the project's directory.