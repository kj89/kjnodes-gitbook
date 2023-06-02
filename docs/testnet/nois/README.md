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
peers="4af23e5bbb434e58082054a7d97b41b62cdb4a83@195.201.197.4:30656,fa51a34d907a7680e0622f676d24709ebc148e00@162.19.31.150:55726,5ecd40831e453845587cbd03534e68a7b9fc3576@65.109.92.79:21656,af4401e79346aa7309d9e11080a5b71fd3cff283@65.109.56.215:26656,2403cecea3dc5c6bcac9ff964095ac673fbc02ef@65.109.39.223:26636,80cb3138f2f951077c1e70686bb4f59e00cb1fad@135.181.18.112:55726,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15156,711a4b20ce63e3a69725d27c73145519a2a1b559@161.97.159.68:17356,c60e7d9dffdc2b97e9d8b36861ff2e077c863482@65.108.2.41:60656,65acf20f39df51e09027a2f204e359d57823a995@65.108.72.253:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
