from numpy import zeros, array
from matplotlib.pyplot import subplots, imshow, show
from matplotlib.animation import FuncAnimation, ImageMagickFileWriter


class GridAnimation:
    def __init__(self, shape : tuple, n_frames : int):
        self.shape = shape
        self.n_frames = n_frames
        self.frames = zeros((n_frames, *shape))
        self.current_frame_index = 0
        self.fig = None
        self.ax = None
        self.im = None
        
        self.init_animation()

    def add_frame(self, frame : array):
        self.__set_current_frame(self.current_frame_index + 1)
        self.frames[self.current_frame_index,:,:] = frame

    def __set_current_frame(self, new_frame_index : int):
        if new_frame_index >= self.n_frames:
            raise ValueError("n_frames is not enough")
        else:
            self.current_frame = new_frame_index

    def __update(self, *args):
        self.im.set_array(self.frames[self.current_frame_index])
        self.__set_current_frame(self.current_frame_index + 1)
        return self.im

    def init_animation(self, origin='lower'):
        self.fig, self.ax = subplots(figsize=self.shape)
        self.__set_current_frame(0)
        self.im = imshow(self.frames[self.current_frame_index], origin=origin)

    def show(self, interval=500):
        self.ani = FuncAnimation(self.fig, self.__update, interval=interval)
        show()

    def save(self, filename="GridAnimation.gif", fps=2):
        ani = FuncAnimation(self.fig, self.__update, self.n_frames)
        writer = ImageMagickFileWriter(fps=fps)
        ani.save(filename, writer=writer) 


import numpy as np
anim = GridAnimation(shape=(10,10), n_frames=100)
for _ in range(100):
    anim.add_frame(frame = np.random.rand(10,10))

anim 