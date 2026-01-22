import matplotlib.pyplot as plt

# choose the method
print('Use the Improved Euler method?')
Improved_Euler_method = input('Otherwise, the standard Euler method is used. (Yes/No): ').strip().lower() == 'yes'
print('Only one type of air resistance can be considered at a time: linear or quadratic.')
More = input('Learn more about air resistance? (Yes/No): ').strip().lower() == 'yes'


if More is True:
    print('Linear air resistance is applied to small-sized objects moving through a viscous medium '
          '(most commonly droplets of viscous liquids) at low velocities over short distances.')
    print('In the program, the velocity limit for linear air resistance is set to 30 m/s '
          '(this value can be modified)')
    print('Large values of mass, velocity and height may lead to unrealistic results.')
    print('Quadratic air resistance is used for larger values of velocity and other parameters; '
          'no velocity limit is imposed in this case.')
    print('In the absence of air resistance, mass does not affect the falling velocity, '
          'so it cannot be chosen')

# choose the res
Air_res_1 = input('Consider linear air resistance? (Yes/No): ').strip().lower() == 'yes'
Air_res_2 = input('Consider quadratic air resistance? (Yes/No): ').strip().lower() == 'yes'
Show_all_timesx = input('Show the list of coordinates for each simulation step? '
                        '(It is a very long list) (Yes/No): ').strip().lower() == 'yes'
Show_all_timesx_round = input('Show list of coordinates for each simulation step with rounded values? '
                              '(It is a very long list) (Yes/No): ').strip().lower() == 'yes'
if Show_all_timesx_round is True or Show_all_timesx is True:
    print('The list will be shown after the initial search')

while Air_res_1 is True and Air_res_2 is True:
    print('You have chosen two types of air resistance to consider.')
    print('Only one type of air resistance can be considered at a time: linear or quadratic.')
    Air_res_1 = input('Consider linear air resistance? (Yes/No): ').strip().lower() == 'yes'
    Air_res_2 = input('Consider quadratic air resistance? (Yes/No): ').strip().lower() == 'yes'


# values
g = 9.81
m = 0
x = float(input('Height (m): '))
v = 0
a = 0
v_max = 0
dt = 0.0005
k = 0
v_old = 0
times = 0

# they are here for matplotlib
all_v = []
all_x = []
all_times = []
all_x_round = []
all_times_round = []
all_a = []
all_a_round = []


# mass
if Air_res_1 is True or Air_res_2 is True:
    m = float(input('Mass (kg): '))

if Air_res_1 is True:
    print('The velocity limit is 30 m/s by default.')
    print('Large values of mass, velocity and height may lead to unrealistic results.')

    v_max = 30
    change_v_max = input('Use a custom velocity limit? (Yes/No): ').strip().lower() == 'yes'

    if change_v_max is True:
        max_v = float(input('Custom velocity limit (m/s): '))

    # the drag c. when it's Air_res_1
    k = m * g / v_max

if Air_res_2 is True:
    print('Examples of drag coefficients:')
    print('Highly streamlined object 0.02 – 0.05')
    print('Sphere / compact object 0.05 – 0.1')
    print('Human (feet-first position) 0.15 – 0.3')
    print('Human (spread-eagle position) 0.3 – 0.6')
    print('Deployed parachute 0.8 – 1.5')
    k = float(input('Drag coefficient: '))

if Air_res_1 is False and Air_res_2 is False:
    print('In the absence of air resistance, mass does not affect the falling velocity')

if Improved_Euler_method is True:
    while x >= 0:
        # they are here for matplotlib
        all_v.append(v)
        all_x.append(x)
        all_times.append(times)
        all_x_round.append(round(x, 2))
        all_times_round.append(round(times, 2))

        v_max = max(v_max, abs(v))

        if Air_res_1 is True:
            a = g - k * v / m

            # we should append "a" here to make it be the same step with the rest
            all_a.append(a)
            all_a_round.append(round(a, 2))

            x_sup = x - dt * v
            v_sup = v + dt * a
            a_sup = g - k * v_sup / m

            x = x - dt / 2 * (v + v_sup)
            v = v + dt / 2 * (a + a_sup)

            times += dt

        elif Air_res_2 is True:
            a = g - k * v * abs(v) / m

            all_a.append(a)
            all_a_round.append(round(a, 2))

            x_sup = x - dt * v
            v_sup = v + dt * a
            a_sup = g - k * v_sup * abs(v_sup) / m

            x = x - dt / 2 * (v + v_sup)
            v = v + dt / 2 * (a + a_sup)

            times += dt

        else:
            a = g
            a_sup = g

            all_a.append(a)
            all_a_round.append(round(a, 2))

            x_sup = x - dt * v
            v_sup = v + dt * a

            x = x - dt / 2 * (v + v_sup)
            v = v + dt / 2 * (a + a_sup)

            times += dt


    print('complete')

if Improved_Euler_method is False:
    while x >= 0:
        all_v.append(v)
        all_x.append(x)
        all_times.append(times)
        all_x_round.append(round(x, 2))
        all_times_round.append(round(times, 2))

        v_max = max(v_max, abs(v))

        if Air_res_1 is True:
            a = g - k * v / m

            all_a.append(a)
            all_a_round.append(round(a, 5))

            v = v + a * dt
            x = x - v * dt

            times += dt

        elif Air_res_2 is True:
            a = g - k * v * abs(v) / m

            all_a.append(a)
            all_a_round.append(round(a, 5))

            v = v + a * dt
            x = x - v * dt

            times += dt

        else:
            a = g

            all_a.append(a)
            all_a_round.append(round(a, 5))

            v = v + a * dt
            x = x - v * dt

            times += dt

    print('complete')


# some results
print(f'Total time: {round(times, 2)}s')
print('Terminal velocity (m/s):')
print(v_max)
print('Rounded terminal velocity (m/s):')
print(round(v_max, 2))

# they are here for the search ang for the lists
all_timesx = dict(zip(all_times, all_x))
all_timex_round = dict(zip(all_times_round, all_x_round))

# plots
if Air_res_1 is False and Air_res_2 is False:
    # we do not have "a" in this case so here are only 3 plots:
    fig, ax = plt.subplots(1, 3)
    fig.set_size_inches(15, 4)

    plt.subplots_adjust(wspace=0.4)

    ax[0].plot(all_times, all_v)
    ax[0].set_xlabel('Time (t), s')
    ax[0].set_ylabel('Velocity (v), m/s')

    ax[1].plot(all_times, all_x)
    ax[1].set_xlabel('Time (t), s')
    ax[1].set_ylabel('Height (x), m')

    ax[2].plot(all_v, all_x)
    ax[2].set_xlabel('Velocity (v), m/s')
    ax[2].set_ylabel('Height (x), m')

    plt.show()

elif Air_res_1 is True or Air_res_2 is True:
    fig, ax = plt.subplots(2, 3)
    fig.set_size_inches(13, 8)

    plt.subplots_adjust(wspace=0.4)
    plt.subplots_adjust(hspace=0.4)

    ax[0, 0].plot(all_times, all_v)
    ax[0, 0].set_xlabel('Time (t), s')
    ax[0, 0].set_ylabel('Velocity (v), m/s')

    ax[0, 1].plot(all_times, all_x)
    ax[0, 1].set_xlabel('Time (t), s')
    ax[0, 1].set_ylabel('Height (x), m')

    ax[0, 2].plot(all_v, all_x)
    ax[0, 2].set_xlabel('Velocity (v), m/s')
    ax[0, 2].set_ylabel('Height (x), m')

    ax[1, 0].plot(all_times, all_a)
    ax[1, 0].set_xlabel('Time (t), s')
    ax[1, 0].set_ylabel('Acceleration (a), m/s^2')

    ax[1, 1].plot(all_a, all_x)
    ax[1, 1].set_xlabel('Acceleration (a), m/s^2')
    ax[1, 1].set_ylabel('Height (x), m')

    ax[1, 2].plot(all_a, all_v)
    ax[1, 2].set_xlabel('Acceleration (a), m/s^2')
    ax[1, 2].set_ylabel('Velocity (v), m/s')

    plt.show()


# the search
print(all_timex_round[round(float(input
                                  (f'Find coordinates (enter time from 0 to {round(times, 2)} s): ')), 4)])


# the lists
if Show_all_timesx is True:
    print('list of coordinates for each simulation step (s and m):')
    print(all_timesx)
if Show_all_timesx_round is True:
    print('list of coordinates for each simulation step with rounded values (s and m):')
    print(all_timex_round)
