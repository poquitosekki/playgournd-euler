# PROJECT 1
# MULTIPLE OF 3 OR 5

#!/usr/bin/python3
# This is just fa Shebang line

def sum_of_div_by_35(to=10):
    result = 0
    for i in range(1, to):
        if div_by_35(i):
            result += i

    return result

def div_by_35(i):
    return True if (i % 3 == 0) or (i % 5 == 0) else False

print(sum_of_div_by_35())

# END
# NOTES :
# So there is no reason to use xrange instead of range in this case because python3's range is behaving now like xrange of pyhton 2
#
#
#
