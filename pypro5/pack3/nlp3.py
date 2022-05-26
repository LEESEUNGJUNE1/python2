# 단어의 빈도수를 이용해 문서의 특징 추출
# BOW(Back Of Words): 문서가 가지는 모든 단어, 문맥, 순서를 무시하고 단어에 대해 빈도 수를 부여해 벡터를 생성

# CountVectorizer : 단순하게 텍스트에서 단위별 등장횟수를 카운팅하여 수치백터(Bow)화
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

contents = ['How to format my hard disk','Hard disk format format problems']    # 중복 배제, 소문자로 변환, 사전순으로 출력해준다.

count_vec = CountVectorizer(analyzer='word', min_df = 1)    # 'word', 'char'
tran = count_vec.fit_transform(raw_documents=contents)
print(tran)
print(count_vec.get_feature_names())
print(tran.toarray())

print('-----------')
# TfidfVectorizer : 하나의 문단에서 자주 나오는 단어에 대해 가중치를 높게 부여하거나,
# 전체 문서의 모든 문단에서 자주 등장하는 단어에 대해서는 패널티를 부여
tfidf_vec = TfidfVectorizer(analyzer='word', min_df = 1)
train_idf = tfidf_vec.fit_transform(raw_documents=contents)
print(train_idf)
print(tfidf_vec.get_feature_names())
print(train_idf.toarray())