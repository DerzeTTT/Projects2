#include <GL/glut.h> // include the GLUT library

void display()
{
    // Set the background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0);

    // Clear the color buffer and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    // Set the drawing color to red
    glColor3f(1.0, 0.0, 0.0);

    // Draw a triangle using glBegin() and glEnd() functions
    glBegin(GL_TRIANGLES);
        glVertex2f(-0.5, -0.5); // first vertex
        glVertex2f(0.5, -0.5); // second vertex
        glVertex2f(0.0, 0.5); // third vertex
    glEnd();

    // Flush the OpenGL pipeline to update the display
    glFlush();
}

int main(int argc, char** argv)
{
    // Initialize the GLUT library and create a window
    glutInit(&argc, argv);
    glutCreateWindow("Triangle");

    // Set the display function
    glutDisplayFunc(display);

    // Enter the GLUT event loop
    glutMainLoop();

    return 0;
}
