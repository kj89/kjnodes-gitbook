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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,799ecf85b985e44ba30f3ff1c9da11fd4064d041@86.48.2.182:26656,ac6c000f0d3980066fb771a3b4831272aed62da2@54.165.89.184:26656,58dbb25e697d832d54997177ece80c1b94baef61@178.62.208.204:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,4af344bb3302bf926580f0b8ea4de9be401c3522@94.131.111.156:26656,852a17f9f2023ac99d499c046995faf52b28e5c2@194.163.142.246:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,4e9eca56eab4bfd662a7e35bb1ffb38f97b39ebc@31.220.84.72:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,eddac5bfe62acf85ab2f541ff2de4f2918daf23d@31.220.78.100:39656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,d4bb11fc3fdf834e13a803f159dfe12851c4b1c1@86.48.3.201:26656,ebce72e66d97eafa364fd65fb19d945748eab36d@43.134.36.145:26656,f509244124091fbf57494d825f2c49d5bd2c093f@120.226.39.114:26656,3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,9920bfdee1f9f61221e0301b1823f050e8fb992f@193.203.203.121:26656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
