import requests,re,bs4,sys
class searchphone:
    rooturl="https://www.jumia.co.ke/"
    url=""
    page=1
    allcategories=[
				    'sport-fitness',
				    'home-living',
                   'small-appliances',
    				'women-s-fashion',
                   'baby-kids-and-toys',
                   'men-s-fashion',
                   'mobile-phones',
                   	'food-stuffs',
    				'cooking-small-appliances',
    				'fashion-accessories',
    				'kitchen-dining',
    				'video-audio',
                   
                   ];
    categoryindex=0
    categories=allcategories[1]

    def makeurl(self,index,page):
        print(self.url)
        self.url=self.rooturl+self.allcategories[self.categoryindex]+"/?page="+str(page);

        self.process(url=self.url)

    def __init__(self):
        self.makeurl(index=self.categoryindex,page=self.page)

    def process(self,url):
        print(url)
        pagerequest=requests.get(url)
        requestdata=pagerequest.text
        soups=bs4.BeautifulSoup(requestdata,"lxml")
        links = soups.select(".products > .sku > .link")
        for link in links:
            if self.findphone(linkname=link.getText()):

                print("found in ",self.categories,self.page,self.url)
                sys.exit()

        self.page+=1;
        self.url="";

        if self.categoryindex==8:
            sys.exit()

        if self.page==20 :
            self.page=1;
            self.categoryindex+=1


        self.makeurl(index=self.categoryindex,page=self.page)

    def findphone(self,linkname):
        print(linkname)
        regex = re.compile(r' KSh 5 ')
        status = regex.search(linkname)
        print(status)
        if status:
            return True
        else:
            return False


s=searchphone()

