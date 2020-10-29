ReadMe!
FE 595 HW3
Minghao Kang
===============================================================
This python script can only use for random companies data ONLY!
===============================================================

==========================================================================================
The first step to use this script is merge your dataset into a single pd.Dataframe.
In order to do it, please import merage_dataset.py and you have to find out what kind of file you have, if you have a .txt file, you need to use function txt_file(path) function to input your .txt file to a data frame. If you have a .csv file, you need to use csv_file(path) to input your .csv file to a data frame. After you have all your file coverted to data frame, you can use function meragedf to merge all of your files into one big data frame. 
==========================================================================================

==========================================================================================
After you have the merged dataset, you import sentiment analysis.py to do sentiment analysis. In this script, you can find a function called best_worst_idea which can tell you what is the best business idea and the worst business idea in your merged dataset.
There are two input, the first one is the file path of your merged dataset and the second input is number of ideas that you want to see. For example, if n = 1, the function will show you the best 1 idea and worst 1 idea, if n = 2, it will show you the best 2 idea and worst 2 idea.
==========================================================================================

==========================================================================================
In the third script, you can find out top n commonest words in your dataset, you can use function find_common after you import find 10 commonest.py. there are 2 input for this function, one is the file path of your merged dataset, and the second one is the number of  common words you want to see. For example, if n = 1, the function will show you the most common word, if n = 2, it will show you the top 2 common word in your merged dataset.
==========================================================================================

###############################
                              #
Thank you for using my script!#
                              #
###############################





