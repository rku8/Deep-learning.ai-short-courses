### Overview
Supervised learning is a core building block for training a large language model.

How it works:
A language model is built by using supervised learning (x→y) to repeatedly predict the next word.

E.g.:   *My favorite food is a bagel with cream cheese and lox.*

| **Input x** | **Output y** |
| --- | --- |
| My favorite food is a | bagel |
| My favorite food is a bagel | with |
| My favorite food is a bagel with | cream |
| ………… | ….. |

Given a large training set (billions of words) and make the dataset `input x` , `output y` . Repeatedly ask the model to learn the prediction of what’s next word.

Getting from base LLM to instruction tuned LLM:-     

- Train a base LLM on lot of data. (take months)
- Further train the model:
    - Fine tune on examples of where the output follows input instructions. (tries to predict next words)
        
        To improve the quality of LLM’s output-
        
    - Obtain human-ratings of the quality of different LLM outputs, on criteria such as whether it is useful, honest and harmless.
        
        Further
        
    - Tune LLM to increase probability that it generates the more highly rated outputs (using RLHF: Reinforcement Learning with human Feedback)

---

Note: It is not repeatedly predict next word, it predicts next token.

The words that often most used with human.

E.g. 

![image.png](imgs\image.png)

Some of the words that are not much used like ‘Prompting’

E.g. 

![image.png](imgs\image_1.png)

Here, the single word ‘Prompting’ contains 3 tokens.

Suppose I have the word `lollipop` and I want to reverse this, then the LLM might look this word as

![image.png](imgs\image_2.png)

> ChatGPT is not see individual letters, it sees three tokens. So it is hard to respond this word into correct reverse order.
> 

To overcome such problems, we can use `l-o-l-l-i-p-o-p` then it reverse this and prints.

![each letter is token](imgs\image_3.png)

each letter is token

> For english language: 1 token is around 4 characters.
> 

---

Token limits:

- Different models have different limits on the number of tokens in the input (’context’) + output (’completion’).
- gpt-3.5-turbo ~4000 tokens

---

Supervised learning:  ——

Prompt based AI:—————