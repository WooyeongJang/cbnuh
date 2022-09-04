echo 'Run'

/home/wyjang/anaconda3/envs/MRItoCTDCNN/bin/python \
/home/wyjang/IdeaProjects/cbnuh/backend/src/eh_preprocessing.py $1

/home/wyjang/anaconda3/envs/MRItoCTDCNN/bin/python \
/home/wyjang/IdeaProjects/cbnuh/backend/src/eh_pred.py $1

echo 'Done'
