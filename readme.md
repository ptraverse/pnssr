python nighthack - sportstats scraper rewrite
pnssr

http://www.sportstats.ca/display-results.xhtml?raceid=25143

?css selector - almost right
<code>
	var nextPageButton = $('.pagination-wrapper ul li:not(.disabled):not(.active)').first();
	var athleteRow = $('tr.ui-widget-content');
	$(athleteRow).each(function(index, row) {
		var athleteName = $(row).find('a.athlete-trigger').text();
		var athleteTime = $(row).find('td').last().text();
</code>

	
virtualenv 
pip -> Splinter

---splinter fun!---
*https://splinter.readthedocs.org/en/latest/
*https://splinter.readthedocs.org/en/latest/javascript.html

<code>
	from splinter import Browser

	browser = Browser()    
	# Visit URL
	url = "http://www.google.com"
	browser.visit(url)
	browser.fill('q', 'splinter - python acceptance testing for web applications')
	# Find and click the 'search' button
	button = browser.find_by_name('btnG')
	# Interact with elements
	button.click()
	#Do Javascript
	browser.execute_script("$('body').empty();")
</code>