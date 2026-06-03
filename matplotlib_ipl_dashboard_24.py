                                                        #
# import matplotlib.pyplot as plt

# players = ['Virat','Rohit','SKY','Gill','Pant','Hardik','Dhoni','Rahul']
# balls_faced = [48, 35, 22, 41, 30, 18, 15, 55]
# runs_scored = [72, 55, 48, 63, 44, 38, 27, 82]

# plt.plot(balls_faced, runs_scored, color='red', marker='x')
# plt.scatter(balls_faced, runs_scored, color='blue', marker='o')
# plt.xlabel('Balls Faced')
# plt.ylabel('Runs Scored')
# plt.title('Strike Rate Scatter – IPL 2024 Batters')
# plt.show()
                                                        #Scatter
# matches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # cumulative_runs = [45, 98, 167, 210, 278, 345, 401, 456, 523, 589]

# # plt.plot(matches, cumulative_runs)
# # plt.xlabel('Match Number')
# # plt.ylabel('Cumulative Runs')
# # plt.title('RCB - Cumulative Runs (IPL 2024)')
# # plt.show()

                                                    #Top runs scorers chart

# import matplotlib.pyplot as plt

# batters = ['Virat', 'Gill', 'Rohit', 'Rahul', 'SKY', 'Pant']
# total_runs = [741, 702, 588, 520, 495, 446]

# plt.bar(batters, total_runs)
# plt.xlabel('Batters')
# plt.ylabel('Total Runs')
# plt.title('IPL 2024 – Top 6 Run Scorers')
# plt.show()
       
                                                #Score distribution

# import matplotlib.pyplot as plt

# match_scores = [
#     142, 178, 165, 198, 134, 210, 156, 189, 172, 145,
#     203, 168, 155, 181, 194, 148, 162, 177, 191, 140,
#     185, 159, 173, 206, 152, 167, 188, 196, 143, 170
# ]

# plt.hist(match_scores, bins=8)
# plt.xlabel('Total Score')
# plt.ylabel('Number of Matches')
# plt.title('IPL 2024 – Match Score Distribution')
# plt.show()

                                                #Multi-team run rate

# import matplotlib.pyplot as plt

# overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rcb_run_rate = [6.0, 7.2, 8.1, 8.8, 7.5, 9.2, 10.1, 9.8, 11.0, 10.5]
# csk_run_rate = [5.5, 6.8, 7.4, 8.2, 8.9, 9.1, 8.7, 10.2, 9.5, 11.2]

# plt.plot(overs, rcb_run_rate, label='RCB')
# plt.plot(overs, csk_run_rate, label='CSK')
# plt.xlabel('Overs')
# plt.ylabel('Run Rate')
# plt.title('RCB vs CSK – Run Rate per Over')
# plt.legend()
# plt.show()


                                                #subplots - 1*2 side by side panels 

# import matplotlib.pyplot as plt

# matches = [1, 2, 3, 4, 5, 6]
# rcb_scores = [178, 145, 198, 162, 210, 175]
# kkr_scores = [165, 188, 143, 201, 157, 184]

# fig, axes = plt.subplots(1, 2)
# axes[0].plot(matches, rcb_scores)
# axes[0].set_title('RCB Scores')
# axes[0].set_xlabel('Match')
# axes[0].set_ylabel('Runs')

# axes[1].plot(matches, kkr_scores)
# axes[1].set_title('KKR Scores')
# axes[1].set_xlabel('Match')
# axes[1].set_ylabel('Runs')

# plt.tight_layout()
# plt.show()

                                            #subplots - 2*2 - Four panel grid 

# import matplotlib.pyplot as plt

# matches = [1, 2, 3, 4, 5, 6, 7, 8]
# rcb_scores = [178, 145, 198, 162, 210, 175, 188, 201]
# mi_scores  = [165, 182, 155, 199, 172, 188, 160, 195]
# balls = [22, 35, 18, 41, 30, 28, 45, 33]
# runs  = [38, 58, 30, 72, 51, 44, 77, 55]
# all_scores = [142, 178, 165, 198, 134, 210, 156, 189, 172, 145,
#               185, 159, 173, 206, 152, 167, 188, 196, 143, 170]
# fig, axes = plt.subplots(2, 2)
# axes[0][0].plot(rcb_scores, matches)
# axes[0][0].set_title('RCB Line')

# axes[0][1].bar(mi_scores, matches)
# axes[0][1].set_title('MI Bar')

# axes[1][0].scatter(balls, runs)
# axes[1][0].set_title('Scatter')

# axes[1][1].hist(all_scores, bins=6)
# axes[1][1].set_title('Score Hist')

# plt.tight_layout()
# plt.show()

                                                #IPL 2024 Visual Dashboard

import matplotlib.pyplot as plt

overs = list(range(1, 21))
rcb_rr = [6.0, 7.5, 8.1, 9.2, 8.8, 10.1, 9.5, 11.0, 10.5, 12.0,
          11.5, 10.8, 12.5, 13.0, 11.8, 14.0, 13.5, 15.0, 14.5, 16.0]
csk_rr = [5.5, 6.8, 7.9, 8.5, 9.1, 9.8, 10.5, 9.9, 11.2, 10.8,
          12.0, 11.5, 13.2, 12.8, 13.5, 14.2, 13.8, 15.5, 14.8, 16.2]
batters    = ['Virat', 'Gill', 'Rohit', 'Rahul', 'SKY']
total_runs = [741, 702, 588, 520, 495]
balls_faced = [48, 35, 22, 41, 30, 18, 15, 55]
runs_scored = [72, 55, 48, 63, 44, 38, 27, 82]
all_scores  = [142, 178, 165, 198, 134, 210, 156, 189, 172, 145,
               185, 159, 173, 206, 152, 167, 188, 196, 143, 170]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0][0].plot(overs, rcb_rr, label='RCB')
axes[0][0].plot(overs, csk_rr, label='CSK')
axes[0][0].legend()
axes[0][0].set_title('Run Rate Comparision')
axes[0][0].set_xlabel('Over')
axes[0][0].set_ylabel('Run Rate')

axes[0][1].barh(batters, total_runs)
axes[0][1].set_title('Top Scorers')
axes[0][1].set_xlabel('Runs')
axes[0][1].set_ylabel('Batter')

axes[1][0].scatter(balls_faced, runs_scored)
axes[1][0].set_title('Balls vs Runs')
axes[1][0].set_xlabel('Balls Faced')
axes[1][0].set_ylabel('Runs')

axes[1][1].hist(all_scores, bins=8)
axes[1][1].set_title('Score Distribution')
axes[1][1].set_xlabel('Score')
axes[1][1].set_ylabel('Count')

plt.suptitle('IPL 2024 Dashboard', fontsize=14)
plt.tight_layout()
plt.show()