#shared_functions.py
import os
import pygame
import config


def spawn_ball(xball, yball):
    """Draw ball"""
    return xball, yball

def move_ball(xball,yball):
    xball += config.ball_speed_x
    yball += config.ball_speed_x
    if xball + config.ball_radius > config.WIDTH or xball - config.ball_radius < 0:
        config.ball_speed_x *= -1  # Reverse x-direction
    if yball + config.ball_radius > config.HEIGHT or yball - config.ball_radius < 0:
         config.ball_speed_y *= -1  # Reverse y-direction
    return xball, yball

