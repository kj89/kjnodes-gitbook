# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-testnet-005 | **Latest Version Tag**: v1.0.3 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois-testnet](https://explorer.kjnodes.com/nois-testnet)

## Public endpoints

* api: [https://nois-testnet.api.kjnodes.com](https://nois-testnet.api.kjnodes.com)
* rpc: [https://nois-testnet.rpc.kjnodes.com](https://nois-testnet.rpc.kjnodes.com)
* grpc: nois-testnet.grpc.kjnodes.com:15190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nois-testnet.rpc.kjnodes.com:15156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nois-testnet.rpc.kjnodes.com:15159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois-testnet/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="f93d61f5d8c6f58a60d69c23ff8b6e37ebdfa765@116.202.227.117:51656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15156,1e9f3c5da72edebe751b108aa52657b190c8991d@65.108.225.158:17356,457a8e8dcb3bef4d7a6fd7fcb3b97d1282ca029c@65.108.206.118:60856,4af23e5bbb434e58082054a7d97b41b62cdb4a83@195.201.197.4:30656,6d6164cd45c7c65ab76abd40f5ff683f72e7f50f@65.109.92.241:40136,80cb3138f2f951077c1e70686bb4f59e00cb1fad@135.181.18.112:55726,2403cecea3dc5c6bcac9ff964095ac673fbc02ef@65.109.39.223:26636,5ecd40831e453845587cbd03534e68a7b9fc3576@65.109.92.79:21656,08b081a1791ff0a8fdfa1d8e4a3c7e17af7a91aa@65.109.158.90:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
