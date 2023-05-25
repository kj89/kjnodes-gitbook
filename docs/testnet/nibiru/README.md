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

**live-peers** (23)
```bash
peers="25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,930b1eb3f0e57b97574ed44cb53b69fb65722786@144.76.30.36:15662,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
