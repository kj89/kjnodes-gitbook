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

**live-peers** (9)
```bash
peers="4af23e5bbb434e58082054a7d97b41b62cdb4a83@195.201.197.4:30656,f93d61f5d8c6f58a60d69c23ff8b6e37ebdfa765@116.202.227.117:51656,00c205b11dc2d2295749810722bb2e995a24c0c1@95.216.14.58:60656,fa51a34d907a7680e0622f676d24709ebc148e00@162.19.31.150:55726,af4401e79346aa7309d9e11080a5b71fd3cff283@65.109.56.215:26656,32e0934cb169db0745ee16dae2e529bb1dd59c2c@135.181.252.92:26656,d5d9d4b0af4c4ee119cd640fbbca72ff96f5c8c0@209.126.81.240:26631,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15156,08b081a1791ff0a8fdfa1d8e4a3c7e17af7a91aa@65.109.158.90:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
