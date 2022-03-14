import subprocess
process=subprocess.run(["echo",Welcome to india"], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
result=process.communicate()
print(result.stdout)
