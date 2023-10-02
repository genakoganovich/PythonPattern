import sys
import io

output_stream = sys.stdout
sys.stdout = io.StringIO()

# Вывод текста в stdout
print("Пример текста в stdout")

# Получение вывода из stdout
output = sys.stdout.getvalue()

# Вывод результата
sys.stdout = output_stream
print('hello ' + output)
