if __name__ == "__main__":
  import csv

  # file = open("country.csv", encoding = "UTF-8")
  # reader = csv.reader(file)
  # for line in reader:
  #   print(line)
  # file.close()

  # with open("country.csv", "r", encoding="utf8") as file:
  #   reader = csv.reader(file)
  #   for line in reader:
  #     print(line)
  #   # don’t need to explicitly call the close() method

  # with open("country.csv", encoding="utf8") as file:
  #   reader = csv.reader(file)
  #   start_index = 1
  #   for index, line in enumerate(reader, start_index):
  #     if index == 1:
  #       print("Header:")
  #       print(line)
  #       print("Data")
  #     else:
  #       print(line)

  # with open("country.csv", encoding="utf8") as file:
  #   reader = csv.reader(file)
  #   # skip the header
  #   next(reader)

  #   for line in reader:
  #     print(line)

  # total_area = 0

  # with(open("country.csv", "r", encoding="utf8")) as file:
  #   reader = csv.reader(file)
  #   next(reader)

  #   for line in reader:
  #     total_area += float(line[1])

  # print(total_area)

  # with(open("country.csv", "r", encoding = "utf8")) as file:
  #   reader = csv.DictReader(file)
  #   next(reader)

  #   for line in reader:
  #     print(f"The area of {line['name']} is {line['area']} km2")

  field_names = ["name", "area", "code2", "code3"]
  with(open("country.csv", "r", encoding = "utf8")) as file:
    reader = csv.DictReader(file, field_names)
    next(reader)

    for line in reader:
      print(f"The area of {line['name']} is {line['area']} km2")