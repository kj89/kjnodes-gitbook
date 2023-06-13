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
peers="fa51a34d907a7680e0622f676d24709ebc148e00@162.19.31.150:55726,711a4b20ce63e3a69725d27c73145519a2a1b559@161.97.159.68:17356,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27286,76fa9d34e68f3e58f4b1dbbc1cb81a02e78530f7@135.181.155.14:26656,d5d9d4b0af4c4ee119cd640fbbca72ff96f5c8c0@209.126.81.240:26631,80cb3138f2f951077c1e70686bb4f59e00cb1fad@135.181.18.112:55726,f93d61f5d8c6f58a60d69c23ff8b6e37ebdfa765@116.202.227.117:51656,af4401e79346aa7309d9e11080a5b71fd3cff283@65.109.56.215:26656,c60e7d9dffdc2b97e9d8b36861ff2e077c863482@65.108.2.41:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
