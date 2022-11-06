from game.casting.actor import Actor
import random
speed = 5

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.

        get_identity (string): You can score from the O actor

        frame_counter (value): Counter reset to reset to zero
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._identity = ""
        self.frame_counter = 0
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def set_identity(self, x):
        """Recognize the object on the game.
    
        Args:
            recognize(value): Pull apart values
        """
        self._identity = x

    def get_identity(self): 
        """Recognize the object on the game

            Returns:
                string: selected number foSr identification
        """
        return self._identity
    
    def drop(self):
        self._position._y += speed
        """Moves the object and position

        Args: 
            Speed (value): position and speed
        """

        

    def reset(self):
        """
        Will apear the objects during the game on the screen 
        random.randint will appear gems as the same manner for rocks
        """
        y = random.randint(1, 7 - 1)
        ypos = y * 30
        self._position._y = int(0 - ypos)
        x = random.randint(1, 60 - 1)
        pos = x
        pos = x * 30
        self._position._x = pos