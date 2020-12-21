fp = open('xd.txt', 'w+')
for i in range(100):
    to_str = str(10) + '\n'
    fp.write(to_str)
fp.close()

from subprocess import PIPE, run

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout.strip('\n')

my_output = out("grep 10 xd.txt")
print(my_output)