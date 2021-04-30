import joblib

def textClass(text, modelsPath):

    sgd = joblib.load(modelsPath + 'svg_model.pkl')
    knn = joblib.load(modelsPath + 'knn_model.pkl')
        
    knnPred = ''
    sgvPred = ''

    if knn:   
        if (text == ''):
            print('Empty text!')
        else:
            predicted_text = knn.predict([text])
            knnPred = predicted_text[0]
    else:
        print('KNN model not found!')

    if sgd:
        if (text == ''):
            print('Empty text!')

        else:
            predicted_text = sgd.predict([text])
            sgvPred = predicted_text[0]

    else:
        print('SVG not found!')
        
    if knnPred == 0: knnPred = 'normal'
    if knnPred == 1: knnPred = 'suicide'
    if knnPred == 3: knnPred = 'extremism'

    if sgvPred == 0: sgvPred = 'normal'
    if sgvPred == 1: sgvPred = 'suicide'
    if sgvPred == 3: sgvPred = 'extremism'

    return({
        'knn':knnPred,
        'sgv':sgvPred
    })



print(textClass('Хачей нужно убивать', 'C:\\Users\\ОлежаГей\\Documents\\GitHub\\Плато?\\'))