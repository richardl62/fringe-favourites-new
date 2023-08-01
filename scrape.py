import re

with open('html-only.html', 'rt') as f:
    data = f.readlines()
for line in data:
    if 'class="show-title' in line:
        main_link = re.search(r'href="([^"]*).*<span>(.*)</span>', line)
        print(main_link.group(1), main_link.group(2))
    
    dates = re.search(r'<span class="(.*)">([0-9]+)</span>', line)
    if dates:
        print(dates.group(2), dates.group(1))

    venue = re.search(r'<span class="venue-name">(.*)</span>', line)
    if venue:
        print(venue.group(1))


    