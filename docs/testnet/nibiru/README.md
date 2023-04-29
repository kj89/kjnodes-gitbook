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
peers="b9da17f4f6ae0acd79608006adf04f2929f3cdf4@149.102.136.187:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,345cfe2a2081fee1788ee54fbb106be4900c0294@148.251.10.110:27060,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,0e90ac8e15b040c2a158b68f25299fc32a9d5940@89.117.57.25:26656,e0312a70844803297269124468f070a84f06777c@65.108.41.173:28056,b380fa4928c0a8078b5046f6f70991395aa3f79e@91.107.232.208:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,9df18d7fe13517817100466c2c7980c6125354b7@136.243.172.166:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,765e15c46b4ca251e3cf180a6ffdcfd5d2158dd2@185.196.20.165:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,db1deb2f4d23eb91da1d10e86562d84aaa0f9a0e@5.75.239.226:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,492adb0eac00feacaeef1aaa9496b8cdb513de44@45.14.194.188:26656,65979cd3ccfc446e7a347669fa212ffad080bb07@109.172.45.168:26656,de9410cc356635b1f555c06332af943319b75a80@109.123.243.29:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
