# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# time complexity: O(N log N)
# space complexity: O(N)
def solution(genres, plays):
    res = list()
    genre_total = dict()
    genre_songs = dict()
    n = len(genres)
    
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        
        genre_total[genre] = genre_total.get(genre, 0) + play
        if genre not in genre_songs:
            genre_songs[genre] = list()
        genre_songs[genre].append((play, i))
        
    sorted_genres = sorted(genre_total.items(), 
                          key = lambda x: x[1], 
                          reverse=True)
    
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], 
                      key=lambda x: (-x[0], x[1]))
        res.extend([song[1] for song in songs[:2]])
        
    return res
