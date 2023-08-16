class Chandrayan:
    x_coordinate = 0
    y_coordinate = 0
    z_coordinate = 0
    last_facing = ''
    facing = 'Up'

    def print(self):
        print(f"x:{self.x_coordinate} y:{self.y_coordinate} z: {self.z_coordinate} FACING = {self.facing} lastfacing = {self.last_facing}")

    def movement(self, x, y, z, facing, commands):
        self.x_coordinate = x
        self.y_coordinate = y
        self.z_coordinate = z
        self.facing = facing
        for command in commands:
            if self.facing == 'N':
                if command == 'f':
                    self.y_coordinate += 1
                elif command == 'b':
                    self.y_coordinate -= 1
                elif command == 'l':
                    self.facing = 'W'

                elif command == 'r':
                    self.facing = 'E'

                elif command == 'u':
                    self.facing = 'U'
                    self.last_facing = 'N'

                elif command == 'd':
                    self.facing = 'D'
                    self.last_facing = 'N'

            elif self.facing == 'S':
                if command == 'f':
                    self.y_coordinate -= 1
                elif command == 'b':
                    self.y_coordinate += 1
                elif command == 'l':
                    self.facing = 'E'

                elif command == 'r':
                    self.facing = 'W'

                elif command == 'u':
                    self.facing = 'U'
                    self.last_facing = 'S'

                elif command == 'd':
                    self.facing = 'D'
                    self.last_facing = 'S'

            elif self.facing == 'W':
                if command == 'f':
                    self.x_coordinate -= 1
                elif command == 'b':
                    self.x_coordinate += 1
                elif command == 'l':
                    self.facing = 'S'

                elif command == 'r':
                    self.facing = 'N'

                elif command == 'u':
                    self.facing = 'U'
                    self.last_facing = 'W'

                elif command == 'd':
                    self.facing = 'D'
                    self.last_facing = 'W'

            elif self.facing == 'E':
                if command == 'f':
                    self.x_coordinate += 1
                elif command == 'b':
                    self.x_coordinate -= 1
                elif command == 'l':
                    self.facing = 'N'

                elif command == 'r':
                    self.facing = 'S'

                elif command == 'u':
                    self.facing = 'U'
                    self.last_facing = 'E'

                elif command == 'd':
                    self.facing = 'D'
                    self.last_facing = 'E'

            elif self.facing == 'U':
                if command == 'f':
                    self.z_coordinate += 1
                elif command == 'b':
                    self.z_coordinate -= 1
                elif command == 'l':
                    if self.last_facing == 'N':
                        self.facing = 'W'

                    elif self.last_facing == 'S':
                        self.facing = 'E'

                    elif self.last_facing == 'E':
                        self.facing = 'N'

                    elif self.last_facing == 'W':
                        self.facing = 'S'

                elif command == 'r':
                    if self.last_facing == 'S':
                        self.facing = 'W'

                    elif self.last_facing == 'N':
                        self.facing = 'E'

                    elif self.last_facing == 'W':
                        self.facing = 'N'

                    elif self.last_facing == 'E':
                        self.facing = 'S'

                elif command == 'u':
                    self.facing = 'U'

                elif command == 'd':
                    self.facing = 'D'
            elif facing == 'D':
                if command == 'f':
                    self.z_coordinate -= 1
                elif command == 'b':
                    self.z_coordinate += 1
                elif command == 'l':
                    if self.last_facing == 'N':
                        self.facing = 'W'

                    elif self.last_facing == 'S':
                        self.facing = 'E'

                    elif self.last_facing == 'E':
                        self.facing = 'N'

                    elif self.last_facing == 'W':
                        self.facing = 'S'


                elif command == 'r':
                    if self.last_facing == 'S':
                        self.facing = 'W'

                    elif self.last_facing == 'N':
                        self.facing = 'E'

                    elif self.last_facing == 'W':
                        self.facing = 'N'

                    elif self.last_facing == 'E':
                        self.facing = 'S'

                elif command == 'u':
                    self.facing = 'U'

                elif command == 'd':

                    self.facing = 'D'
            self.print()



obj = Chandrayan()
obj.print()
command = ['f', 'r', 'u', 'b', 'l']
obj.movement(0, 0, 0, 'N', command)

