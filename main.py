def display_inverted_asterisk_triangle(rows):
  for i in range(rows, 0, -1):
      for j in range(i):
          print('*', end='')
      print()

# Number of rows in the inverted triangle
num_rows_inverted = 20

# Call the function to display the inverted asterisk triangle
display_inverted_asterisk_triangle(num_rows_inverted)
