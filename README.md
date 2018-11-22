# Latitude-Longitude-Scraper
Scrapes your set location's Latitude &amp; Longitude from Google Maps.

# Running Script
If data is in xlsx file set the file directory as well as the sheet name and column name where the locations are located.

If in a csv follow same step except for sheet name, just leave that empty.

You can also just read in a list for Locations_file.

Once these are set run the script and data will be saved to your directory and store in Complete_df. 

# Output
Coordinates will be saved into a new csv next to their respective location name.

# Exceptions
If you give a broad location such as "Taco Bell New York City" the first result will be returned and will likely not be the location you're looking for, so be as deliberate as possible.

If you are trying to get coordinates for a large amount of data Google will most likely stop at about 150-250 pulls. You will have to wait a few hours before scraping again. 

If require large amounts of coordinate data I recommend using Google's Places API (https://developers.google.com/places/web-service/search). Code that I used for that is posted. You will have to get API credintials and using the service will cost money, though it is pretty cheap and you can get $300 of credit for signing up. 
