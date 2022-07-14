from manim import *
class ParabolaScene(Scene):
    CONFIG={
        'config_axes':{
            'x_range':[-3,3],
            'x_length':7,
            'y_range':[0,8],
        }
    }
    def construct(self):
        axes=self.get_axes_parabola()
        curva_1=self.get_curve(axes)[0]
        value_tracker=self.get_curve(axes)[1]
        curva_1.add_updater(lambda t: self.update_function(t))
        self.add(axes,curva_1)
        self.play(
            value_tracker.animate.set_value(5),
            run_time=3
        )
        self.wait()
    def get_axes_parabola(self):
        axes_parabola = Axes(**self.CONFIG['config_axes'])
        return axes_parabola
    def get_curve(self,axes):
        value_tracker=ValueTracker(2)
        x_function=lambda x: x**ValueTracker(2).get_value()
        curva_1=axes.plot(x_function,self.CONFIG['config_axes']['x_range'],color=RED)
        return [curva_1,value_tracker]
    def update_function(self,mob):
        axes=self.get_axes_parabola()
        curve=self.get_curve(axes)[0]
        mob.become(curve)
        return mob