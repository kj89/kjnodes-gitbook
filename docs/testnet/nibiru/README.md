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

**live-peers** (27)
```bash
peers="ecfb1779940db8a8957f8a5fdcad28edf7606653@161.97.81.245:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,0945129df734538663010c1349f1b4f29da48687@89.117.48.176:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,6903fcc270cb5189033124fece49ce4bb4745ba0@38.242.245.13:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,1d31af8dcbc5a3333eb6583f97ed6b2387d70e72@34.30.60.89:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,c1b40d056e4260a9fa9d1142af1adbeec5039599@142.132.202.50:46656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
