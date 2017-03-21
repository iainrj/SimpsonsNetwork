import csv, itertools

prev_ep_num = 1

with open('simpsons_ep-charFixed.csv', 'w', newline='') as csvW:
	with open('simpsons_ep-char.csv') as csvfile:
		ep_list = []
		epReader = csv.reader(csvfile)
		next(epReader)

		for row in epReader:
			ep_num = int(row[0])

			if prev_ep_num == ep_num:
				ep_list.append(int(row[1]))
			else:
				# print(ep_list)
				while len(ep_list) > 0:
					item1 = ep_list.pop()
					for item2 in ep_list:
						new_row = []
						new_row.append(item1)
						new_row.append(item2)
						row_writer = csv.writer(csvW, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
						row_writer.writerow(new_row)
						# print(new_row)
				ep_list = []
				prev_ep_num = prev_ep_num + 1
				ep_list.append(int(row[1]))
		# print(ep_list)

