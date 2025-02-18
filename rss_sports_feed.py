import json
import xml.etree.ElementTree as ET

import requests

# URL for RSS Feed
rss_url = 'https://www.ttusports.com/general/headlines-featured?feed=rssgraffiti'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "*/*",
}

response  = requests.get(rss_url, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch RSS feed: {response.status_code}")
    exit()
    
# Parse the XML response
root = ET.fromstring(response.content)

# Create list for storing news items
rss_items = []

# Iterate over each item element
for item in root.findall('.//item'):
    title = item.find('title').text if item.find('title') is not None else ''
    link = item.find('link').text if item.find('link') is not None else ''
    description = item.find('description').text if item.find('description') is not None else ''
    pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
    enclosure = item.find('enclosure')
    if enclosure is not None:
        image_url = enclosure.get('url')
    else:
        image_url = 'https://banner2.cleanpng.com/20180525/zvq/kisspng-tennessee-technological-university-tennessee-tech-5b07b00030aea2.6243947915272304641994.jpg'
    
    # Append to the list
    rss_items.append({
        'title': title, 
        'link': link,
        'description': description,
        'pubDate': pubDate,
        'image_url': image_url
    })
        
        
# Save the list to a JSON file
with open('rss_feed.json', 'w') as f:
    json.dump(rss_items, f, indent=4)
    
print("RSS feed saved to rss_feed.json")