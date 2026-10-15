#first create a virtual environtment and then activate it -- this creates a seprate workspace for this project folder
# create .env file -- used to store the api keys 
#create .gitignore file -- secure the .env file and wont make it visible in the github
# install required packages -- python-dotenv ,  gemini(google-genai)  -- pip install
# check installed packages -- pip list
# create python file for building applications 


#import required packages 
from dotenv import load_dotenv
import os
from groq import Groq
import json


#load the environment variable in the python file 
load_dotenv()

#get the environment variable and store it in the python variable

api_key =os.getenv("groq_api_key") 

#check the api key is loaded succesfully or not

if not api_key:
    print(" Api key not found.")


# create the client 
client = Groq(api_key=api_key)

#define the model in a variable -- choose a model that is available in the groq account
#If model is unavailable , check the models page in groq console 
MODEL = "openai/gpt-oss-20b"

# ====================================================================
# Step[2] : CREATE A REUSABLE AI FUNCTION
# ====================================================================

def ask_ai(prompt):
    #send the prompt to the groq chat completion api.
    response = client.chat.completions.create(
        model= MODEL,

        #provide the prompt as a user messsage.
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        #control how creative the api response can be.
        temperature=0.7,

        #limit the MAximum response length.
        max_tokens= 1000
    )

    #Extract and return the AI_genrated text.
    return response.choices[0].message.content


# ====================================================================
# Step[3] : GENERATE IDEAS
# ====================================================================

def generate_ideas(topic):
    prompt = f"""
    You are a content planning assistant 

    Generate 5 useful beginner-friendly ideas about:
    {topic}

    Explain each idea in one sentence.
    Use a numbered list.
    """

    #send the new prompt to groq and get the ai response

    ideas = ask_ai(prompt)

    #return the ideas to next stage
    return ideas

# ====================================================================
# Step[4] : CREATE AN ARTICLE
# ====================================================================

def create_article(topic , ideas):

    #Insert the ideas from step3 into the next prompt.

    prompt = f""" 
    You are a professional content writer.

    Topic : {topic}

    Use these ideas to write an informative articles:

    {ideas}

    Requirements:
    - Write a suitable title.
    - Use simple english
    - Include an introduction.
    - Explain the ideas using headings.
    - Include a conclusion.
    - keep the article beginner-friendly.
    """

    #send the new prompt to groq
    article = ask_ai(prompt)

    #return the article to the next stage
    return article

# ====================================================================
# Step[5] : SUMMARIZE THE ARTICLE
# ====================================================================

def create_summary(article):
    #pass the complete article to the ai for summarization.
    prompt = f""" 
    You are an expert summarizer.

    summarize the following article into 5 important
    bullet points

    Use simple english
    Preserve the article's main meaning.

    ARTICLE:{article}
    """
    #ask groq to summarize the article
    summary = ask_ai(prompt)

    #return the summary to next stage
    return summary


# ====================================================================
# Step[6] : CREATE A LINKDIN POST
# ====================================================================


def create_linkedin_post(topic, summary):

    #use the summary to create a LINKEDIN POST
    prompt = f""" 
    You are a professional social media content writer.

    Create a LinkedaIn post about : {topic}

    Use this summary as the source material:
    {summary}

    Requirements:
    - Start with anengaging opening.
    - Use simple, Professional English.
    - Keep the post concise.
    - Add a call to action.
    - Add a relevant hashtags.
    - Do not invent facts or statistics.
    """

    #send the prompt to groq
    post = ask_ai(prompt)

    #return the final LinkedIn post.
    return post

# ====================================================================
# Step[7] : RUN THE PROMPT CHAIN
# ====================================================================

def main():

    #Ask the user to enter a topic.
    topic = input("Enter a Topic: ").strip()

    #stop if user does not enter a topic.
    if not topic:
        print("Please enter a valid topic.")
        return

    try:

        #CHAIN 1
        #Generate ideas from the user's topic.
        print("\n STEP 1 : Generating Ideas...")
        ideas = generate_ideas(topic)

        # display the genrated ideas
        print("\n============IDEAS==========")
        print(ideas)

        #CHAIN 2
        #pass the ideas into the articles-generation function.
        print("\nSTEP 2 : Creating article...")
        article = create_article(topic, ideas)

        # display the genrated Article.
        print("\n============ARTICLE==========")
        print(article)

        #CHAIN 3
        #pass the article into the summary function.
        print("\nSTEP 2 : Creating summary...")
        summary = create_summary(article)
        
        # display the genrated Summary.
        print("\n============SUMMARY==========")
        print(summary)


        #CHAIN 4
        #pass the summary into the LinkedIn post function.
        print("\nSTEP 2 : Creating aLinkedIN post...")
        LinkedIn_post = create_linkedin_post(topic , summary)
        
        # display the genrated LinkedIN post.
        print("\n============LINKEDIN POST ==========")
        print(LinkedIn_post)

        #confirm that all stages completeed successfully.
        print("\nPrompt Chaining completed successfully.")

    except Exception as error:

        #display an error if an API request or another step fails.
        print("\n Something went wrong.")
        print("Error:", error)

#Run main()only when the file is executed directly.
if __name__ == "__main__":
    main()


# ====================================================================
# END OF THE PROJECT
# ====================================================================