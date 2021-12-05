import re

TEST = '''
p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
'''

TEST2 = '''
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>    
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
'''


def particle_swarm1(particle_data):
    particles = {i: read_particles(line)
                 for i, line in enumerate(particle_data)}

    closest_particle = -1

    # Compare all particles to find one(s) with smallest acceleration

    smallest_acc = 100000
    acc_dict = dict()

    for part_id, pva in particles.items():
        if pva[2].manhatten_distance() <= smallest_acc:  # Compare acceleration
            smallest_acc = pva[2].manhatten_distance()
            acc_dict[part_id] = pva

    if len(acc_dict) == 0:
        print('Error in comparing accelerations!')
    elif len(acc_dict) == 1:
        for key in acc_dict.keys():
            closest_particle = key
    else:
        # If there are multiple particles that share the smallest acceleration then
        # compare those particles to find the one(s) with the smallest initial velocity

        smallest_vel = 10000
        vel_dict = dict()

        for part_id, pva in acc_dict.items():
            if pva[1].manhatten_distance() <= smallest_vel:
                smallest_vel = pva[1].manhatten_distance()
                vel_dict[part_id] = pva

        if len(vel_dict) == 0:
            print('Error in comparing velocities!')
        elif len(vel_dict) == 1:
            for key in vel_dict.keys():
                closest_particle = key
        else:
            print('Ones of these is probably the answer for part 1, pick one:')
            print(vel_dict.keys())
            return

    print('Closest:', closest_particle)


def particle_swarm2(particle_data):
    particles = {i: read_particles(line)
                 for i, line in enumerate(particle_data)}

    for _ in range(1000):
        for pva in particles.values():
            pva[1] += pva[2]  # update velocity
            pva[0] += pva[1]  # update position

        copy_particles = dict(particles)

        # Check each particles position against the rest of particles in the collection
        for p_id, pva in particles.items():
            for p_id_check, pva_check in particles.items():
                if p_id is not p_id_check:
                    if pva[0] == pva_check[0]:  # Check for collisions
                        if p_id_check in copy_particles:
                            # Remove particle from copy
                            del copy_particles[p_id_check]

        # Point old dict to updated copy.
        particles = copy_particles

    # The above works but it's slow. It would probably much faster if I can refactor
    # it to use sets.

    print(len(particles))


def read_particles(in_line):
    regex = r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>'

    match = re.match(regex, in_line)
    grps = match.groups()

    return [Vector(int(grps[0]), int(grps[1]), int(grps[2])),  # position
            Vector(int(grps[3]), int(grps[4]), int(grps[5])),  # velocity
            Vector(int(grps[6]), int(grps[7]), int(grps[8]))]  # acceleration


class Vector():
    '''Implements Vectors and associated functions'''

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    def manhatten_distance(self):
        '''Returns the Manhatten Distance of the vector.'''
        return abs(self.X) + abs(self.Y) + abs(self.Z)

    def __add__(self, other):
        return Vector(self.X + other.X, self.Y + other.Y, self.Z + other.Z)

    def __sub__(self, other):
        return Vector(self.X - other.X, self.Y - other.Y, self.Z - other.Z)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z

    def __str__(self):
        return '({},{},{})'.format(self.X, self.Y, self.Z)


def load_puzzle():
    return [line.strip('\n') for line in open('day20input.txt', 'r').readlines()]


if __name__ == '__main__':
    # particle_swarm1(TEST.strip('\n').split('\n'))
    # particle_swarm1(load_puzzle())

    # particle_swarm2(TEST2.strip('\n').split('\n'))
    particle_swarm2(load_puzzle())
