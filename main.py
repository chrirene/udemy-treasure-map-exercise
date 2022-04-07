# A program for Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜","⬜"]
map = [row1, row2, row3]
        
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) 
vertical = int(position[1]) 

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"



# position_as_int = int(position)

# if position_as_int == 11:
#   row1[0] = "X" 
# if position_as_int == 21:
#   row1[1] = "X" 
# if position_as_int == 31:
#   row1[2] = "X" 

# if position_as_int == 12:
#   row2[0] = "X"  
# if position_as_int == 22:
#   row2[1] = "X" 
# if position_as_int == 32:
#   row2[2] = "X" 

# if position_as_int == 13:
#   row3[0] = "X" 
# if position_as_int == 23:
#   row3[1] = "X" 
# if position_as_int == 33:
#   row3[2] = "X" 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")