# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="19f9022eb4d36164288deec5b0badc1ba2e9a1af@89.163.164.110:26656,360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,497f453d42d2db70f0af4ca4acb1f85896bf903d@65.108.200.60:26656,38a546d75ae84bb002990ce2eb35c04d7d284809@159.223.69.214:26656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
