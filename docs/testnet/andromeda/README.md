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

**live-peers** (8)
```bash
peers="8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
