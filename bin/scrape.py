from splinter import Browser

browser = Browser('chrome')

# Visit URL
# url = "http://www.sportstats.ca/display-results.xhtml?raceid=25143"
# browser.visit(url)

# Do Javascript
# browser.execute_script("$('body').empty();")
browser.quit()
