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

**live-peers** (9)
```bash
peers="749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,5e5186020063f7f8a3f3c6c23feca32830a18f33@65.109.174.30:56656,360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
