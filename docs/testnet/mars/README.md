# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e8f573d581516235258229f4a86de34f98c0e1ad@173.212.223.170:28656,e3e04058dc376357ad9979b2f0a5e17446e8d0b8@94.103.91.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,9c55f0518b9cb5c4000a7229707f00b787003757@192.99.14.194:26656,5bca99161a02e45e9e3fe6303728f8fd13d3d9d8@65.108.69.68:26757,7f614946315d781fec92baf8cd6475fa6fea482a@65.109.92.148:61356,d2e3c13b830a7653498553f7423d81607093f7be@147.182.242.103:20656,3a3176133ef82ce0bc60608826370945a3620c8a@185.250.37.82:20656,6177977ccd8dcfc6f5ba48bc99b00453cedd3ef3@146.190.172.173:20656,9a191e8b191d1c8e36176b508b9f71f31677f9f8@15.204.207.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
