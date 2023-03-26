// import { join } from 'path';
// const fs = require('fs');

let port, password, protocol, name, PID, accessToken, entitlementToken, lockFilePath;

// make a funcion that returns a file path
function getLockFilePath() {
    return process.env.LOCALAPPDATA + '\\Riot Games\\Riot Client\\Config\\lockfile';
}

function readLockFile(filePath) {
    // read the lockfile
    try{
        const data = fs.readFileSync(filePath, 'utf8').split(':');
        name = data[0];
        PID = data[1];
        port = data[2];
        password = data[3];
        protocol = data[4];
        return true;
    }
    catch(err) {
        alert('Error reading lockfile: ' + err);
        return false;
    }
}

// Wait for the window to load before adding the click event listener
window.onload = () => {
    let button = document.getElementById('ValoButton');
    button.addEventListener('click', () => {
        // check if the lockfile exists
        alert('Checking if lockfile exists...');
        let lockFileExists = readLockFile(getLockFilePath());
        if (lockFileExists) {
            alert('Lockfile exists!');
        }
    });
};