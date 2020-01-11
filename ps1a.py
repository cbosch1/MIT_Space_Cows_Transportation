###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}

    with open(filename) as file:

        for line in file:

            linelist = line.split(',')

            cows[linelist[0]] = int(linelist[1])

    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    sorted_cow = sorted(cows,key=cows.get,reverse=True)

    result = []

    while sorted_cow != []:
        
        trip = []

        total_weight = 0

        for cow in sorted_cow:
            
            if total_weight + cows[cow] <= limit:

                trip.append(cow)

                total_weight += cows[cow]
        
        result.append(trip)

        temp = []

        for cow in sorted_cow:

            if cow not in trip:

               temp.append(cow) 

        sorted_cow = temp

    return result
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    for plan in get_partitions(cows):

        overweight = False

        for trip in plan:

            trip_weight = 0

            for cow in trip:

                trip_weight += cows[cow]

            if trip_weight > limit:

                overweight = True

        if not overweight:
            
            return plan
        
# Problem 4
def compare_cow_transport_algorithms(cows):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.perf_counter()

    greedy = greedy_cow_transport(cows)

    end = time.perf_counter()

    greedy_time = end - start


    start = time.perf_counter()

    brute = brute_force_cow_transport(cows)

    end = time.perf_counter()

    brute_time = end - start


    print('Greedy result:', len(greedy), 'trips')
    
    print('Greedy time:', greedy_time, 'seconds')

    print('Brute result:', len(brute), 'trips')

    print('Brute time:', brute_time, 'seconds')


cows = load_cows('ps1_cow_data.txt')

compare_cow_transport_algorithms(cows)

