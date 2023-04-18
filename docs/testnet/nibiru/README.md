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

**live-peers** (28)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,796c8546e5ba9d5ba119f377e783ec512d54cf42@38.242.153.107:26656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,83be009ed822ad05d877c26bfa457c95551128c0@167.99.249.130:26656,e3bcf7faf6efca24f6d0735bc96f67929a8164d3@164.90.217.176:26656,f8c257cf4791ba315ac8b291a065e825afd7310c@195.201.85.236:11656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,4a44af55ee65d15c13d666bb5d830da43673f7a9@185.190.140.80:26656,e1a8a5f0b0d6ad3a2e39560dc282f96ff023919d@77.220.215.44:26656,c0bca259cb7611549f0c41d9e0c311e40b705b63@38.242.153.84:26656,fa50b2f85e74098c7dd8e0ffa6c102181fea6ae2@38.242.228.88:39656,9bf81d292a0cb72a1920b50d63dd1dc881ed0a2f@5.199.138.18:39656,d0c580a19e635fdb2d60d56b9462c0aa4e4517d6@207.180.227.122:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,049f949ef374eb0202685e17742241005acde129@38.242.152.36:26656,015a39332269be67fb95317038e8c9c57c6ca121@167.71.209.28:39656,fd0379ae2ef2bfb7f174d0171c06f0bc5bcd286f@183.2.149.136:26656,3a0b54203d91571398a5b4538a938fd464c4d871@176.117.185.56:40656,129586ad8f2e42c87d8811012107581b3eb0a1b1@146.0.35.40:26656,4b38d4082e88f3623233915c240f112b25b442ba@84.46.245.66:26656,3a5d2bd306d6a0b842e5b14dfd1fc5a1069b55d1@14.162.213.215:20156,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,d1d23f77c7498e63c20d2ddb1ccf0a2bc04a5b5c@38.242.157.163:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
