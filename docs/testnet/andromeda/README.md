# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (16)
```bash
peers="a478235ecd296f14a2889fac5eb4b43e5e98c239@159.69.64.22:16656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,19f9022eb4d36164288deec5b0badc1ba2e9a1af@89.163.164.110:26656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,66e4051cbbfe428d64b6bd615a7e77b3c4f1ca61@185.215.167.133:46656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,497f453d42d2db70f0af4ca4acb1f85896bf903d@65.108.200.60:26656,4a369367f8ee97c976330f9be79da387d11a0340@65.108.194.44:28656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,e1ca2c14c007cc23e280b191d32b6a3da2389672@65.21.183.66:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
