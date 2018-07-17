import requests,re,bs4,sys

class searchitem:
    url=""
    allcategorieslinks=[]
    categoryindex=1
    pageindex=1


    def process(self):

        pagerequest = requests.get(self.url)
        requestdata = pagerequest.text
        soups = bs4.BeautifulSoup(requestdata, "lxml")
        links = soups.select(".products > .sku > .link")
        for link in links:
            if self.finditem(linkname=link.getText()):
                print(self.url)
                print("found in ", self.allcategorieslinks[self.categoryindex], self.pageindex)
                sys.exit()
        print(" Not found in ", self.url)

        self.pageindex += 1


        self.makeurl(self.pageindex)

    def makeurl(self, page):
        self.url = self.allcategorieslinks[self.categoryindex] + "?page="+str(page)
        if self.pageindex>=25:
            self.categoryindex += 1
            self.pageindex=self.pageindex-25;

        self.process()




    def makecategories(self):
        rooturl = "https://www.jumia.co.ke/"
        categories = []
        categorieslinks = []

        data = requests.get(rooturl)
        soups = bs4.BeautifulSoup(data.text, "lxml")
        links = soups.select(".menu-items > .menu-item > .main-category")



        for link in links:
            self.allcategorieslinks.append(link.get('href'))

        self.makeurl(self.pageindex)
        self.process()


    def finditem(self, linkname):
        regex = re.compile(r'KSh 1 ')
        status = regex.search(linkname)
        if status:
            return True
        else:
            return False


    def __init__(self):
        self.makecategories()





s=searchitem()