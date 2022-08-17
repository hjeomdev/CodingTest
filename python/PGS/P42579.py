# def solution(genres, plays):
#     answer = []
#
#     # 장르별 재생 수 합산
#     genre_rank = {genre: 0 for genre in set(genres)}
#     play_rank = {genre: [] for genre in set(genres)}
#
#     for i in range(len(genres)):
#         genre_rank[genres[i]] += plays[i]
#
#     genre_rank = dict(sorted(genre_rank.items(), reverse=True)) # 불필요하게 총 재생수를 같이 저장하려고 딕셔너리로 만들려고 했음..
#     # print(genre_rank, play_rank)
#
#     # 재생 내림차순, 인덱스 오름차순 나열
#     for i in range(len(genres)): # 8번 줄에서도 동일한 포문을 돌리는데 굳이 한 번 더 돌림
#         play_rank[genres[i]].append([plays[i], i])
#     # print(genre_rank, play_rank)
#
#     for (genre, song) in play_rank.items():
#         # print(genre, song)
#         song.sort(key=lambda x:[-x[0], x[1]])
#         play_rank[genre] = song
# sort와 sorted의 차이는 sort는 리스트의 매소드로 해당 리스트 자체를 정렬(수정)하고, sorted는 내장함수로 정렬한 리스트를 새로 만들어 반환한다.
#
#     # print(play_rank)
#
#     for genre in genre_rank.keys():
#         answer.append(play_rank[genre][0][1])
#         answer.append(play_rank[genre][1][1]) # 곡이 한 곡인 경우를 생각 못함
#
#     return answer
# 전체적으로 불필요한 포문을 너무 많이 돌림



def solution(genres, plays):
    answer = []

    # 장르별 재생 수 합산해서 재생 내림차순으로 장르 나열
    # 재생 내림차순, 인덱스 오름차순 나열
    genre_rank = {genre: 0 for genre in set(genres)}
    play_rank = {genre: [] for genre in set(genres)}

    for i in range(len(genres)):
        genre_rank[genres[i]] += plays[i]
        play_rank[genres[i]].append([plays[i], i])

    best_genre = [x[0] for x in sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)]

    for genre in best_genre:
        play_rank[genre] = sorted(play_rank[genre], key=lambda x: [-x[0], x[1]])
        answer.append(play_rank[genre][0][1])
        if len(play_rank[genre]) > 1:
            answer.append(play_rank[genre][1][1])

    return answer


print("answer:", solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
