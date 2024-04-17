/*
** Gaby, 2024
** poc
** File description:
** main
*/

#include "Engine.hpp"

int main(int ac, char** av) {
    Engine engine;
    int status = 0;

    status = engine.selectMode(ac, av);
    if (status == -1)
        return 84;
    if (status == 0)
        engine.run();
    return 0;
}



