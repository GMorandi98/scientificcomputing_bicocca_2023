import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L, T = 50, 70
n_step = 50
states = np.zeros((n_step, L, T), dtype=int)
#states = np.zeros((L, T), dtype=int)

### Random initial state ###
#states[0, :, :] = np.random.randint(0, 2, size=(L,T))

### Personalized initial state ###
states[0, 1, 1:3] = [1, 1]
states[0, 2, 1:3] = [1, 1]
states[0, 1, 15:17] = [1, 1]
states[0, 2, 15:17] = [1, 1]  # these are 2x2 block that live forever

states[0, 5, 10] = 1
states[0, 6, 10] = 1
states[0, 7, 10] = 1
states[0, 7, 22] = 1
states[0, 8, 22] = 1
states[0, 9, 22] = 1
states[0, 13, 10:13] = [1, 1, 1]
states[0, 14,  9:12] = [1, 1, 1]  # these are different types of oscillators

states[0, 7, 19]    = 1
states[0, 8, 20:22] = [1, 1]
states[0, 9, 19:21] = [1, 1]
##################################

# ### Personalized initial state ###
# states[1, 1:3] = [1, 1]
# states[2, 1:3] = [1, 1]
# states[1, 15:17] = [1, 1]
# states[2, 15:17] = [1, 1]  # these are 2x2 block that live forever

# states[5, 10] = 1
# states[6, 10] = 1
# states[7, 10] = 1
# states[7, 22] = 1
# states[8, 22] = 1
# states[9, 22] = 1
# states[13, 10:13] = [1, 1, 1]
# states[14,  9:12] = [1, 1, 1]  # these are different types of oscillators

# states[7, 19]    = 1
# states[8, 20:22] = [1, 1]
# states[9, 19:21] = [1, 1]
# ##################################


# def state_evolution(old_state): # old_state is np.array((L, T))
#     new_state = old_state.copy()
#     for x in range(L):
#         for t in range(T):
#             # count living cells in the 8 neighbours
#             live = old_state[  (x+1)%L, (t+1)%T]   +  old_state[(x-1+L)%L, (t-1+T)%T] + \
#                    old_state[  (x+1)%L,       t]   +  old_state[        x, (t+1)%T]   + \
#                    old_state[(x-1+L)%L,       t]   +  old_state[        x, (t-1+T)%T] + \
#                    old_state[(x-1+L)%L, (t+1)%T]   +  old_state[  (x+1)%L, (t-1+T)%T]
#             if old_state[x, t] == 0:        # dead cell in current site (x,t)
#                 if live == 3:               # dead --> live, by reproduction
#                     new_state[x, t] = 1
#             else:                           # living cell in current site (x,t)
#                 if live == 2 or live == 3:  # the cell survives
#                     new_state[x, t] = 1
#     return new_state

for s in range(n_step-1):
    for x in range(L):
        for t in range(T):
            # count living cells in the 8 neighbours
            live = states[s,   (x+1)%L, (t+1)%T]   +  states[s, (x-1+L)%L, (t-1+T)%T] + \
                   states[s,   (x+1)%L,       t]   +  states[s,         x, (t+1)%T]   + \
                   states[s, (x-1+L)%L,       t]   +  states[s,         x, (t-1+T)%T] + \
                   states[s, (x-1+L)%L, (t+1)%T]   +  states[s,   (x+1)%L, (t-1+T)%T]
            if states[s, x, t] == 0:        # dead cell in current site (x,t)
                if live == 3:               # dead --> live, by reproduction
                    states[s+1, x, t] = 1
            else:                           # living cell in current site (x,t)
                if live == 2 or live == 3:  # the cell survives
                    states[s+1, x, t] = 1


fig, ax = plt.subplots()
color_map = mpl.colors.ListedColormap(["white", "black"])
ims = ax.imshow(states[0,:,:], interpolation='nearest', cmap=color_map)
ax.set_yticks(np.arange(-0.5, L-1, 1))
ax.set_xticks(np.arange(-0.5, T-1, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(color='grey', linestyle='-', linewidth=1)

def update(frame):
    ims.set_data(states[frame, :, :])
    ax.set_title(f"State {frame+1}", fontsize=14)
    return ims

ani = animation.FuncAnimation(fig=fig, func=update, frames=n_step, interval=800)
plt.show()
