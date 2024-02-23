from seleniumbase import SB
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Your Gmail login credentials
mail_address = "USERNAME"
password = "PASSWORD"  # Replace with your actual password

# List of queries directly in the script
questions = [
    "What are the best solo travel destinations?",
    "How do I respond to unsolicited advice about having kids in the future?",
    "What are the three types of coverage in rental insurance policy?",
    "How do I prepare for the SAT or ACT at high school?",
    "How to act on a first date?",
    "How do I handle questions from family and friends about not having kids?",
    "How does renting a house affect my credit score?",
    "Tips for a good college essay?",
    "What are the top movies for a solo movie night?",
    "How do I manage estate planning or will-writing without direct descendants?",
    "How to find affordable apartments near me?",
    "Which calculator is approved for use in high school math exams?",
    "Recommend some books about embracing singlehood.",
    "Can you recommend books or blogs about choosing a child-free lifestyle?",
    "Can you find cheap rental insurance for me?",
    "Additional math high school classes near me",
    "Find me events for singles happening this weekend.",
    "How can I handle family pressure about not having kids yet?",
    "Where is the best place to look for rental homes?",
    "Which colleges are known for their programs in environmental science?",
    "How can I meet other singles in my city?",
    "How do I set up social media filters to see less baby-related content?",
    "What are the risks of subleasing a house?",
    "How do I prepare for my high school oral presentations?",
    "Can you recommend dating apps or websites that are popular among singles?",
    "What are some quotes about having a good life without kids?",
    "How do I convince an owner to rent his house to me?",
    "What topics are usually covered in high school geometry?",
    "Are there any solo dining experiences or restaurants nearby?",
    "How to cure infertility?",
    "What changes can I make to a rental apartment?",
    "What are extracurricular activities that colleges look for?",
    "What's a good solo workout routine I can try at home?",
    "Can you suggest movies or TV shows that focus on life without children?",
    "How to decorate a rental without damaging walls?",
    "How can I get a scholarship for my college?",
    "What are some fun weekend ideas for someone who is single?",
    "How do I prepare for elderly care without children to rely on?",
    "What are the important things during a rental property inspection for a renter?",
    "Which courses should I take for college prep?",
    "What are the good ways to budget for a single person?",
    "Can you suggest fun activities that don't involve kids?",
    "How do I understand my rental agreement?",
    "How do I ask my high school teacher for a letter of recommendation?",
    "What are some safety tips for a person traveling solo?",
    "What are the best vacation destinations tailored for adults without kids?",
    "Can you find apartments for rent near me?",
    "How to join student council at high school?",
    "Is dating online a good option?",
    "Are there any popular restaurants that cater mainly to adults?",
    "Should I rent houses that include utilities?",
    "Can you recommend books for high school summer reading lists?",
    "What should single people do to avoid depression?",
    "How can I plan for my retirement without having kids?",
    "What's the process of breaking a lease early?",
    "When are college applications due?",
    "How to know the personality of the person on the first date?",
    "What financial planning advice do you give to people without children?",
    "How to find good rental insurance?",
    "Any college counseling sessions soon?",
    "What are the best self-care routines for someone living alone?",
    "What social groups are available for people without children?",
    "How to get a discount for renting a house from the owner?",
    "How can I use my school library?",
    "Who inherits my stuff if I am single?",
    "What hobbies are best for people without children?",
    "Can I have pets in a rented apartment?",
    "Which clubs help with college applications?",
    "Are there any dating tips for someone getting back into the scene after a long time?",
    "Show me the advantages of not having kids in terms of lifestyle.",
    "What to look for during a rental inspection?",
    "When are the college application deadlines for this year?",
    "What's a good hobby to take up when you live alone?",
    "Can you recommend books that discuss life without children?",
    "How to handle repairs in a rental property as a renter?",
    "Find me tips for writing my high school graduation speech."
]

with SB(uc=True) as sb:
    sb.open("https://www.google.com/gmail/about/")
    sb.click('a[data-action="sign in"]')

    # Wait for email input to be present
    sb.wait_for_element_present('input[type="email"]', timeout=10)
    sb.type('input[type="email"]', mail_address)
    sb.click('button:contains("Next")')

    # Wait for password input to be present
    sb.wait_for_element_present('input[type="password"]', timeout=10)
    sb.sleep(5)
    sb.type('input[type="password"]', password)
    sb.click('button:contains("Next")')

    # Redirect to Google after logging in to Gmail
    sb.open("https://www.google.com/")
    
    # Wait for search input to be present before the loop
    try:
        search_input = WebDriverWait(sb.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
    except TimeoutException:
        print("Search input element not found within the specified time.")

    # Automatically search queries based on the list
    for query in questions:
        try:
            # Wait for search input inside the loop
            search_input = WebDriverWait(sb.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_input.clear()
            search_input.send_keys(query)
            search_input.submit()
            sb.sleep(1)
        except TimeoutException:
            print(f"Element 'input[name=\"q\"]' not found. Retrying...")
