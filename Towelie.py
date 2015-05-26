#Towelie - A Stupid Towel Information Bot for Voat.co
#Made with VAPy Vapp - Voat App Framework

from random import choice

import Records
from Vapp import Vapp

class Towelie(Vapp):

    def __init__(self):
        super(Towelie, self).__init__()

        self.records = Records.Records("towelie")


    def run(self):
        
        #print(self.patterns)
        #print(self.responses)

        for subverse_name in self.subverses:

            subverse = self.vapy.get_subverse(subverse_name)
            submissions, comments = [i[0] for i in subverse], [j for i in subverse for j in i[1]]
            
            #print(len(submissions))
            #input(len(comments))

            for sub in submissions:
                self.view_cache.append(self.vapy.get_id(sub))
                for pattern in self.patterns:

                    if (self.vapy.contains_regex_in_title(pattern, sub) or
                            self.vapy.contains_regex_in_content(pattern, sub, ignore_links=True)):
                        response_type = choice(self.patterns[pattern])
                        sub_id = self.vapy.get_id(sub)
                        post_id = self.vapy.post_comment_to_submission(sub_id, choice(self.responses[response_type]))
                        self.records.log_post(post_id)

            for comment in comments:
                self.view_cache.append(self.vapy.get_id(sub))
                for pattern in self.patterns:
                    
                    if self.vapy.contains_regex_in_content(pattern, comment):
                        response_type = choice(self.patterns[pattern])
                        com_id = self.vapy.get_id(comment)
                        post_id = self.vapy.post_reply_to_comment(com_id, choice(self.responses[response_type]))
                        self.records.log_post(post_id)


def main():
    tbot = Towelie()
    tbot.run()

if __name__ == '__main__':
    main()
