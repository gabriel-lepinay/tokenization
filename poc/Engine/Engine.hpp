/*
** Gaby, 2024
** poc
** File description:
** Engine
*/

#ifndef ENGINE_HPP_
    #define ENGINE_HPP_

    #include <iostream>


class Engine {
    public:
        Engine();
        ~Engine();
        bool run();
        int selectMode(int ac, char **av);
        std::string tokenize();
        std::string detokenize();
        void generateToken();


        int getMode() const { return mode; }
        void setMode(int mode) { this->mode = mode; }
        std::string getAsset() const { return asset; }
        void setAsset(std::string asset) { this->asset = asset; }
        int getNbTokenToGenerate() const { return nbTokenToGenerate; }
        void setNbTokenToGenerate(int nbTokenToGenerate) { this->nbTokenToGenerate = nbTokenToGenerate; }
    private:
        int mode = 0;
        std::string asset;
        int nbTokenToGenerate = 0;
};

#endif /* !ENGINE_HPP_ */
