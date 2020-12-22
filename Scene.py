
class Scene:
    def __init__(self, animation, seconds, shouldNotify=False):
        
        #Animation object should always have an update function within it
        self.animation = animation
        self.seconds = seconds
        self.shouldNotify = shouldNotify

    def update(self):
        self.animation.update()

    def animationStarted(self):
        if (self.shouldNotify == True):
            self.animation.reset()
