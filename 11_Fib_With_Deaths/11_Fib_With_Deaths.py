#functions

#calculates the number of offspring produced
def getOffspring(age_tracker):
    total_reproducing = 0 #stores the desired value

    #iterate over each item in the list, with an index value j
    for j, n_age in enumerate(age_tracker):
        if j == 0:
            continue #skip the first entry

        total_reproducing += n_age #add all entries (other than the first) to the running total
    
    return total_reproducing



#MAIN FOLLOWS
#------------
#collect the data
#f = open("rosalind_fibd.txt", "r")
#data = f.read()
#f.close()

#split the data
#data_split = data.split(" ")

#convert to int
#inputs = []
#for i in data_split:
#    inputs.append(int(i))

inputs = [98, 20]

total_months = inputs[0] #length of the simulation
death_age = inputs[1]    #logically, this will always be 2 or larger since it takes one month to mature

age_tracker = [] #list of quantities of each age, [1,2,...,death_age] (we start with 1 age 1)

total_pop = 0 #stores the total population for output at the end of the simulation

 
#iterate for every month
for i in range(total_months):
    current_offspring = 0 #stores a temp value

    if i == 0: 
        age_tracker.insert(0, 1) #insert the first immature individual
        total_pop += 1 #add it the the total pop
        print(total_pop)

    elif i < death_age: #no need to remove dead individuals 
        current_offspring = getOffspring(age_tracker)  #get how many offspring will be produced 
        total_pop += current_offspring                 #add the offspring to the total population
        age_tracker.insert(0, current_offspring)       #insert the immature individuals at the front of the age_tracker list

    elif i < total_months: #must remove dead individuals
        current_offspring = getOffspring(age_tracker)  #get how many offspring will be produced 
        total_pop += current_offspring                 #add the offspring to the total population
        total_pop -= age_tracker[death_age - 1]        #remove the oldest individuals in the age_tracker list from the total population 
        age_tracker.pop(death_age - 1)                 #remove the oldest individuals from the age_tracker list
        age_tracker.insert(0, current_offspring)       #add the immature individuals to the age_tracker list

print(total_pop)

#create and output file
#out = open("rosalind_fibd_output.txt", "w")
#out.write(str(total_pop))
#out.close()