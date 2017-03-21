import csv, itertools

with open('simpsons_ep-charFixed2Weights.csv', 'w', newline='') as csvW:
	total = 0

  with open('simpsons_ep-charFixed2.csv') as csvfile:
		for i in range(1, 652):
		  for j in range(1, 652):
        epReader = csv.reader(csvfile)
        next(epReader)

        s_counter = i
        t_counter = j
        total = 0

        for row in epReader:
        	curr_s = int(row[0])
        	curr_t = int(row[1])

        	if s_counter == curr_s and t_counter == curr_t:
        		total = total + 1

        if total > 0:
        	new_row = []
        	new_row.append(i)
        	new_row.append(j)
        	new_row.append("Undirected")
        	new_row.append(total)
        	row_writer = csv.writer(csvW, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        	row_writer.writerow(new_row)

