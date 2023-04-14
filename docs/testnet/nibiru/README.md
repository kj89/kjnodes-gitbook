# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (27)
```bash
peers="4e9eca56eab4bfd662a7e35bb1ffb38f97b39ebc@31.220.84.72:26656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,a433076e0bda0bec09153a7185bfd95f6ad92b0d@185.250.36.151:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,17d683da420ce5eaa3fe1b9699b6b7720e4c5483@158.220.100.251:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,95e4f7c7e00838a0a217d58023042cf49c57b94b@45.141.122.68:26656,bf9f870fac4626cd6acf319c9b4fa84b20077194@185.194.217.187:39656,8692da09e683b94c0e90a3ce83e4902459c3d044@31.223.32.35:14546,856f1b729ccb2d0f12bc638ddb71ae49bece70f4@31.220.90.89:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,10d32d2262e7a1d79c4283cef696a521dec43785@85.239.233.155:10656,efaee8ff19257f93a8bb632aeeec29068e9f39c1@95.214.53.37:26656,d191900c45d3df1611aa48c1a3bf24f851dc25c6@165.227.155.35:26656,bf5be00eb2fed367f75b63b9c685ab612765e302@149.102.139.163:26656,676d054de95824a1bf7595973a6bb5a2a955c77f@173.249.59.151:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,e774ca76b7765c49e21daff712fbbc93815771ab@5.9.70.180:15662,852a17f9f2023ac99d499c046995faf52b28e5c2@194.163.142.246:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
