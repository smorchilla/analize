import ktrain

def loadBert(path):
    predictor_load = ktrain.load_predictor(path)
    return(predictor_load)

def textClass(text, model):
    predictor_load = model
    text = predictor_load.predict(text)
    
    if text == "class_0": text = 'normal'
    if text == "class_1": text = 'suicide'
    if text == "class_2": text = 'politics'
    if text == "class_3": text = 'extremism'

    return({
        'bert': text
    })

print(textClass('Сегодня хорошая погода, единая Россия борется с нацистами', loadBert('C:\\Users\\zhiti\\Documents\\GitHub\\analize\\web\\bert-2')))