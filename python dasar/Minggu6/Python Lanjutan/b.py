def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-2)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(8)