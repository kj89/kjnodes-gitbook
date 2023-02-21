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

**live-peers** (38)
```bash
peers="714dfd0efb57197bbcf96b1f8ce9c2cdafd84b72@185.245.183.172:39656,b9c1fb604f314a0b7340bdf2c44fa85ad67ed2ad@38.242.241.61:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,3b2c8bc6a1dba482f6d85e19f78355a9f64950e2@65.109.88.254:32656,ed98dcc0088888d0eb3fbccc207ace26626b92dd@89.117.59.229:26656,d2e3c13b830a7653498553f7423d81607093f7be@147.182.242.103:20656,2f626cb709818afae893a8238946cd176748c622@170.64.188.161:20656,5cef56605237930c81a0c61085c384671356fcb2@161.97.162.189:26656,3a0ce20f65ea3c6ad18938fa4d85f1c34b25ef1e@94.130.132.227:2120,14ba3b19424301a6bb58c27663a0323a81866d5d@134.122.82.186:26656,8f50c04195cc82d0da34e33cfeb0daa694b14479@65.108.105.48:18556,8dea30cdf15deccc3d435fbc799c109c14b3a51f@65.109.88.180:26656,13d97afdbc6150467f7ed3eff40860d82b3ec8ad@38.242.253.207:26656,b98a2a7d2888a63469de4854a088342ad384191a@135.181.150.171:29656,1b4c9d74ca45ff542e8213446e9b384b311d0bea@65.108.200.248:55556,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,a841d3e526089172867a73b709fd14e1d9fb87bd@65.108.231.124:22656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27056,0d0aff593a7672e6b1b3a6898cecfed7624d7a82@141.94.73.93:60556,14ff7bc373e6ffc6978afa3c83c811638a8553a6@85.239.243.210:26656,e615fe1ed10a00ffc6e9911fd201cad557a60976@178.124.214.192:44656,a4ca75792b6802bbe23f409166f29defc8f11b42@159.89.205.107:20656,d387afb4fb00f6c16e6adaee596cf2f75b328146@136.243.88.91:7240,7f21cf9379733e20978b2580892a30cb79a77acf@209.126.9.202:20656,9683a018c2e6815b4f4f607d232d721329ae0a46@176.126.87.86:20656,77c8fe95cc4a1b977e03bda41f47a4fa3e867895@185.202.236.112:20656,045143069de9f5e3e472148c08e3650c109ec52c@18.119.113.123:26656,7f7224da28d362569664faa0430d980982d232a5@144.126.128.215:20656,465b47a9e3e26b385303791bc3c992f42b77393d@65.109.171.155:26656,50c30cc77743dd2adc133f27a8896af015bf5c6d@91.107.242.217:26656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556,0a589d1ce953bb7acaaf5aa9002dfac36fc42649@199.175.98.136:26656,c5a39b97f56d73185ceb904899c65ad8d1390364@199.175.98.135:26656,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,84953f2d118cf38b949164def648d681da375344@65.108.13.185:26959,42f4f53d6ffb55662cf2b65396075f784a1e9a52@5.189.149.159:26656,babc3f3f7804933265ec9c40ad94f4da8e9e0017@38.146.3.101:18556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
