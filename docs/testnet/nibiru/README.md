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
peers="88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
