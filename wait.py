import subprocess
process=subprocess.Popen(["ls",-"la"])
process.wait()
print("completed")
