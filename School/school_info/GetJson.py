#encoding: utf-8
import json
import csv

class ThesisInfo(object):
    def __init__(self):
        self.avatar = "None"
        self.firstName = "None"
        self.lastName = "None"
        self.organization = "None"
        self.major = "None"
        self.title = "None"
        self.birth = "None"
        self.country = "None"
        self.state = "None"
        self.maincity = "None"
        self.phone = "None"
        self.email = "None"
        self.website = "None"
        self.cooperation = []
        self.bio = "None"
        self.keywords = []
        self.city = ["China"]
        self.time = ["Flexible"]
        self.keywordKeys = []
        self.cityKeys = [1]
        self.timeKeys = [1]
            
    def set_value(self):       
        self.parm = {
                "name": self.firstName,
                "email":self.email,
                "password":"bcrypt",
                "avatar":self.avatar,
                "profile":
                    {
                    "keywordKeys":self.keywordKeys,
                    "cityKeys":self.cityKeys,
                    "timeKeys":self.timeKeys,
                    "firstName":self.firstName,
                    "lastName":self.lastName,
                    "organization":self.organization,
                    "major":self.major,
                    "title":self.title,
                    "birth":self.birth,
                    "country":self.country,
                    "state":self.state,
                    "city":self.city,
                    "phone":self.phone,
                    "email":self.email,
                    "website":self.website,
                    "cooperation":self.cooperation,
                    "bio":self.bio
                    }
                }

        
if __name__ == '__main__':
    parm = {"keywordKeys":[1,2,3],
            "cityKeys":[1],
            "timeKeys":[1],
            "firstName":"Chun-Hung",
            "lastName":"Chen",
            "organization":"George Mason University",
            "major":"System Engineering",
            "title":"Professor",
            "birth":"2017-05-30",
            "country":"USA",
            "state":"VA",
            "city":"Fairfax",
            "phone":"+1 (703) 993-3572",
            "email":"cchen9@gmu.edu",
            "website":"http://mason.gmu.edu/~cchen9/",
            "cooperation":["Short time teaching","Customizing core curriculum","Research or development"],
            "bio":"Understanding what could go wrong before it happens is vital to almost every industry. Stochastic modeling works to help engineers simulate incidents that arise from seemingly random circumstances. This is especially important to air transportation systems, technology manufacturing, healthcare, security networks, power grids, and military operations. Chun-\n\nHung Chen is the inventor of a novel idea called Optimal Computing Budget Allocation, which drastically improves the efficiency of stochastic simulation. Because this methodology has proven to be of great importance to so many applications, Chen鈥檚 research has been funded by a variety of organizations such as the National Science Foundation, the National Institutes of Health, the Department of Energy, NASA, the US Air Force, the US Missile Defense Agency, and the Federal Aviation Administration. Chen teaches several sections of systems simulation modeling and research techniques on the graduate and undergraduate level.\n",
            "keyword-1":"highly efficient methodology ",
            "keyword-2":"semiconductor manufacturing",
            "keyword-3":"power grids",
            "city-1":"China",
            "time-1":"Flexible"}

    with open('namelist.csv', 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    with open('info.json', 'w') as json_file:
        for record in content:
            teacher = json.loads(record)
            info = ThesisInfo()
            info.set_value()
            info.avatar = teacher['img']
            info.firstName = teacher['name']
            info.lastName = teacher['name']
            info.organization = "None"
            info.major = "None"
            info.title = teacher['title']
            info.birth = "None"
            info.country = "US"
            info.state = "None"
            info.maincity = "None"
            info.phone = teacher['phone']
            info.email = teacher['email']
            info.website = "None"
            info.cooperation = []
            info.bio = teacher['background']
            info.keywords = []
            info.city = ["Wisconsin"]
            info.time = ["Flexible"]
            info.keywordKeys = []
            info.cityKeys = [1]
            info.timeKeys = [1]
            info.set_value()
            json.dump(info.parm, json_file)
            json_file.write("\n")