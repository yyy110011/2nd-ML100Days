#from base.base_data_loader import BaseDataLoader
import pandas as pd
import numpy as np
import PIL
import os

class catdogloader():
    def __init__(self):
        #super(catdogloader, self).__init__(config)
        self.X_train, self.y_train, self.X_test = self.load_data()
        print(os.getcwd())
        #self.X_data, self.y_train = self.load_data()
    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test


    def load_data(self):
        #split_th = self.config.split_threshold
        #data = pd.read_csv(self.config.data_path, header=None)
        #current_path = os.getcwd()
        #di = dict()
        pic_size = 128
        dataset_path = ['train', 'test']
        classes = ['dogs', 'cats']

        X_data = []
        y_data = []
        X_test = []
        #yListData = [[] for _ in range(4)]
        #yListVal = [[] for _ in range(4)]
        for root in dataset_path:
            if root == 'train':
                for c_idx, c in enumerate(classes):
                    for name in os.listdir(os.path.join(root, c)):
                        img_name = os.path.join(root, c, name)
                        img = PIL.Image.open(img_name).convert('RGB')
                        img = img.resize((pic_size,pic_size), PIL.Image.ANTIALIAS)
                        X_data.append(np.array(img)/255)
                        temp = np.zeros(2)
                        temp[c_idx] = 1
                        y_data.append(temp)
            elif root == 'test': 
                for i in range(400):
                    print(i)
                    img_name = os.path.join(root, '%03d' % i + '.jpg')
                    img = PIL.Image.open(img_name).convert('RGB')
                    img = img.resize((pic_size,pic_size), PIL.Image.ANTIALIAS)
                    X_test.append(np.array(img)/255)
                break 
                    
        X_data = np.array(X_data)
        y_data = np.array(y_data)
        X_test = np.array(X_test)    
        #y_train = (y_train

        indices = np.random.permutation(X_data.shape[0])
        print(indices)
        #training_idx, test_idx = indices[:3500], indices[3500:]
        X_train = X_data[indices,:]
        y_train = y_data[indices]
        #x_train = X_data[:split_th, :, :, :]
        #x_val = X_data[split_th:, :, :, :]

        #y_train = yListData
        #y_val = yListVal

        #print('Shape of x_train : ', np.shape(x_train))
        #print('Shape of y_train : ', np.shape(y_train))
        #print('Shape of x_val   : ', np.shape(x_val))
        #print('Shape of y_val   : ', np.shape(y_val))
        #return X_data, y_train
        return X_train, y_train, X_test