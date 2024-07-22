import numpy as np

a = 2.6090275933683564
e = 0.38967323455652847
i = 0.2886307414612506
O = 4.224496597238895
w = 1.6304233289390568


r0_eclp = np.array([
    [np.cos(O), -np.sin(O), 0],
    [np.sin(O), np.cos(O), 0],
    [0, 0, 1]
]) @ np.array([
    [1, 0, 0],
    [0, np.cos(i), -np.sin(i)],
    [0, np.sin(i), np.cos(i)]
    
]) @ np.array([
    [np.cos(w), -np.sin(w), 0],
    [np.sin(w), np.cos(w), 0],
    [0, 0, 1]
]) @ np.array([a, 0, 0])

r1_eclp = np.array([
    [np.cos(O), -np.sin(O), 0],
    [np.sin(O), np.cos(O), 0],
    [0, 0, 1]
]) @ np.array([
    [1, 0, 0],
    [0, np.cos(i), -np.sin(i)],
    [0, np.sin(i), np.cos(i)]
    
]) @ np.array([
    [np.cos(w), -np.sin(w), 0],
    [np.sin(w), np.cos(w), 0],
    [0, 0, 1]
]) @ np.array([0, a*np.sqrt(1-e**2), 0])

print(r0_eclp, r1_eclp)