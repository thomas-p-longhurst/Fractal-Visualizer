# CS 1440 Assignment 4.1 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Software Development Plan is comprehensive and well-written<br/>DuckieCorp project conventions are followed<br/>Other required documentation is filled out as well
| 10 pts | A User's Manual explains in simple terms how the program is run<br/>Avoid explaining internal details about how the program works
| 15 pts | A UML class diagram describes your design<br/>Class diagram adheres to UML standards as far as these were explained in class<br/>All modules/classes are represented, behaviors and data members are accounted for, and relationships between modules are described<br/>Names of abstract classes appear in *italics*
| 10 pts | All seven (7) unit tests pass<br/>No trivial unit tests are present
| 20 pts | Factory Method and Strategy design patterns are employed effectively<br/>Default objects are produced by factories as appropriate
| 45 pts | Program requirements are met<br/>New features are competently implemented<br/>Concrete and Abstract classes are used correctly<br/>CLI matches requirements<br/>Error messages are appropriate and informative

**Total points: 110**


## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.

Additionally, this assignment is subject to the following penalties:

0.  **10 point penalty** submitted project is not a clone of the starter code repository.
1.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
2.  **10 point penalty** if `eval()` or a similar function is used by your program.  You should use `int()` and `float()` instead.
3.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
4.  **110 point penalty** if your program imports any modules **except**:
    *   `unittest`
    *   `sys`
    *   `time`
    *   `math`
    *   `tkinter`
    *   modules that are provided by the starter code
    *   modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
5.  **15 point penalty**  if your UML diagram is unreadable.  Watch out for a transparent background (on Diagrams.net, click File -> Export as -> PNG..., then make sure that the option "Transparent background" is left unchecked).  Make sure that the background isn't black, as this obscures the lines connecting classes to each other.  Make sure that the file size is large enough to make the text legible, and that the colors of the diagram stand out in sharp contrast to the background.
6.  **10 point penalty** for each  _trivial_ unit test (i.e. a unit test which unconditionally passes without meaningfully testing some functionality)
