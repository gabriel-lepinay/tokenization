/*
** Gaby, 2024
** poc
** File description:
** Engine
*/

#include "Engine.hpp"

Engine::Engine()
{
}

Engine::~Engine()
{
}

int Engine::selectMode(int ac, char **av)
{
    if (ac != 3) {
        if (ac > 1 && std::string(av[1]) == "-h") {
            std::cout << "Usage: ./poc [mode] [asset/x]\n\t mode:\n\t\t0: Tokenize\n\t\t1: Detokenize\n\t\t1: Generate x token x: int > 0." << std::endl;
            return (1);
        }
        std::cerr << "Wrong usage.\n\tUse -h for help." << std::endl;
        return (-1);
    }

    if (std::string(av[1]) == "0")  {
        setMode(0);
        setAsset(std::string(av[2]));
    } else if (std::string(av[1]) == "1") {
        setMode(1);
        setAsset(std::string(av[2]));
    } else if (std::string(av[1]) == "2") {
        setMode(2);
        try {
            setNbTokenToGenerate(std::stoi(av[2]));
        } catch (std::exception &e) {
            std::cerr << "Wrong usage.\n\tUse -h for help." << std::endl;
            return (-1);
        }
    } else {
        std::cerr << "Wrong usage.\n\tUse -h for help." << std::endl;
        return (-1);
    }
    return (0);
}

bool Engine::run()
{
    if (getMode() == 0)
        tokenize();
    if (getMode() == 1)
        detokenize();
    if (getMode() == 2)
        generateToken();
    return (true);
}

std::string Engine::tokenize()
{
    std::string tokenized = "";
    std::cout << "Tokenizing " << getAsset() << std::endl;
    return (tokenized);
}

std::string Engine::detokenize()
{
    std::string detokenized = "";
    std::cout << "Detokenizing " << getAsset() << std::endl;
    return (detokenized);
}

void Engine::generateToken()
{
    std::cout << "Generating " << getNbTokenToGenerate() << " token" << std::endl;
}