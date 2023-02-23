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
peers="0d0aff593a7672e6b1b3a6898cecfed7624d7a82@141.94.73.93:60556,ee4e7bb1590f16d48576b15198cf1ba99cf42f3e@95.216.198.241:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,3a0ce20f65ea3c6ad18938fa4d85f1c34b25ef1e@94.130.132.227:2120,714dfd0efb57197bbcf96b1f8ce9c2cdafd84b72@185.245.183.172:39656,e8d1a9688c01cdcb3288d8d175f6229487580478@118.68.125.194:20656,14ba3b19424301a6bb58c27663a0323a81866d5d@134.122.82.186:26656,1b4c9d74ca45ff542e8213446e9b384b311d0bea@65.108.200.248:55556,d2e3c13b830a7653498553f7423d81607093f7be@147.182.242.103:20656,4b66ccb20f36e46b980b54f7cd96ee8c4b603a90@65.108.72.233:12656,0a51033bf758d2b4601d4ba65ba6127c5d81cea9@5.9.61.120:33656,2f626cb709818afae893a8238946cd176748c622@170.64.188.161:20656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,465b47a9e3e26b385303791bc3c992f42b77393d@65.109.171.155:26656,3b2c8bc6a1dba482f6d85e19f78355a9f64950e2@65.109.88.254:32656,f28e4984599feefc0490014713cee04c741c711c@65.108.134.215:35656,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27056,e272ef7aeb2d7ac7465f42c3acd499baf4935683@154.26.139.253:17656,7f7224da28d362569664faa0430d980982d232a5@144.126.128.215:20656,c5a39b97f56d73185ceb904899c65ad8d1390364@199.175.98.135:26656,7342199e80976b052d8506cc5a56d1f9a1cbb486@65.21.89.54:26653,9683a018c2e6815b4f4f607d232d721329ae0a46@176.126.87.86:20656,931d82351a5b96a1e9838008636b98c6e6b530bc@65.108.225.158:18556,50c30cc77743dd2adc133f27a8896af015bf5c6d@91.107.242.217:26656,77c8fe95cc4a1b977e03bda41f47a4fa3e867895@185.202.236.112:20656,07dd4b754950bb6c5bf4f5c63d288eea3ef3d982@194.113.106.81:26656,1f19076a29f6f1a01c7ec2d82f66ff7eeb86c875@185.177.116.151:20656,d387afb4fb00f6c16e6adaee596cf2f75b328146@136.243.88.91:7240,7f21cf9379733e20978b2580892a30cb79a77acf@209.126.9.202:20656,8f50c04195cc82d0da34e33cfeb0daa694b14479@65.108.105.48:18556,a4ca75792b6802bbe23f409166f29defc8f11b42@159.89.205.107:20656,41c2771869f1285ba79aabd0568fcd0788d00c7d@65.109.112.20:11154,56995e7d1eb99e8e57fcf57dd739f41234df7467@23.106.238.179:30656,1a32cf8556822038e6dccb368ac998dc14df470d@89.163.142.196:26656,a841d3e526089172867a73b709fd14e1d9fb87bd@65.108.231.124:22656,b9c1fb604f314a0b7340bdf2c44fa85ad67ed2ad@38.242.241.61:20656,ed98dcc0088888d0eb3fbccc207ace26626b92dd@89.117.59.229:26656,0a589d1ce953bb7acaaf5aa9002dfac36fc42649@199.175.98.136:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
