def most_trending_hashtag(posts):
    my_dict = {}
    counter = 1
    for i in range(len(posts)):
        key = posts[i]["trends"][0]
        if key in my_dict:
            continue
        else:
            for j in range(i+1,len(posts)):
                if key == posts[j]["trends"][0]:
                    counter+=1
        my_dict.update(key,counter)
        counter = 1
    return my_dict
print(most_trending_hashtag(input()))