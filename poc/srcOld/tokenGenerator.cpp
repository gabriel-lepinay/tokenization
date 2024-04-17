/*
** Gaby, 2024
** poc
** File description:
** randomStr
*/

// g++ -Wall -o cppTokenGenerator src/tokenGenerator.cpp -lssl -lcrypto

#include <iostream>
#include <cstdlib>

#include <openssl/rand.h>
#include <openssl/core.h>
#include <openssl/evp.h>
#include <openssl/provider.h>
#include <iostream>
#include <iomanip>
#include <string>

#include <iostream>

std::string sha256(const std::string &str) {
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    const EVP_MD *md = EVP_sha256();
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int hash_len;

    EVP_DigestInit_ex(mdctx, md, NULL);
    EVP_DigestUpdate(mdctx, str.c_str(), str.size());
    EVP_DigestFinal_ex(mdctx, hash, &hash_len);
    EVP_MD_CTX_free(mdctx);

    std::stringstream ss;
    for (unsigned int i = 0; i < hash_len; i++)
        ss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);

    return ss.str();
}

unsigned int randomNumber() {
    unsigned char buffer[4];

    if (RAND_bytes(buffer, sizeof(buffer)) != 1) {
        std::cerr << "Error generating random number" << std::endl;
        return 1;
    }
    unsigned int random_number = 0;
    for (size_t i = 0; i < sizeof(buffer); ++i) {
        random_number <<= 8;
        random_number |= buffer[i];
    }

    return random_number;
}


std::string strGenerator(int length) {
    std::string str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    std::string newStr;

    for (int i = 0; i < length; i++) {
        newStr += str[rand() % str.size()];
    }
    return newStr;
}

int main() {
    clock_t start, end;
    // connect to db
    start = clock();

    unsigned int seed = randomNumber();
    srand(seed);

    std::string str = strGenerator(16);
    std::string hashed = sha256(str);
    std::cout << "SHA256 hash of '" << str << "': " << hashed << std::endl;
    // add to db
    end = clock();
    std::cout << "C++ execution time: " << (double)(end - start) / CLOCKS_PER_SEC << " seconds" << std::endl;
    return 0;
}