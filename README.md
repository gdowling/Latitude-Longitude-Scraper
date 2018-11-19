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
If you give a broad location such as "Taco Bell New York City" the first result will be returned and will likely not be the location you're looking for, so be as exact as possible.
