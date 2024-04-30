import subprocess
import matplotlib.pyplot as plt
import numpy as np
import time

last100py = []
last100cpp = []

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode().strip()

def parse_time(output):
    lines = output.split("\n")
    print("lines:", lines)
    seconds = (lines[-1].split(": ")[1])
    number = seconds.split(" ")[0]
    return number

def monitor(axs, cpp_time, py_time, iteration):
    print("i:", iteration, "adding cpp_time (type:", type(cpp_time), "):", cpp_time)
    print("i:", iteration,"adding py_time (type:", type(py_time), "):", py_time)
    axs[0].plot(iteration, cpp_time, 'b+--', markersize=8, label="Python")
    axs[0].plot(iteration, py_time, 'g+--', markersize=8, label="C++")


    if len(last100py) > 99:
        last100py.pop(0)
    if len(last100cpp) > 99:
        last100cpp.pop(0)
    last100py.append(py_time)
    last100cpp.append(cpp_time)
    average_py = np.mean(last100py)
    average_cpp = np.mean(last100cpp)
    axs[1].cla()
    axs[1].bar("Python", average_cpp, color='b')
    axs[1].bar("C++", average_py, color='g')
    # plt.pause(0.05)

if __name__ == "__main__":
    start_time = time.time()
    py_command = "./pyTokenGenerator"
    cpp_command = "./cppTokenGenerator"
    iterations = 100

    fig, axs = plt.subplots(1,2)
    axs[0].set_xlabel("Execution iteration")
    axs[0].set_ylabel("Execution time (s)")
    axs[0].set_title("Execution time")
    axs[0].legend(["Python", "C++"])
    axs[1].set_title("Average time execution")
    axs[1].set_xlabel("Language")
    axs[1].set_ylabel("100 last average time execution")

    for i in range(1, iterations + 1):
        cpp_time = float(parse_time(run_command(cpp_command)))
        py_time = float(parse_time(run_command(py_command)))
        monitor(axs, cpp_time, py_time, i)
    print("Python execution time: %.6f seconds" % (time.time() - start_time))
    plt.show()



