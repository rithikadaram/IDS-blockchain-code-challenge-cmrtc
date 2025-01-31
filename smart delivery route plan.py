import itertools  
import math  

# Function to calculate the Euclidean distance between two locations  
def calculate_distance(point1, point2):  
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)  

# Function to find the optimal delivery route  
def find_optimal_route(locations, priorities):  
    # Combine the locations and priorities  
    deliveries = list(zip(locations, priorities))  

    # Sort deliveries by priorities: high < medium < low  
    priority_order = {"high": 1, "medium": 2, "low": 3}  
    deliveries.sort(key=lambda x: priority_order[x[1]])  

    sorted_locations = [d[0] for d in deliveries]  # Extract sorted locations  

    # Generate all permutations of the sorted locations to find the optimal route  
    min_distance = float('inf')  
    best_route = []  

    for perm in itertools.permutations(sorted_locations):  
        total_distance = sum(calculate_distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))  
        
        if total_distance < min_distance:  
            min_distance = total_distance  
            best_route = perm  

    return best_route, min_distance  

# Function to get user input for locations and priorities  
def get_user_input():  
    locations = []  
    priorities = []  

    num_deliveries = int(input("Enter the number of delivery locations: "))  
    
    for i in range(num_deliveries):  
        location_input = input(f"Enter location {i + 1} as (x, y): ")  
        location = tuple(map(int, location_input.strip("()").split(",")))  # Convert input to a tuple of integers  
        locations.append(location)  

        priority = input(f"Enter priority for delivery {i + 1} (high, medium, low): ").strip().lower()  
        while priority not in ["high", "medium", "low"]:  
            priority = input("Invalid input! Please enter priority (high, medium, low): ").strip().lower()  
        priorities.append(priority)  

    return locations, priorities  

# Main part of the program  
def main():  
    # Get user input  
    locations, priorities = get_user_input()  

    # Find the optimal route  
    optimized_route, total_distance = find_optimal_route(locations, priorities)  

    # Output the results  
    print("Optimized Route:", optimized_route)  
    print("Total Distance: {:.2f} units".format(total_distance))  

# Execute the main function  
if __name__ == "__main__":  
    main()