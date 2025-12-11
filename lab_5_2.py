name = 'patric log'
print(name)

result = ''
for i in name:
    result = result + i + '_'
print(result)


result1 = result.upper()
print(result1)

result_code1 = []
for i in result1:
    code1 = ord(i)
    result_code1.append(code1)
print(result_code1)


result2 = result.lower()
print(result2)

result_code2 = []
for i in result2:
    code2 = ord(i)
    result_code2.append(code2)
print(result_code2)

print(max(max(result_code1), max(result_code2)))
print(min(min(result_code1), min(result_code2)))