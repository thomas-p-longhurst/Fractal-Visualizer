# CS 1440 Assignment 4.0 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Software Development Plan is comprehensive and well-written<br/>DuckieCorp project conventions are followed<br/>Other required documentation is filled out as well
|20 pts  | Code smells are cataloged in `doc/Smells.md`<br/>Each piece of required information is included: location, code snippet, explanation and fix description
|10 pts  | A User's Manual explains in simple terms how the program is run<br/>Avoid explaining internal details about how the program works
|15 pts  | A UML class diagram describes your design<br/>Class diagram adheres to UML standards as far as these were explained in class<br/>All modules/classes are represented, behaviors and data members are accounted for, and relationships between modules are described
|20 pts  | Increase coverage of unit tests to seven (7) tests<br/>All unit tests pass<br/>No trivial unit tests are present
|10 pts  | The original user interface functionality is preserved<br/>No new features or capabilities are added to the refactored program
|25 pts  | Program requirements are met<br/>The new code is cleaner than the original starter code

**Total points: 110**


## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.

Additionally, this assignment is subject to the following penalties:

0.  **10 point penalty** The last commit of this assignment does not bear the tag `Assn4.0`.
1.  **10 point penalty** submitted project is not a clone of the starter code repository.
2.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
3.  **10 point penalty** if `eval()` or a similar function is used by your program.  You should use `int()` and `float()` instead.
4.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
5.  **110 point penalty** if your program imports any modules **except**:
    *   `unittest`
    *   `sys`
    *   `time`
    *   `math`
    *   `tkinter`
    *   modules that are provided by the starter code
    *   modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
6.  **15 point penalty**  if your UML diagram is unreadable.  Watch out for a transparent background (on Diagrams.net, click File -> Export as -> PNG..., then make sure that the option "Transparent background" is left unchecked).  Make sure that the background isn't black, as this obscures the lines connecting classes to each other.  Make sure that the file size is large enough to make the text legible, and that the colors of the diagram stand out in sharp contrast to the background.
7.  **10 point penalty** for each  _trivial_ unit test (i.e. a unit test which unconditionally passes without meaningfully testing some functionality)
