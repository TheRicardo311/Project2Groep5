###1/8
                if self.hehe == 2:
                    self.FireFurgoY = self.Player1.Furgo.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireFurgoX = self.Player1.Furgo.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x = self.FireFurgoX
                if self.boat == "DrieGroen" and keys[pygame.K_a] and self.hehe == 2:
                    self.hehe = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "DrieGroen" and keys[pygame.K_d] and self.hehe == 2:
                    self.hehe = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                    (self.x_x, self.FireFurgoY, 50, (55 * self.Player1.Furgo.length)), 0)

                    self.exdee += 1
                    self.x_x -= 1
                    if self.Player1.Furgo.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2 or self.Player1.Furgo.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Furgo.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row + 2 or self.Player1.Furgo.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Intensity.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column - 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row + 2 or self.Player1.Furgo.pos_column - 1 == self.Player2.Silver.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Silver.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row + 2 or self.Player1.Furgo.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Merapi.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    if self.exdee == (self.Player1.Furgo.atk_range * 55):
                        self.hehe = 3
                if self.hehe == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x, self.FireFurgoY, 50, (55 * self.Player1.Furgo.length)), 0)
                    self.exdee += 1
                    self.x_x += 1
                    if self.Player1.Furgo.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2 or self.Player1.Furgo.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Furgo.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row + 2 or self.Player1.Furgo.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Intensity.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column + 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row + 2 or self.Player1.Furgo.pos_column + 1 == self.Player2.Silver.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Silver.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    elif self.Player1.Furgo.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row + 2 or self.Player1.Furgo.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row + 2:
                        self.Player2.Merapi.hp -= 1
                        self.hehe = 3
                        self.x_y = 0
                    if self.exdee == (self.Player1.Furgo.atk_range * 55):
                        self.hehe = 3

                ###2/8
                if self.hehe2 == 2:
                    self.FireIntensityY = self.Player1.Intensity.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireIntensityX = self.Player1.Intensity.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x1 = self.FireIntensityX
                if self.boat == "Vier1Groen" and keys[pygame.K_a] and self.hehe2 == 2:
                    self.hehe2 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "Vier1Groen" and keys[pygame.K_d] and self.hehe2 == 2:
                    self.hehe2 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe2 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x1, self.FireIntensityY, 50, (55 * self.Player1.Intensity.length)), 0)

                    self.exdee2 += 1
                    self.x_x1 -= 1
                    if self.Player1.Intensity.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row + 3 or self.Player1.Intensity.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Furgo.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Intensity.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Intensity.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column - 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Intensity.pos_column - 1 == self.Player2.Silver.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row + 3 or self.Player1.Intensity.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Merapi.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    if self.exdee2 == (self.Player1.Intensity.atk_range * 55):
                        self.hehe2 = 3
                if self.hehe2 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x1, self.FireIntensityY, 50, (55 * self.Player1.Intensity.length)), 0)
                    self.exdee2 += 1
                    self.x_x1 += 1
                    if self.Player1.Intensity.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row + 3 or self.Player1.Intensity.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Furgo.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Intensity.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Intensity.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column + 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Intensity.pos_column + 1 == self.Player2.Silver.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    elif self.Player1.Intensity.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row + 3 or self.Player1.Intensity.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row + 3:
                        self.Player2.Merapi.hp -= 1
                        self.hehe2 = 3
                        self.x_y2 = 0
                    if self.exdee2 == (self.Player1.Intensity.atk_range * 55):
                        self.hehe2 = 3

                ###3/8
                if self.hehe3 == 2:
                    self.FireSilverY = self.Player1.Silver.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireSilverX = self.Player1.Silver.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x2 = self.FireSilverX
                if self.boat == "Vier2Groen" and keys[pygame.K_a] and self.hehe3 == 2:
                    self.hehe3 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "Vier2Groen" and keys[pygame.K_d] and self.hehe3 == 2:
                    self.hehe3 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe3 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x2, self.FireSilverY, 50, (55 * self.Player1.Silver.length)), 0)

                    self.exdee3 += 1
                    self.x_x2 -= 1
                    if self.Player1.Silver.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row + 3 or self.Player1.Silver.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Furgo.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Silver.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Intensity -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column - 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Silver.pos_column - 1 == self.Player2.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row + 3 or self.Player1.Silver.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Merapi.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    if self.exdee3 == (self.Player1.Silver.atk_range * 55):
                        self.hehe3 = 3
                if self.hehe3 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x2, self.FireSilverY, 50, (55 * self.Player1.Silver.length)), 0)
                    self.exdee3 += 1
                    self.x_x2 += 1
                    if self.Player1.Silver.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row + 3 or self.Player1.Silver.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Furgo.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row + 3 or self.Player1.Silver.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Intensity -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column + 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 3 or self.Player1.Silver.pos_column + 1 == self.Player2.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Silver.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    elif self.Player1.Silver.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row + 3 or self.Player1.Silver.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row + 3:
                        self.Player2.Merapi.hp -= 1
                        self.hehe3 = 3
                        self.x_y3 = 0
                    if self.exdee3 == (self.Player1.Silver.atk_range * 55):
                        self.hehe3 = 3
            else:
                ###4/8
                if self.hehe4 == 2:
                    self.FireMerapiY = self.Player1.Merapi.pos_row * (self.HEIGHT + self.MARGIN) + 5
                    self.FireMerapiX = self.Player1.Merapi.pos_column * (self.WIDTH + self.MARGIN) + 200
                    self.x_x3 = self.FireMerapiX
                if self.boat == "VijfGroen" and keys[pygame.K_a] and self.hehe4 == 2:
                    self.hehe4 = 1
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.boat == "VijfGroen" and keys[pygame.K_d] and self.hehe4 == 2:
                    self.hehe4 = 4
                    self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                    self.row = pos[1] // (self.HEIGHT + self.MARGIN)
                if self.hehe4 == 1:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x3, self.FireMerapiY, 50, (55 * self.Player1.Merapi.length)), 0)

                    self.exdee4 += 1
                    self.x_x3 -= 1
                    if self.Player1.Merapi.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row + 4 or self.Player1.Merapi.pos_column - 1 == self.Player2.Furgo.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Furgo.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row + 4 or self.Player1.Merapi.pos_column - 1 == self.Player2.Intensity.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Intensity.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column - 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row + 4 or self.Player1.Merapi.pos_column - 1 == self.Player2.Silver.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Silver.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4 or self.Player1.Merapi.pos_column - 1 == self.Player2.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Merapi.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    if self.exdee4 == (self.Player1.Merapi.atk_range * 55):
                        self.hehe4 = 3
                if self.hehe4 == 4:

                    pygame.draw.rect(self.screen, self.RED,
                                     (self.x_x3, self.FireMerapiY, 50, (55 * self.Player1.Merapi.length)), 0)
                    self.exdee4 += 1
                    self.x_x3 += 1
                    if self.Player1.Merapi.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row + 4 or self.Player1.Merapi.pos_column + 1 == self.Player2.Furgo.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Furgo.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row + 4 or self.Player1.Merapi.pos_column + 1 == self.Player2.Intensity.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Intensity.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column + 1 == self.Player2.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row + 4 or self.Player1.Merapi.pos_column + 1 == self.Player2.Silver.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Silver.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    elif self.Player1.Merapi.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4 or self.Player1.Merapi.pos_column + 1 == self.Player2.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4:
                        self.Player2.Merapi.hp -= 1
                        self.hehe4 = 3
                        self.x_y4 = 0
                    if self.exdee4 == (self.Player1.Merapi.atk_range * 55):
                        self.hehe4 = 3

            ###5/8
            if self.hehe5 == 2:
                self.FireFurgoYGeel = self.Player2.Furgo.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireFurgoX = self.Player2.Furgo.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x4 = self.FireFurgoX
            if self.boat == "DrieGeel" and keys[pygame.K_a] and self.hehe5 == 2:
                self.hehe5 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "DrieGeel" and keys[pygame.K_d] and self.hehe5 == 2:
                self.hehe5 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe5 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x4, self.FireFurgoYGeel, 50, (55 * self.Player2.Furgo.length)), 0)

                self.exdee5 += 1
                self.x_x4 -= 1
                if self.Player2.Furgo.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2 or self.Player2.Furgo.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Furgo.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row + 2 or self.Player2.Furgo.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Intensity.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column - 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row + 2 or self.Player2.Furgo.pos_column - 1 == self.Player1.Silver.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Silver.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row + 2 or self.Player2.Furgo.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Merapi.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                if self.exdee5 == (self.Player2.Furgo.atk_range * 55):
                    self.hehe5 = 3
            if self.hehe5 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x4, self.FireFurgoYGeel, 50, (55 * self.Player2.Furgo.length)), 0)
                self.exdee5 += 1
                self.x_x4 += 1
                if self.Player2.Furgo.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row + 2 or self.Player2.Furgo.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Furgo.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row + 2 or self.Player2.Furgo.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Intensity.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column + 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row + 2 or self.Player2.Furgo.pos_column + 1 == self.Player1.Silver.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Silver.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                elif self.Player2.Furgo.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row + 2 or self.Player2.Furgo.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player2.Furgo.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Furgo.pos_row + 2:
                    self.Player1.Merapi.hp -= 1
                    self.hehe5 = 3
                    self.x_y5 = 0
                if self.exdee5 == (self.Player2.Furgo.atk_range * 55):
                    self.hehe5 = 3

            ###6/8
            if self.hehe6 == 2:
                self.FireIntensityYGeel = self.Player2.Intensity.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireIntensityX = self.Player2.Intensity.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x5 = self.FireIntensityX
            if self.boat == "Vier1Geel" and keys[pygame.K_a] and self.hehe6 == 2:
                self.hehe6 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "Vier1Geel" and keys[pygame.K_d] and self.hehe6 == 2:
                self.hehe6 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe6 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x5, self.FireIntensityYGeel, 50, (55 * self.Player2.Intensity.length)), 0)

                self.exdee6 += 1
                self.x_x5 -= 1
                if self.Player2.Intensity.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row + 3 or self.Player2.Intensity.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Furgo.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Intensity.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Intensity.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column - 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Intensity.pos_column - 1 == self.Player1.Silver.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Silver.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row + 3 or self.Player2.Intensity.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Merapi.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                if self.exdee6 == (self.Player2.Intensity.atk_range * 55):
                    self.hehe6 = 3
            if self.hehe6 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x5, self.FireIntensityYGeel, 50, (55 * self.Player1.Intensity.length)), 0)
                self.exdee6 += 1
                self.x_x5 += 1
                if self.Player2.Intensity.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row + 3 or self.Player2.Intensity.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Furgo.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Intensity.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Intensity.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column + 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Intensity.pos_column + 1 == self.Player1.Silver.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Silver.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                elif self.Player2.Intensity.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row + 3 or self.Player2.Intensity.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player2.Intensity.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Intensity.pos_row + 3:
                    self.Player1.Merapi.hp -= 1
                    self.hehe6 = 3
                    self.x_y6 = 0
                if self.exdee6 == (self.Player1.Intensity.atk_range * 55):
                    self.hehe6 = 3

            ###7/8
            if self.hehe7 == 2:
                self.FireSilverYGeel = self.Player2.Silver.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireSilverX = self.Player2.Silver.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x6 = self.FireSilverX
            if self.boat == "Vier2Geel" and keys[pygame.K_a] and self.hehe7 == 2:
                self.hehe7 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "Vier2Geel" and keys[pygame.K_d] and self.hehe7 == 2:
                self.hehe7 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe7 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x6, self.FireSilverYGeel, 50, (55 * self.Player2.Silver.length)), 0)

                self.exdee7 += 1
                self.x_x6 -= 1
                if self.Player2.Silver.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row + 3 or self.Player2.Silver.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Furgo.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Silver.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Intensity.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column - 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Silver.pos_column - 1 == self.Player1.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Silver.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row + 3 or self.Player2.Silver.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Merapi.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                if self.exdee7 == (self.Player2.Silver.atk_range * 55):
                    self.hehe7 = 3
            if self.hehe7 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x6, self.FireSilverYGeel, 50, (55 * self.Player2.Silver.length)), 0)
                self.exdee7 += 1
                self.x_x6 += 1
                if self.Player2.Silver.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row + 3 or self.Player2.Silver.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player2.Silver.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Furgo.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row + 3 or self.Player2.Silver.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player2.Silver.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Intensity.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column + 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row + 3 or self.Player2.Silver.pos_column + 1 == self.Player1.Silver.pos_column and self.Player2.Silver.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Silver.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                elif self.Player2.Silver.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row + 3 or self.Player2.Silver.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player2.Silver.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Silver.pos_row + 2:
                    self.Player2.Merapi.hp -= 1
                    self.hehe7 = 3
                    self.x_y7 = 0
                if self.exdee7 == (self.Player2.Silver.atk_range * 55):
                    self.hehe7 = 3

            ###8/8
            if self.hehe8 == 2:
                self.FireMerapiYGeel = self.Player2.Merapi.pos_row * (self.HEIGHT + self.MARGIN) + 5
                self.FireMerapiX = self.Player2.Merapi.pos_column * (self.WIDTH + self.MARGIN) + 200
                self.x_x7 = self.FireMerapiX
            if self.boat == "VijfGeel" and keys[pygame.K_a] and self.hehe8 == 2:
                self.hehe8 = 1
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.boat == "VijfGeel" and keys[pygame.K_d] and self.hehe8 == 2:
                self.hehe8 = 4
                self.column = (pos[0] - 200) // (self.WIDTH + self.MARGIN)
                self.row = pos[1] // (self.HEIGHT + self.MARGIN)
            if self.hehe8 == 1:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x7, self.FireMerapiYGeel, 50, (55 * self.Player2.Merapi.length)), 0)

                self.exdee8 += 1
                self.x_x7 -= 1
                if self.Player2.Merapi.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row + 4 or self.Player2.Merapi.pos_column - 1 == self.Player1.Furgo.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Furgo.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row + 4 or self.Player2.Merapi.pos_column - 1 == self.Player1.Intensity.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Intensity.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column - 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row + 4 or self.Player2.Merapi.pos_column - 1 == self.Player1.Silver.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Silver.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4 or self.Player2.Merapi.pos_column - 1 == self.Player1.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Merapi.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                if self.exdee8 == (self.Player2.Merapi.atk_range * 55):
                    self.hehe8 = 3
            if self.hehe8 == 4:

                pygame.draw.rect(self.screen, self.RED,
                                 (self.x_x7, self.FireMerapiYGeel, 50, (55 * self.Player2.Merapi.length)), 0)
                self.exdee8 += 1
                self.x_x7 += 1
                if self.Player2.Merapi.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row + 4 or self.Player2.Merapi.pos_column + 1 == self.Player1.Furgo.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Furgo.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Furgo.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row + 4 or self.Player2.Merapi.pos_column + 1 == self.Player1.Intensity.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Intensity.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Intensity.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column + 1 == self.Player1.Silver.pos_column and self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row + 4 or self.Player2.Merapi.pos_column + 1 == self.Player1.Silver.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Silver.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Silver.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                elif self.Player2.Merapi.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row + 4 or self.Player2.Merapi.pos_column + 1 == self.Player1.Merapi.pos_column and self.Player2.Merapi.pos_row <= self.Player1.Merapi.pos_row <= self.Player2.Merapi.pos_row + 4:
                    self.Player1.Merapi.hp -= 1
                    self.hehe8 = 3
                    self.x_y8 = 0
                if self.exdee8 == (self.Player2.Merapi.atk_range * 55):
                    self.hehe8 = 3