class MinMaxC:
  try:
    import pandas as pd 
    from scipy import stats as s
  except ImportError as e:
    %pip install pandas
    %pip install scipy
    import pandas as pd 
    from scipy import stats as s
  data=[]
  numclass=[]
  max_dic={}
  min_dic={}
  target = []
  def fi(self,X,Y):
    self.data = pd.concat([X, Y], axis=1, ignore_index=True)
    self.target=Y.unique()
    for i in self.target:
      temp=self.data[Y==i]
      temp=temp.iloc[: , :-1]
      self.max_dic[i]=temp.max()
      self.min_dic[i]=temp.min()

  def pre(self,X):
    y_predict=[]
    for l in range(X.shape[0]):
      predict=[]
      for j in self.target:
        for k in range(X.shape[1]):
          if self.max_dic[j][k]>=X.iloc[l,k] and self.min_dic[j][k]<=X.iloc[l,k]:
            predict.append(j)
      y_predict.append((s.mode(predict)[0]))  
    return y_predict

