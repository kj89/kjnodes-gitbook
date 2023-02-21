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

**live-peers** (10)
```bash
peers="c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,13eff3f60e60546435a9f79e241372b299f559a1@5.161.80.223:26656,749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,dff203d0633c98eea4a228c5e913f22236043d89@23.88.69.101:16656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,bcdd1b337504f2d3523f6d63a7de1a2641187908@154.26.130.175:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
