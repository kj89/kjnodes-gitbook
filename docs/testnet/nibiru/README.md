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

**live-peers** (27)
```bash
peers="25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,e9a824e54f1161a85a3044f48968ee28404ce5fc@183.2.149.136:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,d0b30b6fdd2df3e70e41fb0ba43b400e7d02e6e0@38.242.252.252:26656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,ac7f7e919e67a1de4fc4003c46fa04ccce13d81f@139.192.3.222:39656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,ca91b6230e92ee6f5b9c5b1fe80fa07a1b72225a@185.211.6.205:26656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,2fe037c0e7a8f3da20ef50f20712b55fd52a9b8b@144.91.110.211:29656,aa999ecb4e74d0b95465638670cd6fddc9c1f544@65.109.89.37:26656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,0f486f06c3808ca0f6b1ceeb9e81d6f41972333a@149.102.152.218:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,df070f411293136cc09c6e1e244525e7283e2188@194.163.175.66:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,4705e330d64ffcc36ef9fe50556f5e44c20a167d@108.61.205.9:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
