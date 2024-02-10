from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0


mycontroller.drive_forwards

while True :
 #forward state
    if state == 0:
        mycontroller.drive_forwards()
        if mycontroller.left_odom.get_count()>= 1234 and mycontroller.right_odom.get_count() >=1234 and turns_made < 3:
            state = 1
            #reset the odemetry count
            mycontroller.left_odom.reset_count
            mycontroller.right_odom.reset_count 
        elif mycontroller.left_odom.get_count ()<= 1234 and mycontroller.right_odom.get_count() <= 1224 and turns_made <= 3:
            state = 2
            mycontroller.left_odom.reset_count ()
            mycontroller.right_odom.reset_count()
        elif turns_made > 5:
            state = 3
    
#turning state
  
    elif state == 1:
        mycontroller.raft.led_on()
        mycontroller.left_turn() 
     
        turns_made += 1 

        state = 0
    #triangle
    elif state == 2:
         mycontroller.custom_right_turn(120)
         turns_made += 1
         state = 0
    #stopping state
    elif state == 3:
        mycontroller.stop ()

         




 

