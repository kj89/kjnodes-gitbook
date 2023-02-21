# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)




## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (40)
```bash
peers="50c30cc77743dd2adc133f27a8896af015bf5c6d@91.107.242.217:26656,77c8fe95cc4a1b977e03bda41f47a4fa3e867895@185.202.236.112:20656,41c2771869f1285ba79aabd0568fcd0788d00c7d@65.109.112.20:11154,1f19076a29f6f1a01c7ec2d82f66ff7eeb86c875@185.177.116.151:20656,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,2f626cb709818afae893a8238946cd176748c622@170.64.188.161:20656,714dfd0efb57197bbcf96b1f8ce9c2cdafd84b72@185.245.183.172:39656,3a0ce20f65ea3c6ad18938fa4d85f1c34b25ef1e@94.130.132.227:2120,14ff7bc373e6ffc6978afa3c83c811638a8553a6@85.239.243.210:26656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,14ba3b19424301a6bb58c27663a0323a81866d5d@134.122.82.186:26656,d2e3c13b830a7653498553f7423d81607093f7be@147.182.242.103:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27056,3b2c8bc6a1dba482f6d85e19f78355a9f64950e2@65.109.88.254:32656,0ac2700e7cb168727e28f77332f810fa9477b92a@108.61.201.223:20656,7f21cf9379733e20978b2580892a30cb79a77acf@209.126.9.202:20656,0d0aff593a7672e6b1b3a6898cecfed7624d7a82@141.94.73.93:60556,aa4a969c9eb0ca62e4168877dc0e403c1364eb92@88.198.52.89:33656,1b4c9d74ca45ff542e8213446e9b384b311d0bea@65.108.200.248:55556,42f4f53d6ffb55662cf2b65396075f784a1e9a52@5.189.149.159:26656,18632bb94974e2038bd8a9345b05b3b45ae319eb@62.171.157.1:46656,8f50c04195cc82d0da34e33cfeb0daa694b14479@65.108.105.48:18556,ff01d363a3459f80d13c39607bb61c640ffafe10@135.181.248.18:29656,7342199e80976b052d8506cc5a56d1f9a1cbb486@65.21.89.54:26653,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,8cd58bdfadefa1302c30b919b4d8ce9acd53fb0d@65.108.9.230:33656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556,e615fe1ed10a00ffc6e9911fd201cad557a60976@178.124.214.192:44656,465b47a9e3e26b385303791bc3c992f42b77393d@65.109.171.155:26656,a4ca75792b6802bbe23f409166f29defc8f11b42@159.89.205.107:20656,7f7224da28d362569664faa0430d980982d232a5@144.126.128.215:20656,9683a018c2e6815b4f4f607d232d721329ae0a46@176.126.87.86:20656,b9c1fb604f314a0b7340bdf2c44fa85ad67ed2ad@38.242.241.61:20656,ed98dcc0088888d0eb3fbccc207ace26626b92dd@89.117.59.229:26656,13d97afdbc6150467f7ed3eff40860d82b3ec8ad@38.242.253.207:26656,f487ab9ef00212a6e0763ab10e64658e1f14a1fc@38.242.235.176:46656,a841d3e526089172867a73b709fd14e1d9fb87bd@65.108.231.124:22656,0a589d1ce953bb7acaaf5aa9002dfac36fc42649@199.175.98.136:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:34256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
