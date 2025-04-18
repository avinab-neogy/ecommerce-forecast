from tscv import GapRollForward

def walk_forward_validation(model, data, window_size=30):
    cv = GapRollForward(
        min_train_size=window_size*3,
        gap_size=7,
        max_test_size=window_size
    )
    
    scores = []
    for train_idx, test_idx in cv.split(data):
        train = data.iloc[train_idx]
        test = data.iloc[test_idx]
        
        model.fit(train)
        score = model.score(test)
        scores.append(score)
    
    return np.mean(scores)
