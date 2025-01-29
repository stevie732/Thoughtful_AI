## Step 1: Define the Predefined Dataset
- We'll start by defining the dataset of questions and answers about Thoughtful AI.

***

## Step 2: Create the Agent Logic
- The agent will compare the user's input with the predefined questions and return the corresponding answer. If no match is found, it will provide a generic response.

***

## Step 3: Build the Chat Interface
- We'll use Gradio to create a simple chat interface for the agent.

***

## Step 4: Run the Application
- Save the code in a Python file and run it. The Gradio interface will launch, allowing users to interact with the agent.

- I've created a virtual environment to install the dependencies to.
in your `cli` type:
`python3 -m venv .venv`

- then activate your virtual environment by typing:
`source .venv/bin/activate`

## Install dependencies:
- `pip install -r requirements.txt`

#### Your app is ready to run!!!! :)

***

## Example Interaction

#### 1. User Input: "What does EVA do?"
  - Agent Response: "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejects."

#### 2. User Input: "What is Thoughtful AI?"
  - Agent Response: "Thoughtful AI is a company that develops intelligent agents to automate and streamline healthcare administrative processes, such as eligibility verification and claims processing."

#### 3. User Input: "How do i contact support?"
  - Agent Response: "I'm sorry, I don't have information on that. Please contact Thoughtful AI support for further assistance."

***

* The agent uses exact string matching for simplicity. For more advanced matching, you could use fuzzy matching or embeddings.

* The fallback response ensures the agent remains helpful even for out-of-scope questions.

* Gradio provides a lightweight and user-friendly interface for quick prototyping.