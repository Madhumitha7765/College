import os


if __name__ == "__main__":

    while True:
        print("\n_____________________________________")
        print("Enter the action you wish to perform : ")
        print("1.View analysis of top 50 songs on Spotify ")
        print("2.Features of Sound distributions in Spotify Songs")
        print("3.Basic Analysis of Songs in Spotify ")
        print("4.EXIT")

        choice = input("Enter your choice :: ")
        if int(choice) ==1 :
            # redirects to top50_analysis file
            os.system('python Top50_analysis.py')
        elif int(choice) ==2:
            # redirects to sound features file
            os.system('python sound_features.py')
        elif int(choice) ==3:
            # redirects to song_analysis file
            os.system('python song_analysis.py')
        elif int(choice) ==4:
            break
        else:
            print("\ninvalid choice,Re-enter again\n")
            continue
