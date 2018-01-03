import sys

sys.stderr.write('This is std error test\n')

sys.stderr.flush()

sys.stdout.write('This is a std out test\n')

try:
    print(float(sys.argv[0]) + 5)

except Exception:

    print('Enable to find the path')

finally:

    print('Next stuff...')