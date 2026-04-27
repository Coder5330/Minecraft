from settings import *

class Mob:
    def __init__(self, app, position, health=20):
        self.app = app
        self.position = glm.vec3(position)
        self.health = health
        self.alive = True
        self.velocity_y = 0.0
        self.yaw = 0.0

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.alive = False

    def check_collision(self, pos):
        vh = self.app.scene.world.voxel_handler
        radius = 0.3
        for dx in (-radius, radius):
            for dz in (-radius, radius):
                for y_offset in (0.0, 0.5, 1.0):
                    result = vh.get_voxel_id(
                        glm.ivec3(int(pos.x + dx), int(pos.y + y_offset), int(pos.z + dz))
                    )
                    if result[0] and int(result[0]) != WATER_BLOCK:
                        return True
        return False

    def move(self, dx, dz):
        new_pos = glm.vec3(self.position.x + dx, self.position.y, self.position.z + dz)
        if not self.check_collision(new_pos):
            self.position.x += dx
            self.position.z += dz
            return
        new_pos_x = glm.vec3(self.position.x + dx, self.position.y, self.position.z)
        if not self.check_collision(new_pos_x):
            self.position.x += dx
            return
        new_pos_z = glm.vec3(self.position.x, self.position.y, self.position.z + dz)
        if not self.check_collision(new_pos_z):
            self.position.z += dz

    def apply_gravity(self):
        self.velocity_y += GRAVITY * self.app.delta_time
        self.velocity_y = max(self.velocity_y, -0.5)
        self.position.y += self.velocity_y
        ground_height = self.get_ground_height()
        if self.velocity_y <= 0 and self.position.y <= ground_height:
            self.position.y = ground_height
            self.velocity_y = 0

    def get_ground_height(self):
        x, z = int(self.position.x), int(self.position.z)
        for y in range(int(self.position.y), -1, -1):
            result = self.app.scene.world.voxel_handler.get_voxel_id(glm.ivec3(x, y, z))
            if result[0] and int(result[0]) != WATER_BLOCK:
                return y + 1
        return 0

    def apply_water_current(self):
        flow = self.app.scene.world.voxel_handler.get_water_current(
            self.position + glm.vec3(0.0, 0.4, 0.0), MOB_WATER_PUSH
        )
        self.move(flow.x, flow.z)

    def update(self):
        self.apply_water_current()
        self.apply_gravity()
