price_list=[12.5, 35.68] #, 55.66, 12.34, 45.11, 23.43, 54.09, 54.77, 45.23, 90.98
rub="руб"
kop="коп"
new_list=[]
for element in price_list:
    new_list = f'{element:.2f}'.split('.')
    print(new_list)
# забуксовал на простом этапе добавления руб и коп к элементам списка,  
