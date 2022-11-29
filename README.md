Template for cpp projects.

Requires python to build (and g++).

- src for source files
- include for headers (for libs)
- lib for static precompiled binaries (.a) everything in this folder will be included in the build

If you want to make changes to the build script just edit build.py

Not that i haven't actually tested this on windows. So the glfw lib files for windows might be wrong. Alsow pretty sure for windows i need to add GLEW or something. But i'll do that later..... For now it works on mac though
