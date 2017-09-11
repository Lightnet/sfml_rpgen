/*
 * 
 * main entry point
 */


#include "rpgen/sfml_rpgen.h"
//#include "rpgen/sfml_gl.h"
//#include "rpgen/sfml_imgui.h"
//#include "rpgen/sfml_scene.h"



#include <stdio.h>

#undef main

int main(int argc, char* argv[]) //main entry point
{

    //example tests
    //sfml_gl(argc, argv);
    //sfml_imgui(argc, argv);
    //sfml_scene(argc, argv);

    //RPG
    sfml_rpgen(argc, argv);

    return 0;
}