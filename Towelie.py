#Towelie - A Stupid Towel Information Bot for Voat.co
#Made with VAPy Vapp - Voat App Framework

import Vapp, Records

class Towelie(Vapp):

    def __init__(self):
        super(Towelie, self).__init__(profile="towelie")

        self.records = Records.Records()

    def run(self):

        for subverse in self.subverses:

            subvrs = self.vapy.get_subverse(subverse)
            submissions, comments = [i[0] for i in subvrs], [i[1] for i in subvrs]

            for sub in submissions:

                for pattern in self.patterns:

                    if (self.vapy.contains_regex_in_title(pattern, sub) or
                            self.vapy.contains_regex_in_content(pattern, sub, ignore_links=True)):
                        response_type = choice(self.patterns[pattern])
                        sub_id = self.vapy.get_id(sub)
                        post_id = self.vapy.post_comment_to_submission(sub_id, choice(self.responses[response_type]))
                        self.records.log_post(post_id)

            for comment in comments:

                for patten in self.patterns:

                    if self.vapy.contains_regex_in_content(pattern, comment):
                        response_type = choice(self.patterns[pattern])
                        com_id = self.vapy.get_id(comment)
                        post_id = self.vapy.post_reply_to_comment(com_id, choice(self.response[response_type]))
                        self.records.log_post(post_id)

