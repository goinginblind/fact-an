import numpy as np
import math
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt

file_name = input('Название файла без ".csv": ')
with open(f'{file_name}.csv', "r", encoding='utf8') as file:
    lines = file.readlines()

titles = lines[0].split(';')
titles_to_nmbrs ={} # пустой словарь

for no, title in enumerate(titles): #заполняем словарь
    title.strip()
    print(title)
    titles_to_nmbrs[title] = no

shape = (len(lines)-1, len(titles)) # матрица...
data = np.zeros(shape) #...заполненная нулями

for n_line, line in enumerate(lines[1:]): #заполняем числами
    fields = line.split(';')
    for n_field, field in enumerate(fields):
        data[n_line, n_field] = float(field.strip().replace(',', '.'))
print(data.T)

mtx_corr = np.corrcoef(data.T) #коэф корреляции трансп матрицы
print(mtx_corr)

[eig, vect] = np.linalg.eig(mtx_corr) #собств значения, собств вектора

print("Собственные значения:", eig)
print("Матрица собств. векторов:\n",vect, "\n\n")

# собств вектора по столбцам

vect.T @ vect #проверяем, что собственные вектора ортогональны (единичная матрица)

ord_eig = np.flip(eig.argsort()) #собств значения по убыванию
eig_ordered = eig[ord_eig]
vect_ordered = vect[:, ord_eig] #соответствующие им собств вектора


print("Собств. значения в порядке убывания:\n", eig_ordered.round(2))
print("Собств. векторы в соответствующем порядке:\n", vect_ordered.round(2))


th = 1.0
plt.plot (eig_ordered[::1], '--dr')
plt.plot ([0,8], [th, th],'-.g')
plt.title ('eigenvalues')
plt.plot(eig_ordered)
plt.savefig('plot-eigvals')

print ('Факторы:')
for i in range(0, len(eig)):
    if (eig_ordered[i] <= 1):    # метод главных компонент, каменистой осыпи, ищем все факторы, чьи собственные значения > 1
        break
    print(i+1,'---', eig_ordered[i].round(3))    # факторы
trunk = i    #кол-во факторов-1

eig_trunked = eig_ordered[0:trunk] #собственные значения факторов
print(eig_trunked.round(3))

vect_trunked = vect_ordered[:, 0:trunk] #собственные вектора факторов
print(vect_trunked.round(3))

print(vect_trunked.T @ vect_trunked) #показываем, что собственные вектора факторов ортогональны

f_loads = vect_trunked @ np.sqrt(np.diag(eig_trunked))
print(f_loads.round(3))
#факторные нагрузки для упорядоченных факторов как коэффициенты корреляции между признаками и факторами.
#элементы с.в. умножаем на корень из соответствующего собственного числа -> факторные нагрузки

fa = FactorAnalyzer(n_factors=trunk+1, method='principal', rotation="varimax")
fa.fit(data)

for i in range(9):
  print(titles[i], fa.loadings_[i].round(2))
#print(fa.loadings_.round(2))

