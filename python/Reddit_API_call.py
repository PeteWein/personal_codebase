import sys, datetime, json, requests, time

def main():
    """
    The goal is to do a basic API call to our user and see their info.
    It can definitely be improved (i.e. sort by top to determine top comment)
    this call is limited to what is stored on the reddit API (I believe there's a time frame limit or last 1000 limit)
    """
    user = input('What username would you like to look up? ')
    userlist = UserInfo(user)
    try:
        user_results = userlist.redditapi_commentinfo()            # store results of api call in
        # print the results for viewing
        print('User ', end=''), print(user, end=''), \
            print(' has made ', end=''), print(int(user_results[0]), end=''), \
            print(' comments in total.')
        print('User ', end=''), print(user, end=''), \
            print(' has a total score of ', end=''), \
            print(int(user_results[1]), end=''), print('.')
        print('The best comment had ', end=''), print(user_results[2], end=''), \
            print(' upvotes and the comment is below:')
        print('"', end=''), print(user_results[3], end=''), print('"')
        print('Link to comment is below:'),
        print(user_results[4])
    except KeyError as e:
        print('Received API KeyError: '), \
            print(e)
    print('All Reddit API calls complete.')


class UserInfo(object):
    def __init__(self, user):
        self.user = user
        self.user_agent = '/u/' + self.user
        self.userurl = r'https://www.reddit.com/user/'
        self.requesturl = self.userurl + self.user + '/comments/.json?sort=new&limit=100'
        # store original link to modify for loop
        self.requesturlorig = self.requesturl
        self.req = requests.get(self.requesturl, headers={'User-agent': '/u/DasWeinmachine'})

    def redditapi_commentinfo(self):
        print('Gathering Reddit comment info for /u/' + self.user)
        count = 0                       # for looping the url
        comment_count = 0               # how many comments have been made
        total_score = 0                 # total score
        max_score = 0                   # highest scored comment
        max_score_comment = ''          # highest scored text
        max_score_link = ''             # ensure referenced
        apiloop = True
        try:
            while apiloop:
                time.sleep(2)               # you can only make 1 request every 2 seconds (30/min)
                data = self.req.json()
                # print(json.dumps(data, indent=4, sort_keys=True))             # pretty view
                for child in data['data']['children']:                          # score per comment
                    comment_count += 1                                          # increment all appropriate values
                    total_score += child['data']['score']
                    if child['data']['score'] > max_score:
                        max_score = child['data']['score']                      # replace max score if current better
                        max_score_comment = child['data']['body']               # remove body of comment appropriately
                        max_link = child['data']['permalink']                   # link to comment
                        max_score_link = 'https://www.reddit.com' + max_link
                if data['data']['after'] is not None:
                    after = data['data']['after']
                    self.requesturl = self.requesturlorig + '&count=' + str(count) + '&after=' + after
                    self.req = requests.get(self.requesturl, headers={'User-agent': '/u/DasWeinmachine'})
                count = data['data']['dist']
                apiloop = count == 100              # break loop if comments pulled less than max
        except:
            print('Error requesting info for user /u/'+ self.user, end='\n'), \
            print('Error ' + str(data['error']) + ': ' + data['message'], end='')
            sys.exit()
        return comment_count, total_score, max_score, max_score_comment, max_score_link


if __name__ == '__main__':
    main()
