class Recommender():

    def singleRecommendation(data, foodName, k = 6):
        vector = CountVectorizer()
        t1 = vector.fit_transform(data['foodDescription'])
        cos_similarity = cosine_similarity(t1, t1).argsort()[:,::-1] 

        foodIdx = data[data['foodName'] == foodName].index.values[0]
        simIdx = cos_similarity[foodIdx, :k]
        simIdx = simIdx[1:]
        rec = []
        for r in simIdx:
            food = data.iloc[r]
            rec.append(food['foodName']) # r : 전체 dataset에서의 index
        return rec
    
    def doubleRecommendation(data, k = 15, *foodName):
        numUser = len(foodName)
        commonFeatures = []
        idxList = []
        for n in range(numUser):
            userIdx = data[data['foodName'] == foodName[n]].index.values[0]
            idxList.append(userIdx)
            foodinfo = data[data['foodName'] == foodName[n]].values.tolist()[0]
            commonFeatures.append(foodinfo[1])
        feature = []
        string = ''
        for i in commonFeatures:
            concat = "".join(i)
            string += concat
        feature.append(string)
        for i in feature:
            features = i.split(' ')
            features = set(features)
            features = list(features)
        features = ' '.join(features)
        commonFeature = {'foodName': 'COMMON', 'foodDescription': features}
        data = data.append(commonFeature, ignore_index = True)
        
        vector = CountVectorizer()
        t1 = vector.fit_transform(data['foodDescription'])
        cos_similarity = cosine_similarity(t1, t1).argsort()[:,::-1] 
        
        foodIdx = data[data['foodName'] == 'COMMON'].index.values[0]
        simIdx = cos_similarity[foodIdx, :k]
        simIdx = simIdx[1:]
        simIdx = simIdx.tolist()
        for dup in idxList:
            if dup in simIdx:
                simIdx.remove(dup)
        rec = []
        for r in simIdx:
            food = data.iloc[r]
            rec.append(food['foodName'])
        return rec
