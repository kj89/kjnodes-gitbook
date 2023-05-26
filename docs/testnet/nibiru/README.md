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

**live-peers** (17)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,930b1eb3f0e57b97574ed44cb53b69fb65722786@144.76.30.36:15662,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,790d36e7ea45d6660427d4c7473bac0ef525e78a@184.174.36.119:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,2bfd18d860513e6f0f8c56d4d941b975bf825a50@173.249.7.203:36656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
