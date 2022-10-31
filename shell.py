import alphaka

while True:
  text = input('alphaka > ')
  result, error = alphaka.run('<stdin>', text) 

  if error: print(error.as_string())
  else: print(result)