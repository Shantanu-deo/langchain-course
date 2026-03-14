from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()


def main():
    print("Hello from langchain-course!")
    information= """
            Bezos" redirects here. For other people with the surname, see Bezos (surname).
            Jeff Bezos

            Bezos in 2017
            Born	Jeffrey Preston Jorgensen
            January 12, 1964 (age 62)
            Albuquerque, New Mexico, U.S.
            Education	Princeton University (BSE)
            Occupations	
            Businessmanmedia proprietorinvestor
            Known for	Founding Amazon
            Title	
            Founder and executive chairman of Amazon
            Founder of Blue Origin
            Owner of The Washington Post
            Founder of Bezos Expeditions
            Executive chair of Bezos Earth Fund
            Founder of Bezos Academy
            Spouses	
            MacKenzie Scott
            ​
            ​(m. 1993; div. 2019)​
            Lauren Sánchez ​(m. 2025)​
            Children	4
            Parents	
            Jackie Bezos (mother)
            Ted Jorgensen (father)
            Miguel Bezos (stepfather)
            Relatives	Mark Bezos (half-brother)[1]
            Signature

            Jeffrey Preston Bezos (/ˈbeɪzoʊs/ BAY-zohss;[2] né Jorgensen; born January 12, 1964) is an American businessman best known as the founder, executive chairman, and former president and CEO of Amazon, the world's largest e-commerce and cloud computing company. According to Forbes, as of December 2025, Bezos's estimated net worth is US$239.4 billion, making him the fourth richest person in the world.[3] He was the wealthiest person from 2017 to 2021, according to Forbes and the Bloomberg Billionaires Index.[4]

            Bezos was born in Albuquerque, and raised in Houston and Miami. He graduated from Princeton University in 1986 with a degree in engineering. He worked on Wall Street in a variety of related fields from 1986 to early 1994. Bezos founded Amazon in mid-1994 on a road trip from New York City to Seattle. The company began as an online bookstore and has since expanded to a variety of other e-commerce products and services, including video and audio streaming, cloud computing, and artificial intelligence. It is the world's largest online sales company, the largest Internet company by revenue, and the largest provider of virtual assistants and cloud infrastructure services through its Amazon Web Services branch.
            """
    summaryTemplate = """
        Given the information {information} about the person, I want you to create :
        1. A short summary not more than 5 sentences.
        2. Two intersting facts about the person."""
    summaryPromptTemplate = PromptTemplate(
        input_variables=["information"],
        template=summaryTemplate
    )
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    chain= summaryPromptTemplate | llm
    response = chain.invoke({"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
