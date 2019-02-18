import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn("Для выполения этой программы необходима как минимум \
        версия Python 3.0", 
        RuntimeWarning)
else:
    print('Нормальное продолжение')