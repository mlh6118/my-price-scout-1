Group: Marni Hager, Jae Loney, Sergii Otryshko, Pedro Perez
Summary of idea.
What problem or pain point does it solve? a. Keep it high level without going
into too much detail. (3-4 sentences is enough)
Minimum Viable Product (MVP) definition.
What is the minimum required for you to present on your demo day?

1. Cryptocurrency price tracker
   This is a web scraper that scrapes several crypto-currency sites, and
   constantly updates the pricing
   This app aggregates and automatically tracks the prices of various crypto
   currencies in one place.
   Save data
   Auto-rerun script to update data
   Send text message to user (stretch goal)
   Scraping the websites for the top 20 currencies. Then the person can pick the
   ones they want to track, add it to their list. Then once the crypto is in the
   script we will update the values/prices and link it to a library where it
   will send a text when it goes down to a certain price point(Stretch Goal).
   The script will run every (certain amount of time)
   The text message would be a good idea. Add - track the crypto’s the user
   owns? Shall we set threshold prices based on previous buys/sells with a
   percentage up or down from there? Trends in buying trends etc by others?
   Would be better to use an API than scraping for this. More built out than
   just a tracker.
2. Code Fellows ask a question, check if already answered.
   Create new Slack community
   Create API or database to store Slack data
   Search the API or database for previous questions.
   Pulls up related slack threads. Slack premium would be needed if we wanted to
   work with Code Fellows data. Since we can create our own slack community, we
   can do local testing and then push the ideas over. Since they do not store
   the messages we could send the messages to a database/API instead of storing
   the information on Slack
   Would definitely need to store/retrieve the data including the fact that past
   messages are not stored with the Slack API. How robust could we make a
   searchable database with questions from Slack. Say a question had a Python
   Lab 11 problem. How do we break up the search queries, by “enumerate” lab or
   the lab number. Is this a library import library question? Are the questions
   tagged? Can we see if a question from the ticket queue was asked previously
   in a slack questions. If they ask a question in this channel and it is marked
   resolved by a user, we can store this question/answer into a database that we
   can show the next person asking a question. Should use our own database if we
   select this route.


3. Used car tracker/purchase recommendation
   Extract information through APIs
   Return the pricing in a table
   Add alerts
   Pain points- (1) not able to connect with a potential buyer real time (2)
   lack of real time purchase/information for timely decisions.
   Input brand/year/car model that brings back pricing in a table with add
   alerts functionality for certain price levels. The outputs - (1) sorted list
   of cars’ price/availability with contact (2) recommendation as to what price
   and when to buy. (Base this on the Kelly Blue Book.)
   There are libraries that show graphs in the console

---------------------------------------------------------------------------------------------------------------------------

4. Your(em) Ipsum
   This is a Lorem Ipsum Generator for a topic of the user’s choosing.
   This would solve the pain point of making creative customizable Lorem Ipsum
   searches. Currently there are APIs that allow for about 20 different
   subjects, but with this Lorem Ipsum generator, only one API is needed that
   allows for even more customization or creativity. This would implement web
   scraping of a resource (potentially articles) for commonly associated words
   and return paragraphs as an API.
   MVP - A 5 paragraph response of lorem ipsum mixed with words related to the
   Input word
   Not enough expandability in MVP case

5. Regex Eliminator:
   This is a site where you can input the wanted Regex in sentences that returns
   the regex for the query
   This would solve the pain point of creating regex queries. Regex structures
   would be input based on sentences or selectable queries and then put together
   for the user.
   MVP - This site would return three examples for python such as phone numbers,
   emails, and Title Case first and last names to begin with with common
   variations on these input types.
   On the fence for the concept

