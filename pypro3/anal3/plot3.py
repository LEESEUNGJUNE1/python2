# matplotlib 모듈의 기능 보충용 seaborn 
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info())

sns.displot(titanic['age'])
plt.show()

sns.boxplot(y='age', data = titanic, palette = 'Paired')    # pallett = 'Paired' 그래프 색이 흐릿하다.
plt.show()

#sns.countplot(x="class", data=titanic)
sns.countplot(x="class", data=titanic, hue="who")   # hue = "카테고리형 변수"
plt.show()

t_pivot = titanic.pivot_table(index="class",columns="sex",aggfunc="size")
print(t_pivot)
sns.heatmap(t_pivot, cmap=sns.light_palette(color="gray", as_cmap=True), annot=True, fmt="d")
plt.show()

