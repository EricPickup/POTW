from collections import defaultdict

numPairs = int(input())
users = defaultdict(list)
posts = defaultdict(list)

for i in range (0, numPairs):
	a, b = map(int, input().split())
	users[a].append(b)	#Append friend to user
	users[b].append(a)	#Reverse the friend (if a is friends with b, b is friends with a)

numPosts = int(input())

for i in range (0, numPosts):			#For every post
	x, y, z = map(int, input().split())	#Split the values from the input line
	posts[y].append((x,z))				#Append the tuple (x,z) in y's list
							
user, threshold = map(int, input().split())	#Split the input line for user and threshold to be met

for i in posts:								#For every post
	count = 0;								#Variable for overall likes for the post
	for (friend, likeValue) in posts[i]:	#For every tuple in the current post
		if friend in users[user]:			#If the user who liked it is a friend of the user we're checking for
			count += likeValue				#Add the value of their like/dislike to the total
	if count >= threshold:					#If the count meets the threshold, print it
		print(i)