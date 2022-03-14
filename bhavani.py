import subprocess
result=subprocess.run(["echo","Welcome to India"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
print(result.stdout)
