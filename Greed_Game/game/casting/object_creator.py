from game.casting.artifact import Artifact
from game.shared.point import Point
import random




class Gem_droper(Artifact):
    def __init__(self):
        super().__init__()
        self.frame_counter = 0
        self._gems = []

        def get_gems(self):
            """
            return the count gems
            
            """
            return self._gems


        def gem_drop(self):
            """
            This will compute the frame of the objects
            will be added to a list if actor and object position is the same 
            """
            self.frame_counter = self.frame_counter + 1
            if self.frame_counter >= 120:
                self.frame_counter = 0 
                new_artifact = Artifact()
                new_artifact.position = (random.randint(0,1024), 768)
                self._gems.apend(new_artifact)
            else:
                pass

            for artifact in list(self.artifacts):
                """
                Will remove objects founded 
                """
                artifact.position = (artifact.position.x, artifact.position.y -2)
                if artifact.position.y < -100:
                    self.artifacts.remove(artifact)
                elif artifact.bbox.intersects(self.player.bbox):
                    self.artifacts.remove(artifact)
