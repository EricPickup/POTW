#Without a doubt, everybody reading this problem has shared the pain of annoying, redundant Facebook notifications. So and so made a 
#post in uWindsor CompSci. So and so doesn't know which questions were given for an assignment. So and so is looking to hire a tutor
#for a class that has at least 6 or 7 TA's. Wouldn't it be nice if the CompSci group could filter notifications that simply aren't 
#relevant to you? 

#Let's pretend that Facebook is giving us a way to do this. Facebook will provide certain data for our filtering algorithm to take into 
#account. They have also agreed to allow us beta access for a new dislike button. Using these tools, we need an algorithm to notify a user
#only when a given number of your friends have liked the post. The algorithm will tell, for a given user and his/herlike threshold, which 
#posts are worthy of a notification by their standards. 


#Input: 

#The input starts with one line containing an unsigned integer n, where 1 <= n <= 1000. The next n lines gives all friendships in the 
#uWindsor Comp Sci group. Each of these lines contains two unsigned integers, a and b, denoting that user a and b are friends. Following 
#this is another unsigned integer m, where 1 <= m <= 1000. Following are m lines giving all likes / dislikes for every post in the group. 
#Each of these m lines contains three space separated integers, x, y and z. These indicate that user x liked (z = 1 ) or disliked (z = -1 ) post y. 
#Following this is one remaining line, containing two space separated unsigned integers u and t. This line is important. u is the user whom we are 
#determining which posts are notification worthy. A user should only receive notifications when, between all friends, at least t more of them have 
#liked the post than disliked. You should assume that no user may like and dislike the same post. 


#Output:

#The algorithm should determine all posts that have been liked by at least t of u's friends. Thus, the output contains p lines, where p is the 
#number of posts that meet this criteria for user u. Each line contains a post y that meets said criteria. Assume that there will always be at 
#least one post to be returned. 

#Example:
#Sample input 				Sample Output:
#5							10
#4 3
#1 2
#1 3
#1 4
#5 6
#6
#2 10 1
#3 10 1
#4 10 1
#2 11 -1
#3 12 -1
#4 11 1
#1 3

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