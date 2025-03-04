import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.left(45)
    t.backward(branch_length)

def pythagoras_tree(level):
    window = turtle.Screen()
    window.title("Pythagoras tree")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    draw_pythagoras_tree(t, 100, level)

    window.mainloop()

if __name__ == "__main__":
    level = int(input("Enter the recursion level for the Pythagorean tree: "))
    pythagoras_tree(level)