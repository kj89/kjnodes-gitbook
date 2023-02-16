# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.6 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)




## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (23)
```bash
peers="c20f2216b56cb24921b688a6cffc7fe09799a069@162.55.103.44:26656,0188d0143ea4311923a809bb07ee9ebf13c0c63b@94.130.16.254:60656,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,b8802200255f4e02cb3e0e1c71f1172bf074364a@65.108.97.58:31656,56615e02aa90e35a20a1fc4c46e78bb00956f07b@192.118.76.199:26681,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,1dae68f061204fe2c10e9476239c0333258889e7@65.109.31.114:2460,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,c5d8ad1f942cd9b9839f65a6543c460bfa1af161@38.242.221.205:26656,de1f980cc59bdb2457202768d4b4d964d783789e@167.235.21.165:36656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556,3d6fdf19781c7725b5d23ebbef5950aab073c9f9@95.111.225.137:41656,5b4482bfe02384184470070c3d3a4465cf0c18d4@144.91.82.61:31656,63db727618b237d4a27656aa456be2812154bf29@65.109.170.47:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
