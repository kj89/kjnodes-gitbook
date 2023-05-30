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

**live-peers** (19)
```bash
peers="151add3a88c91fdcfce837a58eee8d8d8c9bf960@31.220.84.73:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,ce2dcfe5794bed1d4b32b8a43b32afc5d5e435f2@135.181.114.98:46656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
