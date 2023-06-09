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

**live-peers** (12)
```bash
peers="5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
