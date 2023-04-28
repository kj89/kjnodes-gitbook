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

**live-peers** (28)
```bash
peers="17c8789ad43655581e4af8c3888192e9ee1b6736@185.177.116.135:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,492adb0eac00feacaeef1aaa9496b8cdb513de44@45.14.194.188:26656,481fcddc51ad2695ef829cd8449d64b7988895db@164.92.250.88:26656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,de9410cc356635b1f555c06332af943319b75a80@109.123.243.29:26656,7fdb0a7a0cfdc159466cb7a91f8553d3555b6c3e@195.2.71.17:26656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,b9da17f4f6ae0acd79608006adf04f2929f3cdf4@149.102.136.187:26656,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,94ccd8ff19555dc1628683881855855276d8af69@185.198.27.2:26656,15bb498412ae171d617fec5525c6be0536fa7352@94.158.152.162:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
