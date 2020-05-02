import requests, bs4, re


game = 'Baba Is You'
headers = {'User-Agent' : 'Chrome/70.0.3538.77'}


def getSteamReviews(gameName):
    
    
    steamStoreURLPrefix = 'https://store.steampowered.com/search/?term='
    rawGameName = gameName.split(' ')
    gameNamePLUS = '+'.join(rawGameName)


    res = requests.get(steamStoreURLPrefix + gameNamePLUS, headers=headers)

    res.raise_for_status()

    searchResultsPageSOUP = bs4.BeautifulSoup(res.text, features='lxml')

    search_results_table_tag_type = 'div'
    search_results_table_tag_id = 'search_resultsRows'

    search_results_table = searchResultsPageSOUP.find(search_results_table_tag_type, id=search_results_table_tag_id) #Finds the results table as a whole

    search_results_game_information = search_results_table.findAll('a', class_='search_result_row ds_collapse_flag') #I thought this would find only the names, but it's giving me all of the information for each game.

    searchIndex = 0
    

    working = True
    while working:
        try:

            search_results_game_information = search_results_game_information[searchIndex] # This is where we can choose how many of the results make the cut.

            game_URL = search_results_game_information['href'] # Extracts the link to the page where you buy the game - WANRLYO


            reviews = search_results_game_information.find('span', class_='search_review_summary')
            if reviews:

                reviewsText = reviews['data-tooltip-html'] #Extracts the tooltip that contains the review - WANRLYO
                reviewCleaningREGEX = re.compile(r'(.*)<br>(.*)')
                if '<' in reviewsText or '>' in reviewsText:
                    mo = reviewCleaningREGEX.search(reviewsText)
                    reviewsText = ' - '.join(mo.groups())
            else:
                reviewsText = 'No reviews for this one yet!'


            name = search_results_game_information.find('span', class_='title').get_text()



            price = search_results_game_information.find('div', class_='col search_price responsive_secondrow').get_text().strip()
            if not price:
                price = '(not given.)'

            # print(name)
            # print(game_URL)
            # print(reviewsText)
            # print(price)

            


            return (gameName, name, price, reviewsText, game_URL)

            print(f'''
                You searched for '{gameName}', and I found:
                {name}, which costs {price}.
                The reviews are: {reviewsText}
                And you can buy it from {game_URL}
            
            ''')
        except:
            print(f'Failed to get data for result number {searchIndex}')
            searchIndex+=1
            if searchIndex > 10:
                print('Aborting...')
                working = False







# hint = 'div id=search_resultsRows'
# needToGet = 'a href'

# I can just get the reviews straight off this first page!
