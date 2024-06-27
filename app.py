import numpy as np
from keras.preprocessing import image
from keras.layers import Dense
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Maxpooling2D
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import BatchNormalization
from keras.layers import Dropout



def classify():
    json_file = open('model.json','r')
    Loaded_model_json = json_file.read()
    json_file.close()
    Loaded_model = model_from_json(Loaded_model_json)

    #loads weights into new model

    Loaded_model.load_weights("model.h5")

    lable = ["A","AA","E","EE"]

    path = file 

    test_image = image.load_img(path,target_size = (128,128))

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image,axis = 0)
    result = Loaded_model.predict(test_image)

    fresult = np.max(result)
    lable2 = lable[result.argmax()]
    print(lable2)


def train():
    model = Sequential()
    model.add(Conv2D(32,kernal_size = (3,3) , activation = 'relu' , input_shape = (128,128,1)))
    model.add(Maxpooling2D(pool_size = (2,2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64,kernal_size =(3,3),activation = 'relu'))
    model.add(Maxpooling2D(pool_size = (2,2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64,kernal_size = (3,3)) , activation = 'relu')
    model.add(Maxpooling2D(pool_size = (2,2)))
    model.add(BatchNormalization())
    model.add(Conv2D(96,kernal_size = (3,3) , activation = 'relu'))
    model.add(Maxpooling2D(pool_size = (2,2)))
    model.add(BatchNormalization())
    model.add(Conv2D(32 ,kernal_size = (3,3), activation = 'relu'))
    model.add(Maxpooling2D(pool_size = (3,3)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation = 'relu'))
    model.add(Dropout(0.3))
    model.add(Dense(247 , activation = 'softmax' )) # 247

    model.compile(optimizer = 'adam' , loss = 'categorial_crossentrophy' ,metrics = ['accurracy'])


    train_datagen = ImageDataGenerator(rescale = None,
                                       shear_range = 0.2,
                                       zoom_range = 0.2,
                                       horizontal_flip = True
    )

    test_datagen = ImageDataGenerator(rescale = 1./255)

    training_set = train_datagen.flow_from_directory('/train_images',
                                                     target_size = (128,128),
                                                     batch_size = 8,
                                                     class_mode = 'categorical')

    #print(test_datagen)
    lables = (training_set.class_indices)
    print(lables)


    training_set = test_datagen.flow_from_directory('/train_images',
                                                    target_size =(128,128),
                                                    batch_size = 8,
                                                    class_mode = 'categorical')


    lables2 = (test_set.class_indices)
    print(lables2)



    model.fit_generator(training_set,
                        steps_per_epoch = 100,
                        epochs = 10,
                        validation_data = test_set,
                        validation_steps = 125)



    # making new predictions 

    model_json = model.to_json()
    with open("model.json","w") as json_file:
        json_file.write(model_json)

    #serialize weights to HDF5

        model.save_weights("model.h5")
        print("saved model to disk")


    



#train()
#classify