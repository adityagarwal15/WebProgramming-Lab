from django.shortcuts import render

def calculator_view(request):
    result = None
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    operation = request.POST.get("operation")

    if num1 and num2:
        num1, num2 = int(num1), int(num2)
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

    return render(request, "calculator/index.html", {"result": result})
