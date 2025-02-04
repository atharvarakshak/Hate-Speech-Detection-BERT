# Hate Speech Detection
Comparing performance of different Large Language Models in analysing tweets containing Hate Speech. Comparing with traditional NLP based techniques to Identify Hate Speech.

### Models Used: 
- deepseek-r1:1.5b

### Dataset Used: 
- Hate Speech and Offensive Language Dataset

#  Installation: 
**Install and run Ollama Docker container:**  
Follow the steps provided by the official Ollama documentation https://hub.docker.com/r/ollama/ollama 
It is preferable to run Ollama with a GPU since we will send thousands of requests to the container. 

**Test Installation:**    
Visit http://localhost:11434 to test if ollama is running, you should see the message, `ollama is running`. 

**Run the Model:**   
Find the model you want to run and run it inside the container. To enter the interactive terminal of the container use: 
```bash
 docker exec -it /bin/bash
```
Here run the command: 
```bash
ollama run <Model-Name>
``` 
This will automatically pull and run the model.

Note: Please Ensure you are using an updated version of the Ollama container, or some models may not run. 

 **Changes:**  
 Change the model name in `test_model.py` to test the chosen model. You can run the model on the larger dataset provided at: https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset or on the short dataset included here.
