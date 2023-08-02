import re

FAVOURITES_PAGE = 'favourites.html'

def scrape_favourites():
    with open(FAVOURITES_PAGE, 'rt') as f:
        data = f.readlines()
    
    shows = []

    for line in data:
 
        if 'class="show-title' in line:
            main_link = re.search(r'href="([^"]*).*<span>(.*)</span>', line)
            shows.append({
                "link": main_link.group(1),
                "title": main_link.group(2),
                "dates": {},
            })

        venue = re.search(r'<span class="venue-name">(.*)</span>', line)
        if venue:
            shows[-1]["venue"] = venue.group(1)
        
        date = re.search(r'<span class="(.*)">([0-9]+)</span>', line)
        if date:
            shows[-1]["dates"][date.group(2)] = date.group(1)
    
    return shows

if __name__ == '__main__':
    shows = scrape_favourites()
    print(shows[0],"\n",shows[-1])
    