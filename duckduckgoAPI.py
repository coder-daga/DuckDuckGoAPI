import urllib
import unirest
import time
# These code snippets use an open-source library. http://unirest.io/python

print "\n\n**Welcome to Mayank's implementation of DuckDuckGos' Mashape API**\n\n"

format="json"

q=raw_input("Please enter the Query paramter: ")
skip_disambig="1"
print "Retrieving the results..."
time.sleep(1)

my_url="https://duckduckgo-duckduckgo-zero-click-info.p.mashape.com/?format="+format+"&q="+q+"&skip_disambig="+skip_disambig

response = unirest.get(my_url,
  headers={
    "X-Mashape-Key": "XXXX",
    "Accept": "application/json"
  }
)

def AbstractInfo():
	print ("\n\nPrinting the Abstract URL and the Abstract:\n\n")
	time.sleep(1)
	print "Abstract URL: " +response.body['AbstractURL']+ "\nAbstract: "+response.body['Abstract']

def Image():
	ch=raw_input("\n\nDo you want to save an image of "+q+"? Enter 1 if Yes else enter 0: ")
	time.sleep(3)

	if len(response.body['Image'])<=0 and ch=='1':
		print "Sorry, No URL found."
	elif ch=='0':
		print ("\n\nK fine thanx.") 
	elif len(response.body['Image'])>0 and ch=='1': 
		print ("\n\nPrinting the Image URL:")
		time.sleep(2)
		print response.body['Image']
		print "\n\nSaving image to local drive...\n"
		time.sleep(2)
		urllib.urlretrieve(response.body['Image'], "C:\Users\Mayank\Desktop\\"+q+".png")
		print "Image saved."
	else:
		print("Wrong choice.")

	
def RelatedTopics():
	print ("\n\nPrinting the Related topics: \n")
	for d in response.body['RelatedTopics']:
		print d['Text']


choice=raw_input("\n\nPlease select one of the following: \n1)Display Abstract Info\n2)Display Image URL and save Image\n3)Display Related Topics\n4)Exit: ")

while choice!=4:
	if choice=='1':
		AbstractInfo()
	elif choice=='2':
		Image()
	elif choice=='3':
		RelatedTopics()
	elif choice=='4':
		break;
	choice=raw_input("\n\nPlease select one of the following: \n1)Display Abstract Info\n2)Display Image URL and save Image\n3)Display Related Topics\n4)Exit: ")

print "\nGoodbye! It was nice providing service to you."	

