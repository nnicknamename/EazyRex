  
EasyRex is the the reaction to the complicated nature of regular expressions. Throughout my use of them, I developed small and separate tools that helped me in both the development and the debugging of complex regular expressions. The main issues I faced were the following:

- The difficulty of editing and using large regular expressions, especially when considering the forced horizontal structure.  
- Susceptibility to typos and misspells.  
- Hard to visualize the recognized language when dealing with large expressions.

The goal of EasyRex is to simplify the writing of large regular expressions in an intuitive and scalable way by answering the presented issues.

EasyRex defines regular expressions as operations on a set of base expressions. This structure separates the operations of regular expressions and their arguments, which makes it visually simpler.

This aspect by itself is not a new concept; a lot of libraries already implement such structures, but what EasyRex provides on top of it is what makes it useful. In the construction process, EasyRex can be tasked with a set of __watchers__. These are constraints that Simplex checks while constructing the expression. For example, if you are writing an expression for a language that you know shouldn't accept two consecutive spaces or that shouldn't accept a certain character, EasyRex can be set up with these constraints to alert or raise an exception if such a case is detected.

To address the issue of large regular expressions, EasyRex can visualize the constructed regular expression with a railroad diagram. This is a helpful tool for debugging and visualization.

  
# Note:  
This package is under development; any help is welcome, and make sure not to rely on it for the time being.