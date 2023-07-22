#include <assert.h>

#include <iostream>
using std::cout;
using std::endl;

#include <string>
using std::string;
#include <cryptopp/osrng.h>

using CryptoPP::AutoSeededRandomPool;

#include <cryptopp/aes.h>
using CryptoPP::AES;

#include <cryptopp/integer.h>
using CryptoPP::Integer;

#include <cryptopp/sha.h>
using CryptoPP::SHA1;

#include <cryptopp/filters.h>
using CryptoPP::StringSource;
using CryptoPP::StringSink;
using CryptoPP::ArraySink;
using CryptoPP::SignerFilter;
using CryptoPP::SignatureVerificationFilter;

#include <cryptopp/files.h>
using CryptoPP::FileSource;
using CryptoPP::FileSink;

#include <cryptopp/eccrypto.h>
using CryptoPP::ECDSA;
using CryptoPP::ECP;
using CryptoPP::DL_GroupParameters_EC;

#include <cryptopp/oids.h>
using CryptoPP::OID;
using CryptoPP::byte;

#include <fstream>
#include <iterator>
#include <vector>
#include "cryptopp/filters.h"
#include "cryptopp/base64.h"
using CryptoPP::Base64Encoder;
using CryptoPP::StringSource;
using CryptoPP::StringSink;

void LoadPublicKey(const string& filename, ECDSA<ECP, SHA1>::PublicKey& key);
bool VerifyMessage(const ECDSA<ECP, SHA1>::PublicKey& key, const string& message, const string& signature);

int main(int argc, char* argv[])
{
    //Load public key
    ECDSA<ECP, SHA1>::PublicKey publicKey;
    LoadPublicKey("ec.public.key", publicKey);

    //Verify message
    std::vector<string> lsdir = { "01ca46bc0ac04e09888a241ced9e290c.png", "5ecf653a589b3980a8a166e404069edc.png", "62b7f87696d98b562540881d83fdba18.png", "3449febf4cfb168d1002d84e0da97a56.png", "6538fa0733f048ca52a95e3eb0eeefc2.png", "9557d3da1cb52dc7541d778f68c3730c.png", "b67dc736bd7c6818bb0885de0eba58b9.png", "b90b1a57cdff43c0721cb7afd955f10c.png", "d27a1a4ae33ab2dc6a510b4093c270ce.png", "ff56449f20dffe819908ffd65bb7feab.png" };

    for (int i = 0; i < 10; i++) {
        bool result = false;
        string filename = lsdir[i];
        string message;
        FileSource file(filename.c_str(), true, new CryptoPP::StringSink(message));

        string image = message.substr(0, message.length() - 42);
        string signature = message.substr(message.length() - 42);

        string encoded;
        StringSource(image, true, new Base64Encoder(new StringSink(encoded)));

        result = VerifyMessage(publicKey, encoded, signature);
        string result_str = (result) ? "valid" : "invalid";
        cout << filename << " " << result_str << endl;

    }
    system("pause");
    return 0;
}

void LoadPublicKey(const string& filename, ECDSA<ECP, SHA1>::PublicKey& key)
{
    key.Load(FileSource(filename.c_str(), true /*pump all*/).Ref());
}

bool VerifyMessage(const ECDSA<ECP, SHA1>::PublicKey& key, const string& message, const string& signature)
{
    bool result = false;

    StringSource(signature + message, true,
        new SignatureVerificationFilter(
            ECDSA<ECP, SHA1>::Verifier(key),
            new ArraySink((byte*)&result, sizeof(result))
        ) // SignatureVerificationFilter
    );

    return result;
}
