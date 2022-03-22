from MultiarcPath import *
from PathView import PathView
from Problem import Problem


def main():
    nums_appr = 100  # control the number of points by bezier approximation
    problem = Problem.create_quarter_circle_problem()
    '''
    plot
    '''
    # pathView = PathView(problem, nums_appr)
    # pathView.add("bezier", "b", 1)
    # pathView.add("bezier", "y", 0.8)
    # pathView.add("bezier", "g", 0.6)
    # pathView.add("bezier", "c", 0.4)
    # pathView.add("bezier", "m", 0.2)
    # # pathView.add("multiarcPath", "r")
    # # pathView.add("bspline", "g")
    # # pathView.add("cubicspline", "y")
    # # pathView.add_control_points()
    # pathView.add_arrow()
    # pathView.show()

    pathView = PathView(problem, nums_appr)
    pathView.add("bezier", "b", 0.4)
    pathView.add_multiarc("bezier", "r", 0.4)
    pathView.add_arrow()
    pathView.show()

    pathView = PathView(problem, nums_appr)
    # pathView.add_curvature("bezier", "-b", 1)
    # pathView.add_curvature("bezier", "-y", 0.8)
    # pathView.add_curvature("bezier", "-g", 0.6)
    # pathView.add_curvature("bezier", "-c", 0.4)
    pathView.add_curvature("bezier", "-m", 0.4)
    # # pathView.add_curvature("bspline", "r")
    # # pathView.add_curvature("cubicspline", "y")
    pathView.show()


if __name__ == '__main__':
    main()
