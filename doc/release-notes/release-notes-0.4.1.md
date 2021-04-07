BitBridgeCoin version 0.4.1 is now available for download at:
http://sourceforge.net/projects/bitbridgecoin/files/BitBridgeCoin/bitbridgecoin-0.4.1/

This is a bugfix only release based on 0.4.0.

Please report bugs by replying to this forum thread.

MAJOR BUG FIX  (CVE-2011-4447)

The wallet encryption feature introduced in BitBridgeCoin version 0.4.0 did not sufficiently secure the private keys. An attacker who
managed to get a copy of your encrypted wallet.dat file might be able to recover some or all of the unencrypted keys and steal the
associated coins.

If you have a previously encrypted wallet.dat, the first time you run wxbitbridgecoin or bitbridgecoind the wallet will be rewritten, BitBridgeCoin will
shut down, and you will be prompted to restart it to run with the new, properly encrypted file.

If you had a previously encrypted wallet.dat that might have been copied or stolen (for example, you backed it up to a public
location) you should send all of your bitbridgecoins to yourself using a new bitbridgecoin address and stop using any previously generated addresses.

Wallets encrypted with this version of BitBridgeCoin are written properly.

Technical note: the encrypted wallet's 'keypool' will be regenerated the first time you request a new bitbridgecoin address; to be certain that the
new private keys are properly backed up you should:

1. Run BitBridgeCoin and let it rewrite the wallet.dat file

2. Run it again, then ask it for a new bitbridgecoin address.
wxBitBridgeCoin: new address visible on main window
bitbridgecoind: run the 'walletpassphrase' RPC command to unlock the wallet,  then run the 'getnewaddress' RPC command.

3. If your encrypted wallet.dat may have been copied or stolen, send all of your bitbridgecoins to the new bitbridgecoin address.

4. Shut down BitBridgeCoin, then backup the wallet.dat file.
IMPORTANT: be sure to request a new bitbridgecoin address before backing up, so that the 'keypool' is regenerated and backed up.

"Security in depth" is always a good idea, so choosing a secure location for the backup and/or encrypting the backup before uploading it is recommended. And as in previous releases, if your machine is infected by malware there are several ways an attacker might steal your bitbridgecoins.

Thanks to Alan Reiner (etotheipi) for finding and reporting this bug.
