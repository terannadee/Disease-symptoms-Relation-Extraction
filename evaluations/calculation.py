

def calculate(tp,fn,fp):
    precision = tp /(tp+fp)
    recall = tp/(tp+fn)
    fmesh = 2 * ((precision*recall)/(precision+recall))

    print(precision,recall,fmesh)


calculate(299,101,182)