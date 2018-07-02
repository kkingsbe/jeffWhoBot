import praw

def getSubComments(comment, allComments, verbose=True):
  allComments.append(comment)
  if not hasattr(comment, "replies"):
    replies = comment.comments()
    if verbose: print("fetching (" + str(len(allComments)) + " comments fetched total)")
  else:
    replies = comment.replies
  for child in replies:
    getSubComments(child, allComments, verbose=verbose)

def getAll(r, submissionId, verbose=True):
  submission = r.submission(submissionId)
  comments = submission.comments
  commentsList = []
  for comment in comments:
    getSubComments(comment, commentsList, verbose=verbose)
  return commentsList

reddit = praw.Reddit(client_id='IxXnB1afRLRN5g',
                     client_secret='xnezoWxiLWhnR9Vk9Lw6UEnrqUo',
                     password='BCCBarons2016!',
                     user_agent='jeffWho',
                     username='jeffWhoDid9-11')

print(reddit.user.me())
all = reddit.subreddit('all')
for submission in all.hot():
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.url)    # Output: the URL the submission points to
    comments = getAll(reddit, submission.id)
    for comment in comments:
        try:
            print(comment.body)
            if "jeff bezos" in comment.body.lower():
                comment.reply("[Jeff Who?](https://imgur.com/r/funny/BfZ6roy)")
                print("REPLY SENT")
        except  Exception as e:
            pass