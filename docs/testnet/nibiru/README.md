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

**live-peers** (11)
```bash
peers="7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,930b1eb3f0e57b97574ed44cb53b69fb65722786@144.76.30.36:15662,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
