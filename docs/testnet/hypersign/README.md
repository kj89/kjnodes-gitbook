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
peers="c5d8ad1f942cd9b9839f65a6543c460bfa1af161@38.242.221.205:26656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,54f5df8d6516ead7099191776d9ee2048e0ec947@95.214.53.46:26656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,ec5127072c252f7246fb66f7e7762423a23ff6bd@154.12.228.93:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,fbc7ce82f02e24257395dc0310ad2921ea61e199@65.109.92.148:61156,1de2abae74a4c5fd7d96d9869ef02187f81498f0@134.209.238.66:26656,610843eda2f0388cb8e75917e8c1f63350bd3bd1@154.26.131.130:16656,4e08d5b0cb43c8d5ffc42987a5166bab2a04a93b@65.109.92.240:21066,1e3f0aeb6f2a2017b122af2461a75c9695790954@65.108.233.109:10956,62c3f3e5214495593ad204f3c6cd879f3f4ed6a9@5.9.79.121:26656,e003e628d5c748f2445f1731af20d461f585e7a5@182.253.224.66:12656,eaf27acc810a3d6728dde972ebad26810cce0ae6@65.108.229.233:26656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,52eee2c34150d621312087e49f118969472ba55f@149.102.137.192:26656,a3f3d6dba11bfe080693938666064b2324fbaccf@88.99.164.158:11056,63db727618b237d4a27656aa456be2812154bf29@65.109.170.47:26656,c1b6d86f46eab9d0aa2e4399cddb9cf05d13621a@65.108.206.118:60556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
