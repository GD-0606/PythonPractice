const crypto = require('crypto');
const querystring = require('querystring');

function oneLoginDecryptData(cipherText) {
    const token = 'AU68vf26spwX'; // Updated token

    // Derive key from token and salt using PBKDF2
    const key = crypto.pbkdf2Sync(token, 'V*GH^|9^TO#cT', 1000, 32, 'sha1');

    // Decode the URL-encoded and base64-encoded ciphertext
    const decodedCipherText = Buffer.from(querystring.unescape(cipherText), 'base64');

    // Extract IV and key for AES from the derived key
    const iv = key.slice(16, 32); // IV should be 16 bytes for AES-128
    const aesKey = key.slice(0, 16); // AES key should be 16 bytes for AES-128

    try {
        // Decrypt the data
        const decipher = crypto.createDecipheriv('aes-128-cbc', aesKey, iv);
        decipher.setAutoPadding(true); // Let the library handle padding

        let decrypted = decipher.update(decodedCipherText, 'binary', 'utf8');
        decrypted += decipher.final('utf8');

        return decrypted;
    } catch (error) {
        console.error('Decryption failed:', error.message);
        return null;
    }
}

// TESTS
const cipherText = 'dddmJm8DT0VL5r36QIKwRE%2bbzXbqI3QeYWhiyeWe2I650Z%2fMKqHY4Ng4h5dNSsDZGNWoDQ34w%2bG5P4M%2fTGXQrXoSgpJwHCRKTIuMP5DNgHxYUbeE3xkMhbcdWZUUTGunRqgbJ0bHacm5I79DPMv6Ijg%2fILFVOsqB4ZkBgeDXsVMIXRvETYEVuoFj8JTsd6J%2bwnWXRT8LU%2b4kZUc5v2o%2bOnpAXxjj9Otv%2bToXm4lyVhY%3d';
console.log("AU68vf26spwX".length);

console.log('Plaintext: ' + oneLoginDecryptData(cipherText));
