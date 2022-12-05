import random

file = open('1000000Rep.txt', 'w')

sub_array = []
minimum = int(input("Enter Minimum:  "))
maximum = int(input("Enter Maximum:  "))
repetitions = int(input("Enter Repetitions:  "))
trials = int(input("Enter Trials:  "))
numlim = int(input("Enter the highest event number inclusive:  "))
necessaryPositives = int(input("Enter the number of necessary positives for a trial to be counted:  "))

def randominput(minimum, maximum, repetitions, trials, numlim, necessaryPositives):
    succeededTrials = 0
    for num1 in range(trials):
        count = 0
        for num2 in range(repetitions):
            randomNumber = random.randint(minimum, maximum)
            if(randomNumber <= numlim):
                count += 1
            sub_array.append(randomNumber)
        file.writelines([f"\nTrial {num1 + 1}: {sub_array}", f"\n{count} of {repetitions}"])
        if(count >= necessaryPositives):
            succeededTrials += 1
        sub_array.clear()
    file.write(f"\n{succeededTrials} of {trials} ({succeededTrials/trials}) probability")
   
randominput(minimum, maximum, repetitions, trials, numlim, necessaryPositives)