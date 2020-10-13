import json
import matplotlib.pyplot as plt
import statistics
binary_file = open('output_exp/binary_search.json')
binary_dict = json.load(binary_file)
indexed_file = open('output_exp/indexed_search.json')
indexed_dict = json.load(indexed_file)
linear_file = open('output_exp/linear_search.json')
linear_dict = json.load(linear_file)
linear_plus_merge_file = open('output_exp/linear_search_plus_merge.json')
linear_plus_merge_dict = json.load(linear_plus_merge_file)
linear_plus_binary_file = open('output_exp/linear_search_plus_binary.json')
linear_plus_binary_dict = json.load(linear_plus_binary_file)
binary_file.close()
indexed_file.close()
linear_file.close()
linear_plus_merge_file.close()
linear_plus_binary_file.close()

x_range = range(14)
T_SIZE = [10**6, 10**7, int(1.12*10**7), int(1.15*10**7), int(1.18*10**7), int(1.5*10**7)]

y_binary_io = []
y_binary_io_std = []
y_binary_t = []
y_binary_t_std = []

y_indexed_io = []
y_indexed_io_std = []
y_indexed_t = []
y_indexed_t_std = []

y_linear_io = []
y_linear_io_std = []
y_linear_t = []
y_linear_t_std = []  

y_linear_plus_binary_io = []
y_linear_plus_binary_io_std = []
y_linear_plus_binary_t = []
y_linear_plus_binary_t_std = [] 

y_linear_plus_merge_io = []
y_linear_plus_merge_io_std = []
y_linear_plus_merge_t = []
y_linear_plus_merge_t_std = []  

for t in T_SIZE:
    current_binary_io = []
    current_binary_t = [] 
    current_indexed_io = []
    current_indexed_t = [] 
    current_linear_io = []
    current_linear_t = [] 
    current_linear_plus_binary_io = []
    current_linear_plus_binary_t = [] 
    current_linear_plus_merge_io = []
    current_linear_plus_merge_t = []
    for i in x_range:
        current_binary_io.append(binary_dict[str(t)][str(i)]["I/Os"])
        current_binary_t.append(binary_dict[str(t)][str(i)]["time"])
        current_indexed_io.append(indexed_dict[str(t)][str(i)]["I/Os"])
        current_indexed_t.append(indexed_dict[str(t)][str(i)]["time"])
        current_linear_io.append(linear_dict[str(t)][str(i)]["I/Os"])
        current_linear_t.append(linear_dict[str(t)][str(i)]["time"])
        current_linear_plus_binary_io.append(linear_plus_binary_dict[str(t)][str(i)]["I/Os"])
        current_linear_plus_binary_t.append(linear_plus_binary_dict[str(t)][str(i)]["time"])
        current_linear_plus_merge_io.append(linear_plus_merge_dict[str(t)][str(i)]["I/Os"])
        current_linear_plus_merge_t.append(linear_plus_merge_dict[str(t)][str(i)]["time"])

    y_binary_io.append(statistics.mean(current_binary_io))
    y_binary_io_std.append(statistics.stdev(current_binary_io))
    y_binary_t.append(statistics.mean(current_binary_t))
    y_binary_t_std.append(statistics.stdev(current_binary_t))

    y_indexed_io.append(statistics.mean(current_indexed_io))
    y_indexed_io_std.append(statistics.stdev(current_indexed_io))
    y_indexed_t.append(statistics.mean(current_indexed_t))
    y_indexed_t_std.append(statistics.mean(current_indexed_t))

    y_linear_io.append(statistics.mean(current_linear_io))
    y_linear_io_std.append(statistics.stdev(current_linear_io))
    y_linear_t.append(statistics.mean(current_linear_t))
    y_linear_t_std.append(statistics.stdev(current_linear_t))

    y_linear_plus_binary_io.append(statistics.mean(current_linear_plus_binary_io))
    y_linear_plus_binary_io_std.append(statistics.stdev(current_linear_plus_binary_io))
    y_linear_plus_binary_t.append(statistics.mean(current_linear_plus_binary_t))
    y_linear_plus_binary_t_std.append(statistics.stdev(current_linear_plus_binary_t))

    y_linear_plus_merge_io.append(statistics.mean(current_linear_plus_merge_io))
    y_linear_plus_merge_io_std.append(statistics.stdev(current_linear_plus_merge_io))
    y_linear_plus_merge_t.append(statistics.mean(current_linear_plus_merge_t))
    y_linear_plus_merge_t_std.append(statistics.stdev(current_linear_plus_merge_t))


plot_style = '-'
plt.plot(T_SIZE, y_linear_t, plot_style, color='red', label="Búsqueda lineal")
plt.plot(T_SIZE, y_linear_plus_binary_t, plot_style, color='green', label="Búsqueda lineal con búsqueda binaria")
plt.plot(T_SIZE, y_linear_plus_merge_t, plot_style, color='blue', label="Búsqueda lineal con merge")
plt.title("Duración experimental promedio para las modificaciones de la\n búsqueda lineal en cada ejecución para |P|=10^4 y diferentes |T|")
plt.xlabel("Tamaño de T (líneas)")
plt.ylabel("Tiempo en segundos")
plt.legend()
plt.show()


