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

**live-peers** (21)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,33bae0a8e95d0adc364b5feb44a766100b927e86@91.196.164.89:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:26656,ecfb1779940db8a8957f8a5fdcad28edf7606653@161.97.81.245:26656,4af344bb3302bf926580f0b8ea4de9be401c3522@94.131.111.156:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,e774ca76b7765c49e21daff712fbbc93815771ab@5.9.70.180:15662,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,4dc627534292d408d9087b7d62e59a10fdf99e7f@65.109.60.19:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
