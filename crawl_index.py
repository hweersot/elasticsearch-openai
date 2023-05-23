from es_gpt import ESGPT
import pandas as pd
from tqdm import tqdm

def get_text_from_web(x):
    question_title = x['question_title']
    question_detail = x['question_detail']
    answer = x['answer']
    return str(question_title) + str(question_detail),str(answer)
#    return str(question_title) + str(question_detail) + "\n" + str(answer)


# Create an instance of the ESGPT class
#esgpt = ESGPT(index_name="period")
esgpt = ESGPT(index_name="pad")

path='data/'
'''
file_names=['input_기저귀_100.csv',
            'input_생리_100.csv',
            'input_생리대_100.csv',
            'input_아기_100.csv',
            'input_이유식_100.csv',
            'input_임신_100.csv']
'''
file_names=['input_생리대_100.csv',]
#같은 index 쓸 애들은 url doc_id 기준 중복 제거 필요 (미반영)
for file_name in file_names:
    df=pd.read_csv(path+file_name)
    # Index each paper in Elasticsearch
    print('Uploading '+file_name)
    l=len(df)
    for i,row in df.iterrows():
        print(i/l)

        # Index the paper in Elasticsearch
        question,answer = get_text_from_web(row)

        #메타데이터(전문가,스펙,q전문,날짜 등) 추가
        _dict = {'author':row['author'].strip(), 'date':row['date'].strip(), 'question_title':row['question_title'].strip(),'q_text':question,'a_text_500':answer[:500]}
        id = row['url']+row['author'].strip()

        esgpt.index(doc_id=id, doc=_dict, a_text=answer)