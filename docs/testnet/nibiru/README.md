# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (9)
```bash
peers="0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
