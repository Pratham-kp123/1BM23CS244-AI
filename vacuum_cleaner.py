def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    
    location_input = input("Enter Location of Vacuum (A/B): ")  # user_input of location vacuum is placed
    status_input = input("Enter status of " + location_input + " (0=Clean, 1=Dirty): ")  # status of vacuum location
    status_input_complement = input("Enter status of other room (0=Clean, 1=Dirty): ")  # status of other room
    
    print("Initial Location Condition: " + str(goal_state))
    
    if location_input == 'A':
        # Vacuum placed in Location A
        print("Vacuum is placed in Location A")
        
        if status_input == '1':
            print("Location A is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")
            
            if status_input_complement == '1':
                # if B is Dirty
                print("Location B is Dirty.")
                print("Moving right to the Location B.")
                cost += 1  # cost for moving right
                print("Cost for moving RIGHT: " + str(cost))
                
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("No action. Cost: " + str(cost))
                print("Location B is already clean.")
        
        elif status_input == '0':
            print("Location A is already clean.")
            
            if status_input_complement == '1':
                # if B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B.")
                cost += 1  # cost for moving right
                print("Cost for moving RIGHT: " + str(cost))
                
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("No action. Cost: " + str(cost))
                print("Location B is already clean.")
    
    else:  # Vacuum placed in Location B
        print("Vacuum is placed in Location B")
        
        if status_input == '1':
            print("Location B is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")
            
            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A.")
                cost += 1  # cost for moving left
                print("Cost for moving LEFT: " + str(cost))
                
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("No action. Cost: " + str(cost))
                print("Location A is already clean.")
        
        elif status_input == '0':
            print("Location B is already clean.")
            
            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A.")
                cost += 1  # cost for moving left
                print("Cost for moving LEFT: " + str(cost))
                
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("No action. Cost: " + str(cost))
                print("Location A is already clean.")
    
    # done cleaning
    print("GOAL STATE:")
    print(goal_state)
    print("Performance Measurement: " + str(cost))
vacuum_world()
