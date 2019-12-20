import pandas

youtube = pandas.read_csv('/Users/emmanuelsalcedo/PythonPro/PythonClass/ExternalScripts/USvideos.csv')
print(youtube)
header = youtube.head()

print('\nvideo_id')
vidId = header['video_id']
print(vidId)

print('\nTrending Date')
trenddate = header['trending_date']
print(trenddate)

print("\nTitle")
title = header['title']
print(title)

print("\nChannel Title")
channeltitle = header['channel_title']
print(channeltitle)

print('\nCategory Id')
catid = header["category_id"]
print(catid)

print('\nPublish Time')
publishtime = header["publish_time"]
print(publishtime)

print("\ntags")
tags = header['tags']
print(tags)

print('\nviews')
views = header['views']
print(views)

print('\nlikes')
likes = header['likes']
print(likes)

print('\ndislikes')
dislikes = header['dislikes']
print(dislikes)

print('\ncomment_count')
comment_count = header['comment_count']
print(comment_count)

print('\nthumbnail_link')
thumbnail_link = header['thumbnail_link']
print(thumbnail_link)

print('\ncomments_disabled')
comments_disabled = header['comments_disabled']
print(comments_disabled)

print('\nratings_disabled')
ratings_disabled = header['ratings_disabled']
print(ratings_disabled)

print('\nvideo_error_or_removed')
video_error_or_removed = header['video_error_or_removed']
print(video_error_or_removed)

print('\ndescription')
description = header['description']
print(description)

print("\n Entries Table")
print(len(youtube))

print("\n\n\n\nChannel-title")
youtube['channel-title'] = youtube['channel_title'] + ' - ' + youtube['title']
print(youtube['channel-title'])
