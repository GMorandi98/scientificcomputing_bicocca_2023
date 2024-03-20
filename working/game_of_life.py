import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


### routine to update the state according to the rules ###
def update_state(frames, img, state, N):
    ### counting the living neighbors using np.roll
    live = (np.roll(state,  1, axis=0) +                        # center-north
            np.roll(state, -1, axis=0) +                        # center-south
            np.roll(state,  1, axis=1) +                        # center-east   
            np.roll(state, -1, axis=1) +                        # center-west
            np.roll(np.roll(state,  1, axis=0), 1, axis=1) +    # north-east
            np.roll(np.roll(state,  1, axis=0), -1, axis=1) +   # north-west
            np.roll(np.roll(state, -1, axis=0), 1, axis=1) +    # south-east
            np.roll(np.roll(state, -1, axis=0), -1, axis=1))    # south-west
    
    ### apply the rules
    new_state = np.where((state == 1) & ((live < 2) | (live > 3)), 0, state)    # dead by underpopulation and overpopulation
    new_state = np.where((state == 0) & (live == 3), 1, new_state)              # new live by reproduction 
    
    # update data for the image plot
    img.set_data(new_state)
    # update the state for the next iteration
    state[:] = new_state[:]
    return img
###########################################################


### Intializing grid and starting cnfg ###
N = 40
n_step = 50
state = np.zeros((N, N), dtype=int)
##########################################

# ### Random initial state 
# state = np.random.randint(0, 2, size=(N,N))

### Personalized initial state ###
state[1, 1:3] = [1, 1]
state[2, 1:3] = [1, 1]
state[1, 15:17] = [1, 1]
state[2, 15:17] = [1, 1]  # these are 2x2 block that live forever

state[5, 10] = 1
state[6, 10] = 1
state[7, 10] = 1
state[7, 22] = 1
state[8, 22] = 1
state[9, 22] = 1
state[13, 10:13] = [1, 1, 1]
state[14,  9:12] = [1, 1, 1]  # these are different types of oscillators

state[7, 19]    = 1
state[8, 20:22] = [1, 1]
state[9, 19:21] = [1, 1]
##################################


### animation settings ###
fig, ax = plt.subplots()
color_map = mpl.colors.ListedColormap(["white", "black"])
ims = ax.imshow(state, interpolation='nearest', cmap=color_map)
ax.set_yticks(np.arange(-0.5, N-1, 1))
ax.set_xticks(np.arange(-0.5, N-1, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(color='grey', linestyle='-', linewidth=1)

ani = animation.FuncAnimation(fig        = fig, 
                              func       = update_state, 
                              fargs      = (ims, state, N,),
                              frames     = n_step, 
                              save_count = 50,
                              interval   = 800,
                              )
plt.show()
##########################
