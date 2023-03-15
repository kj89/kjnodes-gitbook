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
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

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

**live-peers** (13)
```bash
peers="433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,82ed4588304873862dfaa403dfe782e92d19b77e@85.208.48.100:36656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
