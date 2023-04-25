# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (25)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,8a1f817ac4f718891cd12ae7dfc1e47cc3c97844@81.0.218.22:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,4e60470d4e89d6bc76f9f48bfb4a99a0f0341a4c@176.124.221.194:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,33bae0a8e95d0adc364b5feb44a766100b927e86@91.196.164.89:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,96285853644bd5c35db33b033abfed598c9c10c0@75.119.130.70:26656,4a69cf47cdb9643295b7a59c07b4a74a97b65963@149.154.69.221:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,e9a824e54f1161a85a3044f48968ee28404ce5fc@183.2.149.136:26656,d1d23f77c7498e63c20d2ddb1ccf0a2bc04a5b5c@38.242.157.163:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,bc60bfcadd0f0d5ea25a9b7165303f26b67d4365@185.217.125.43:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,7fdb0a7a0cfdc159466cb7a91f8553d3555b6c3e@195.2.71.17:26656,549a5eb615e8560105f3801315a07c49c1804f48@158.220.98.245:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
