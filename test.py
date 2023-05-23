import pandas as pd

df = pd.DataFrame(columns=["q_text", "a_text", "n_tokens", "embeddings"])
dfs=[{'_index': 'period', '_id': 'https://www.a-ha.io/questions/4c33c55d42b82ef58f80022161ed3753?aha_term=%EC%83%9D%EB%A6%AC\n          박기섭 의사\n        ', '_score': 3.7893782, '_source': {'author': '박기섭 의사', 'date': '2023. 04. 14. 17:39', 'question_title': '생리는 필요없는 피가 나오는 건가요?', 'a_text': '안녕하세요. 생리혈은 보통 자궁내벽이 착상을 위해 두꺼워지는데 착상이 이루어지지않으면 두꺼워진 자궁내벽이 탈락되어 나오는피입니다. 일반적으로는 문제가 생기지않으나 심한경우라면 과다출혈일수있어 가까운 산부인과에서 확인하셔야  합니다', 'embeddings_dict_list': [{'q_text': '생리는 필요없는 피가 나오는 건가요. 생리할 때마다 느끼는 건데요. 피가 이렇게 많이 나오는데도 안 죽네 싶거든요. 생리할 때 나오는 피는 필요없는 피가 나오는 건가요.', 'n_tokens': 96, 'embeddings': [0.41764500737190247, 0.41764500737190247]}]}}, {'_index': 'period', '_id': 'https://www.a-ha.io/questions/4c33c55d42b82ef58f80022161ed3753?aha_term=%EC%83%9D%EB%A6%AC\n          임종한 의사\n        ', '_score': 3.7893782, '_source': {'author': '임종한 의사', 'date': '2023. 04. 14. 18:37', 'question_title': '생리는 필요없는 피가 나오는 건가요?', 'a_text': '(제가 아는 범위에선) 여성의 배란 주기에서, 착상이 이루어지면 수정이 가능하도록 비후된 자궁내 점막이 일정  기간이 지난 후, 탈락하면서 나오는 ���이 생리로 알고 있습니다. (그 동안 에스트로젠, 프로게스테론 등 호르몬 작용에 의해 일어나게 됩니다)', 'embeddings_dict_list': [{'q_text': '생리는 필요없는 피가 나오는 건가요. 생리할 때마다 느끼는 건데요. 피가 이렇게 많이 나오는데도 안 죽네 싶거든요. 생리할 때 나오는 피는 필요없는 피가 나오는 건가요.', 'n_tokens': 96, 'embeddings': [0.41764500737190247, 0.32263755798339844]}]}}]
s=1

for hit in dfs:
    embeddings_dict_list = hit['_source']['embeddings_dict_list']
    for embeddings_dict in embeddings_dict_list:
        s=pd.DataFrame(embeddings_dict)
        df = pd.concat([df,pd.DataFrame(embeddings_dict)], ignore_index=True)

#print(len(df['embeddings']))
print(pd.DataFrame.from_dict(dfs[0]['_source']['embeddings_dict_list'][0],orient='columns'))
print(pd.DataFrame.from_dict(dfs[0]['_source']['embeddings_dict_list'][0],orient='index').T)