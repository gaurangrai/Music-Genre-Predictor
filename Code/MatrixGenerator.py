import pandas as pd
import CleanData as cd
import numpy as np
from random import shuffle
from multiprocessing.dummy import Pool as ThreadPool
import json

tracks = pd.read_csv('input_csv/tracks.csv', index_col=0, header=[0, 1])
small = tracks[tracks['set', 'subset'] == 'genres_top']
genres = small[('track', 'genres_all')]
# print genres

genre_label = {'Folk':0,'Electronic':1,'Experimental':2,
                'Hip-Hop':3,'Instrumental':4,'International':5,
                'Pop':6,'Rock':7}

genre_csv = pd.read_csv('input_csv/genres.csv')
genre_id_label = {}
for key in genre_label.iterkeys():
    temp_id = genre_csv[genre_csv['title']==key].genre_id.values[0]
    genre_id_label[temp_id] = genre_label[key]


def getData(index_genre,direct):
    pool = ThreadPool(50)
    count = 0
    file_count = 1
    input_matrix = None
    output_matrix_temp = []
    file_name_array = []
    for key in index_genre:

        output_genres = []
        val = genres[key]
        val = val[1:len(val) - 1].split(",")
        for tem_gen in val:
            try:
                tem_gen = int(tem_gen)
                if tem_gen in genre_id_label:
                    output_genres.append(genre_id_label[tem_gen])
            except:
                continue
        # output_matrix.extend(output_genres)
        if len(output_genres) != 0:
            file_name = '{:06d}'.format(key)
            file_name_array.append(file_name)
            output_matrix_temp.append(output_genres)


    output_matrix_temp = output_matrix_temp[::-1]
    output_matrix = []
    temp_file_array = []


    for idx,filename in enumerate(file_name_array):
        temp_file_array.append(filename)
        count += 1

        if count == 100 or idx == len(file_name_array)-1:
            mp3ToMatrixResult = pool.map(cd.mp3ToMatrix, temp_file_array)

            for (temp_matrix,isTrue) in mp3ToMatrixResult:
                print "File Number:"+str(file_count)
                output_temp = output_matrix_temp.pop()
                if isTrue and temp_matrix.shape[1] == 12500:

                    try:
                        if input_matrix == None:
                            if np.all(np.isfinite(temp_matrix)):
                                input_matrix = temp_matrix
                            else:
                                continue
                    except:
                        if np.all(np.isfinite(temp_matrix)):
                            input_matrix = np.concatenate((input_matrix, temp_matrix), axis=0)
                        else:
                            continue
                    output_matrix.append(output_temp)

            if len(output_matrix) != 0:
                input_matrix = pd.DataFrame(input_matrix)
                input_matrix.to_csv(direct+"/input/input_data_"+str(file_count)+".csv", sep=',', index=False)
                json.dump(output_matrix, open(direct+"/output/output_data_"+str(file_count)+".txt", "wb"))

            file_count += 1
            count = 0
            input_matrix = None
            output_matrix = []
            temp_file_array = []

    #     # except:
    #     #     break



index_genre = list(genres.index)
shuffle(index_genre)
current_index = len(index_genre)*60/100
training_data = index_genre[:current_index]
test_data = index_genre[current_index:]


#training
getData(training_data,"song_csv_training")



#test
getData(test_data,"song_csv_test")